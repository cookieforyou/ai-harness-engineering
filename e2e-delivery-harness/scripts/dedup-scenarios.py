#!/usr/bin/env python3
"""
P0-1 v3: Targeted dedup for Pattern B scenarios.
Removes specific generic template sections while preserving:
- Domain Chain of Thought (first occurrence)
- Domain Error Handling (English header without parenthetical)
- Domain Quality Metrics (English header without parenthetical)
- Decision Checkpoints
- Handover Criteria (交接标准)
- Workflow / Related Scenarios
- Handover Context Template YAML
"""
import re
import sys
from pathlib import Path

SCENARIOS_DIR = Path("./scenarios")

# Template-only section headers to remove (these are always generic)
TEMPLATE_SECTIONS_TO_REMOVE = [
    '## Primary Assets',
    '## Expected Output',
    '## Quality Gates',
    '## Metrics',
]

# Generic template report sections (contain placeholder content)
GENERIC_REPORT_PATTERN = r'^## .* Report$'

# Sections that are ALWAYS generic (Chinese-named with parenthetical)
GENERIC_COT = '## Chain of Thought (思维链)'
GENERIC_ERR = '## Error Handling (错误处理)'
GENERIC_QM = '## Quality Metrics (质量指标)'


def find_section_end(lines, start):
    """Find end of section (next ## header or ### or EOF)."""
    for i in range(start + 1, len(lines)):
        if re.match(r'^## |^### ', lines[i]):
            return i
    return len(lines)


def fix_pattern_b(filepath):
    """Fix Pattern B: remove interleaved generic template sections."""
    with open(filepath, 'r') as f:
        lines = f.read().split('\n')

    original_count = len(lines)
    lines_to_remove = set()
    removed_desc = []

    # Track occurrences
    cot_count = 0
    err_cn_count = 0
    qm_cn_count = 0

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Handle generic CoT: keep first, remove subsequent
        if line == GENERIC_COT:
            cot_count += 1
            if cot_count > 1:
                end = find_section_end(lines, i)
                for j in range(i, end):
                    lines_to_remove.add(j)
                removed_desc.append(f'CoT(思维链)#{cot_count} L{i+1}-{end}')
                i = end
                continue

        # Handle generic Error Handling (错误处理): remove ALL occurrences
        # (domain one uses English header without parenthetical)
        if line == GENERIC_ERR:
            err_cn_count += 1
            end = find_section_end(lines, i)
            for j in range(i, end):
                lines_to_remove.add(j)
            removed_desc.append(f'ErrorHandling(错误处理)#{err_cn_count} L{i+1}-{end}')
            i = end
            continue

        # Handle generic Quality Metrics (质量指标): remove ALL occurrences
        if line == GENERIC_QM:
            qm_cn_count += 1
            end = find_section_end(lines, i)
            for j in range(i, end):
                lines_to_remove.add(j)
            removed_desc.append(f'QualityMetrics(质量指标)#{qm_cn_count} L{i+1}-{end}')
            i = end
            continue

        # Remove template-only sections
        if line in TEMPLATE_SECTIONS_TO_REMOVE:
            end = find_section_end(lines, i)
            for j in range(i, end):
                lines_to_remove.add(j)
            removed_desc.append(f'{line} L{i+1}-{end}')
            i = end
            continue

        # Remove generic report templates
        if re.match(GENERIC_REPORT_PATTERN, line):
            end = find_section_end(lines, i)
            section_text = '\n'.join(lines[i:end]).lower()
            # Check if it's a template by looking for placeholder patterns
            placeholder_count = len(re.findall(r'\{\{|\[Description\]|\[Expected', section_text))
            if placeholder_count >= 3 or len(lines[i:end]) < 10:
                for j in range(i, end):
                    lines_to_remove.add(j)
                removed_desc.append(f'{line}(template) L{i+1}-{end}')
                i = end
                continue

        i += 1

    if not lines_to_remove:
        return False, "No generic sections found"

    # Build new content, preserving Handover Context Template
    new_lines = [l for idx, l in enumerate(lines) if idx not in lines_to_remove]

    # Collapse multiple consecutive blank lines
    cleaned = []
    prev_blank = False
    for line in new_lines:
        is_blank = line.strip() == ''
        if is_blank and prev_blank:
            continue
        cleaned.append(line)
        prev_blank = is_blank

    content_out = '\n'.join(cleaned).rstrip('\n') + '\n'

    with open(filepath, 'w') as f:
        f.write(content_out)

    removed = original_count - len(cleaned)
    return True, f"Removed {removed} lines: {', '.join(removed_desc)}"


def main():
    # Only process the 8 Pattern B files that need interleaved dedup
    pattern_b_files = [
        'audit-security',
        'performance-testing',
        'plan-capacity',
        'review-code',
        'review-incident',
        'review-design',
        'migrate-data',
        'manage-change',
    ]

    fixed = 0
    for name in pattern_b_files:
        filepath = SCENARIOS_DIR / name / 'SCENARIO.md'
        try:
            was_fixed, msg = fix_pattern_b(filepath)
            if was_fixed:
                hct = '✅' if 'Handover Context Template' in open(filepath).read() else '⚠️ NO HCT'
                print(f"✅ {name}: {msg} | {hct}")
                fixed += 1
            else:
                print(f"⏭️  {name}: {msg}")
        except Exception as e:
            print(f"❌ {name}: ERROR - {e}")

    print(f"\nPattern B fixed: {fixed}/{len(pattern_b_files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
