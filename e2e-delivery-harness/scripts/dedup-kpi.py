#!/usr/bin/env python3
"""
P1-1: Remove generic KPI-001~004 sections from scenarios.
Keeps domain-specific KPIs, removes generic template KPI blocks.
"""
import re
import sys
from pathlib import Path

SCENARIOS_DIR = Path("./scenarios")

GENERIC_KPI_MARKER = '### Key Performance Indicators (KPIs)'
GENERIC_VALIDATION_MARKER = '### Validation Checklist (验证清单)'
GENERIC_QM_HEADER = '## Quality Metrics (质量指标)'


def find_section_end(lines, start):
    """Find end of section (next ## or ### or EOF)."""
    for i in range(start + 1, len(lines)):
        if re.match(r'^## |^### ', lines[i]):
            return i
    return len(lines)


def remove_generic_kpi_sections(filepath):
    """Remove generic KPI and Validation Checklist sections."""
    with open(filepath, 'r') as f:
        lines = f.read().split('\n')

    original_count = len(lines)
    lines_to_remove = set()
    removed_desc = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Remove generic KPI section
        if line == GENERIC_KPI_MARKER:
            end = find_section_end(lines, i)
            # Verify it's the generic one by checking for KPI-001
            section_text = '\n'.join(lines[i:end])
            if 'KPI-001' in section_text and 'COMPLETION-RATE' in section_text:
                for j in range(i, end):
                    lines_to_remove.add(j)
                removed_desc.append(f'Generic KPIs L{i+1}-{end}')
                i = end
                continue

        # Remove generic Validation Checklist
        if line == GENERIC_VALIDATION_MARKER:
            end = find_section_end(lines, i)
            for j in range(i, end):
                lines_to_remove.add(j)
            removed_desc.append(f'Validation Checklist L{i+1}-{end}')
            i = end
            continue

        # Remove standalone generic Quality Metrics header (with parenthetical)
        if line == GENERIC_QM_HEADER:
            end = find_section_end(lines, i)
            section_text = '\n'.join(lines[i:end])
            # Only remove if it's followed by generic KPI content or is empty
            if 'KPI-001' in section_text or 'COMPLETION-RATE' in section_text or len(lines[i:end]) <= 2:
                for j in range(i, end):
                    lines_to_remove.add(j)
                removed_desc.append(f'Generic QM header L{i+1}-{end}')
                i = end
                continue

        i += 1

    if not lines_to_remove:
        return False, "No generic KPI sections found"

    new_lines = [l for idx, l in enumerate(lines) if idx not in lines_to_remove]

    # Collapse multiple blank lines
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
    # Category B: scenarios with BOTH domain and generic KPIs
    category_b = [
        'automate-test', 'backup-data', 'implement-cicd', 'integrate-api',
        'manage-change', 'manage-config', 'manage-dependencies', 'manage-knowledge',
        'manage-tech-debt', 'migrate-environment', 'optimize-performance',
        'performance-testing', 'plan-capacity', 'plan-disaster-recovery',
        'plan-rollback', 'prepare-release', 'review-code', 'review-design',
        'review-incident', 'setup-infra',
    ]

    # Also include Category C (generic only) for removal - they need domain KPIs added later
    category_c = ['audit-security', 'manage-secrets', 'migrate-data', 'respond-incident']

    all_targets = category_b + category_c

    fixed = 0
    for name in all_targets:
        filepath = SCENARIOS_DIR / name / 'SCENARIO.md'
        if not filepath.exists():
            print(f"⏭️  {name}: file not found")
            continue
        try:
            was_fixed, msg = remove_generic_kpi_sections(filepath)
            if was_fixed:
                # Verify domain KPIs still exist
                content = open(filepath).read()
                has_domain = bool(re.search(r'(AUTO-COVER|FLAKY-RATE|INTEGRATION-PASS|CONFIG-VALID|SECRETS-LEAK|DEBT-VISIBILITY|KNOWLEDGE-INDEX|SLO-ACHIEVE|IAC-COVERAGE|LEAD-TIME|CHECKLIST-COMPLETE|BACKUP-SUCCESS|MIGRATION-SUCCESS|VULN-DETECTION|ROLLBACK-TESTED|RTO-COMPLY|CHANGE-SUCCESS|DEFECT-DETECTION|ISSUE-DETECTION|POSTMORTEM-COMPLETION|IMPROVEMENT-GAIN|FORECAST-ACCURACY)', content))
                has_generic_left = 'KPI-001' in content and 'COMPLETION-RATE' in content
                status = '✅' if not has_generic_left else '⚠️ generic remains'
                print(f"{status} {name}: {msg}")
                fixed += 1
            else:
                print(f"⏭️  {name}: {msg}")
        except Exception as e:
            print(f"❌ {name}: ERROR - {e}")

    print(f"\nFixed: {fixed}/{len(all_targets)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
