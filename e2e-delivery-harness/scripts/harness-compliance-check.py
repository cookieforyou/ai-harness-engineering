#!/usr/bin/env python3
"""
P3-5: Harness Compliance Check Script
Comprehensive compliance monitoring that checks content quality (not just existence).
Validates: structure, content depth, cross-references, KPI alignment, and handoff completeness.
Generates a compliance scorecard with per-asset grades.
"""
import re
import sys
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent

# Minimum content thresholds for each asset type
THRESHOLDS = {
    'scenario': {'min_lines': 150, 'min_sections': 6, 'min_dc': 3, 'min_kpi': 3},
    'agent': {'min_lines': 150, 'min_sections': 6, 'min_input_fields': 4, 'min_output_fields': 3},
    'prompt': {'min_lines': 150, 'min_sections': 6, 'min_variables': 3, 'min_error_scenarios': 2},
    'instruction': {'min_lines': 80, 'min_sections': 5, 'min_steps': 3},
    'skill': {'min_lines': 100, 'min_sections': 5, 'min_pitfalls': 3},
    'standard': {'min_lines': 80, 'min_sections': 4},
    'evaluation': {'min_lines': 50, 'min_sections': 3, 'min_check_items': 8},
    'template': {'min_lines': 60, 'min_sections': 4},
}


class ComplianceChecker:
    def __init__(self):
        self.results = {'categories': {}, 'overall': {}, 'timestamp': datetime.now().isoformat()}
        self.total_checks = 0
        self.total_pass = 0
        self.total_warn = 0
        self.total_fail = 0

    def check_file(self, filepath, asset_type):
        """Run all compliance checks on a single file."""
        if not filepath.exists():
            return {'status': 'FAIL', 'reason': 'File not found'}

        with open(filepath, 'r') as f:
            content = f.read()
            lines = content.split('\n')

        checks = []

        # 1. Structural checks
        checks.append(self._check_yaml_frontmatter(lines, filepath))
        checks.append(self._check_min_lines(lines, asset_type))
        checks.append(self._check_sections(lines, asset_type))

        # 2. Content quality checks
        checks.append(self._check_no_placeholders(content))
        if asset_type == 'template':
            checks.append(self._check_template_field_coverage(content))
            checks.append(self._check_template_cross_references(content, filepath))
        else:
            checks.append(self._check_quantifiable_metrics(content))
            checks.append(self._check_cross_references(content, filepath))

        # 3. Asset-specific checks
        if asset_type == 'scenario':
            checks.append(self._check_scenario_specific(content, lines))
        elif asset_type == 'agent':
            checks.append(self._check_agent_specific(content, lines))
        elif asset_type == 'prompt':
            checks.append(self._check_prompt_specific(content, lines))
        elif asset_type == 'instruction':
            checks.append(self._check_instruction_specific(content))
        elif asset_type == 'skill':
            checks.append(self._check_skill_specific(content))
        elif asset_type == 'standard':
            checks.append(self._check_standard_specific(content))
        elif asset_type == 'evaluation':
            checks.append(self._check_evaluation_specific(content))
        elif asset_type == 'template':
            checks.append(self._check_template_specific(content))

        return self._summarize(checks)

    def _check_yaml_frontmatter(self, lines, filepath):
        """Check YAML frontmatter completeness."""
        has_frontmatter = lines[0].strip() == '---'
        has_closing = False
        required_fields = ['name', 'description', 'version', 'type', 'status']
        found = {f: False for f in required_fields}

        for i, line in enumerate(lines[1:30], 1):
            if line.strip() == '---':
                has_closing = True
                break
            for field in required_fields:
                if line.startswith(f'{field}:'):
                    found[field] = True

        missing = [f for f, v in found.items() if not v]
        if not has_frontmatter or not has_closing:
            return {'check': 'YAML_FRONTMATTER', 'status': 'FAIL', 'detail': 'Missing or malformed YAML frontmatter'}
        elif missing:
            return {'check': 'YAML_FRONTMATTER', 'status': 'WARN', 'detail': f'Missing fields: {missing}'}
        return {'check': 'YAML_FRONTMATTER', 'status': 'PASS', 'detail': 'Complete'}

    def _check_min_lines(self, lines, asset_type):
        threshold = THRESHOLDS.get(asset_type, {}).get('min_lines', 100)
        actual = len([l for l in lines if l.strip()])
        if actual < threshold * 0.5:
            return {'check': 'MIN_LINES', 'status': 'FAIL', 'detail': f'{actual} lines (minimum: {threshold})'}
        elif actual < threshold * 0.8:
            return {'check': 'MIN_LINES', 'status': 'WARN', 'detail': f'{actual} lines (target: {threshold})'}
        return {'check': 'MIN_LINES', 'status': 'PASS', 'detail': f'{actual} lines'}

    def _check_sections(self, lines, asset_type):
        threshold = THRESHOLDS.get(asset_type, {}).get('min_sections', 5)
        sections = len([l for l in lines if re.match(r'^##\s+\S', l)])
        if sections < threshold * 0.5:
            return {'check': 'SECTIONS', 'status': 'FAIL', 'detail': f'{sections} sections (minimum: {threshold})'}
        elif sections < threshold:
            return {'check': 'SECTIONS', 'status': 'WARN', 'detail': f'{sections} sections (target: {threshold})'}
        return {'check': 'SECTIONS', 'status': 'PASS', 'detail': f'{sections} sections'}

    def _check_no_placeholders(self, content):
        """Check for unfilled template placeholders."""
        patterns = [
            r'\[Trigger condition \d', r'\[Rule \d description\]',
            r'\[Next Agent\]', r'\[When to hand off\]', r'\[What data to pass\]',
            r'\[Core concept \d\]', r'\[Principle \d\]', r'### Pitfall \d: \[Name\]',
            r'\[List required tools', r'\[List environment prerequisites',
            r'\[List key configuration', r'\[Root cause\]', r'\[Steps to resolve\]',
            r'\[Description\]', r'\[Name\]',
        ]
        count = sum(1 for p in patterns if re.search(p, content))
        if count > 3:
            return {'check': 'NO_PLACEHOLDERS', 'status': 'FAIL', 'detail': f'{count} unfilled placeholders'}
        elif count > 0:
            return {'check': 'NO_PLACEHOLDERS', 'status': 'WARN', 'detail': f'{count} unfilled placeholders'}
        return {'check': 'NO_PLACEHOLDERS', 'status': 'PASS', 'detail': 'No placeholders'}

    def _check_quantifiable_metrics(self, content):
        """Check for quantifiable metrics (numbers with thresholds)."""
        metrics = len(re.findall(r'[≥≤>=<]\s*\d+\.?\d*\s*%?', content))
        if metrics < 2:
            return {'check': 'QUANTIFIABLE', 'status': 'WARN', 'detail': f'Only {metrics} metric references'}
        return {'check': 'QUANTIFIABLE', 'status': 'PASS', 'detail': f'{metrics} metric references'}

    def _check_cross_references(self, content, filepath):
        """Check for cross-references to related assets (supports both same-dir and ../ paths)."""
        refs = len(re.findall(r'\[.*?\]\((?:\.\./|[^)]+\.md\))', content))
        if refs < 2:
            return {'check': 'CROSS_REFS', 'status': 'WARN', 'detail': f'Only {refs} cross-references'}
        return {'check': 'CROSS_REFS', 'status': 'PASS', 'detail': f'{refs} cross-references'}

    def _check_scenario_specific(self, content, lines):
        dc_count = len(re.findall(r'DC-\d{3}', content))
        threshold = THRESHOLDS['scenario']['min_dc']
        if dc_count < threshold:
            return {'check': 'DECISION_CHECKPOINTS', 'status': 'WARN', 'detail': f'{dc_count} DC-* (target: {threshold})'}

        kpi_count = len(re.findall(r'\| KPI-00[1-5] \|', content)) + len(re.findall(r'\| `[A-Z][A-Z-]+` \| [≥≤]', content))
        if kpi_count < THRESHOLDS['scenario']['min_kpi']:
            return {'check': 'DOMAIN_KPIS', 'status': 'WARN', 'detail': f'{kpi_count} KPIs (target: {THRESHOLDS["scenario"]["min_kpi"]})'}

        has_handover = 'Handover Context Template' in content or 'handover:' in content.lower()
        if not has_handover:
            return {'check': 'HANDOVER_TEMPLATE', 'status': 'FAIL', 'detail': 'Missing Handover Context Template'}
        return {'check': 'SCENARIO_SPECIFIC', 'status': 'PASS', 'detail': f'DC={dc_count}, KPI={kpi_count}, Handover=OK'}

    def _check_agent_specific(self, content, lines):
        has_use_when = '## Use When' in content
        has_working_rules = '## Working Rules' in content
        has_handoff = '## Handoff' in content
        has_io_tables = '## Expected Input' in content and '## Expected Output' in content

        issues = []
        if not has_use_when: issues.append('Use When')
        if not has_working_rules: issues.append('Working Rules')
        if not has_handoff: issues.append('Handoff')
        if not has_io_tables: issues.append('I/O tables')

        if issues:
            return {'check': 'AGENT_SECTIONS', 'status': 'WARN', 'detail': f'Missing: {issues}'}
        return {'check': 'AGENT_SECTIONS', 'status': 'PASS', 'detail': 'All required sections present'}

    def _check_prompt_specific(self, content, lines):
        var_count = len(re.findall(r'^\| `\w+` \|', content, re.MULTILINE))
        err_count = len(re.findall(r'Error Scenario \d', content))

        issues = []
        if var_count < THRESHOLDS['prompt']['min_variables']:
            issues.append(f'Only {var_count} variables')
        if err_count < THRESHOLDS['prompt']['min_error_scenarios']:
            issues.append(f'Only {err_count} error scenarios')

        if issues:
            return {'check': 'PROMPT_SPECIFIC', 'status': 'WARN', 'detail': ', '.join(issues)}
        return {'check': 'PROMPT_SPECIFIC', 'status': 'PASS', 'detail': f'{var_count} vars, {err_count} error scenarios'}

    def _check_instruction_specific(self, content):
        has_commands = bool(re.search(r'```(bash|shell|sh|python|yaml|json)', content))
        has_steps = len(re.findall(r'Step \d', content)) >= THRESHOLDS['instruction']['min_steps']
        if not has_commands or not has_steps:
            return {'check': 'INSTRUCTION_SPECIFIC', 'status': 'WARN', 'detail': f'Commands={has_commands}, Steps={has_steps}'}
        return {'check': 'INSTRUCTION_SPECIFIC', 'status': 'PASS', 'detail': 'Has commands and steps'}

    def _check_skill_specific(self, content):
        pitfalls = len(re.findall(r'### Pitfall \d', content))
        if pitfalls < THRESHOLDS['skill']['min_pitfalls']:
            return {'check': 'SKILL_PITFALLS', 'status': 'WARN', 'detail': f'{pitfalls} pitfalls (target: {THRESHOLDS["skill"]["min_pitfalls"]})'}
        return {'check': 'SKILL_PITFALLS', 'status': 'PASS', 'detail': f'{pitfalls} pitfalls'}

    def _check_standard_specific(self, content):
        has_examples = bool(re.search(r'```(yaml|json|bash|markdown)', content))
        has_rules = len(re.findall(r'^\d+\.\s+\*\*', content, re.MULTILINE)) >= 3
        if not has_examples:
            return {'check': 'STANDARD_DEPTH', 'status': 'WARN', 'detail': 'No code/YAML examples'}
        return {'check': 'STANDARD_DEPTH', 'status': 'PASS', 'detail': f'Examples={"Yes" if has_examples else "No"}, Rules={has_rules}'}

    def _check_evaluation_specific(self, content):
        check_items = len(re.findall(r'^- \[[ x]\]', content, re.MULTILINE))
        if check_items < THRESHOLDS['evaluation']['min_check_items']:
            return {'check': 'EVAL_ITEMS', 'status': 'FAIL', 'detail': f'{check_items} check items (minimum: {THRESHOLDS["evaluation"]["min_check_items"]})'}
        return {'check': 'EVAL_ITEMS', 'status': 'PASS', 'detail': f'{check_items} check items'}

    def _check_template_specific(self, content):
        has_placeholders = bool(re.search(r'\{[\w_]+\}', content))
        has_structure = len(re.findall(r'^##\s+', content, re.MULTILINE)) >= 3
        if not has_placeholders:
            return {'check': 'TEMPLATE_DEPTH', 'status': 'WARN', 'detail': 'No field placeholders'}
        return {'check': 'TEMPLATE_DEPTH', 'status': 'PASS', 'detail': f'Structure={has_structure}'}

    def _check_template_field_coverage(self, content):
        """Template-specific: check for sufficient fillable field placeholders instead of quantifiable metrics."""
        field_count = len(re.findall(r'\{[\w_]+\}', content))
        if field_count < 3:
            return {'check': 'FIELD_COVERAGE', 'status': 'WARN', 'detail': f'Only {field_count} template fields (target: ≥3)'}
        return {'check': 'FIELD_COVERAGE', 'status': 'PASS', 'detail': f'{field_count} template fields'}

    def _check_template_cross_references(self, content, filepath):
        """Template-specific: lower cross-reference threshold (templates only need 1 ref to standard)."""
        refs = len(re.findall(r'\[.*?\]\((?:\.\./|[^)]+\.md\))', content))
        if refs < 1:
            return {'check': 'CROSS_REFS', 'status': 'WARN', 'detail': f'Only {refs} cross-references (target: ≥1)'}
        return {'check': 'CROSS_REFS', 'status': 'PASS', 'detail': f'{refs} cross-references'}

    def _summarize(self, checks):
        pass_count = sum(1 for c in checks if c['status'] == 'PASS')
        warn_count = sum(1 for c in checks if c['status'] == 'WARN')
        fail_count = sum(1 for c in checks if c['status'] == 'FAIL')
        total = len(checks)
        score = round((pass_count + warn_count * 0.5) / total * 100, 1) if total > 0 else 0

        self.total_checks += total
        self.total_pass += pass_count
        self.total_warn += warn_count
        self.total_fail += fail_count

        return {
            'checks': checks,
            'score': score,
            'grade': 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F',
            'summary': f'PASS={pass_count} WARN={warn_count} FAIL={fail_count}',
        }


def scan_category(checker, pattern, asset_type, label):
    """Scan all files matching a pattern in a category."""
    files = sorted(Path(ROOT) / p for p in [pattern] if Path(ROOT / pattern).exists())
    # Actually glob the pattern
    glob_pattern = str(Path(ROOT) / pattern)
    import glob as g
    matched = sorted(g.glob(glob_pattern))

    results = {}
    for fp in matched:
        if fp.endswith('README.md'):
            continue
        name = Path(fp).stem.replace('.template', '').replace('.instructions', '').replace('.prompt', '').replace('.agent', '').replace('.pipeline', '')
        results[name] = checker.check_file(Path(fp), asset_type)

    # Category summary
    scores = [r['score'] for r in results.values()]
    avg_score = round(sum(scores) / len(scores), 1) if scores else 0
    grade_dist = {}
    for r in results.values():
        g = r['grade']
        grade_dist[g] = grade_dist.get(g, 0) + 1

    checker.results['categories'][label] = {
        'count': len(results),
        'avg_score': avg_score,
        'grade_distribution': grade_dist,
        'files': {k: {'score': v['score'], 'grade': v['grade'], 'summary': v['summary']}
                   for k, v in results.items()}
    }
    return results


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Harness Compliance Check - content quality validation')
    parser.add_argument('--category', type=str, choices=['scenarios', 'agents', 'prompts', 'instructions', 'skills', 'standards', 'evaluations', 'templates'], help='Check specific category')
    parser.add_argument('--file', type=str, help='Check a specific file')
    parser.add_argument('--min-grade', type=str, default='C', help='Minimum acceptable grade (default: C)')
    parser.add_argument('--json', action='store_true', help='Output JSON report')
    parser.add_argument('--all', action='store_true', help='Check all categories')
    args = parser.parse_args()

    checker = ComplianceChecker()

    if args.file:
        fp = Path(args.file)
        asset_type = fp.parent.name if fp.parent.name != '.' else 'unknown'
        result = checker.check_file(fp, asset_type)
        print(f"\n📄 {fp.name}")
        print(f"   Score: {result['score']}% (Grade: {result['grade']})")
        print(f"   {result['summary']}")
        for c in result['checks']:
            icon = '✅' if c['status'] == 'PASS' else ('❌' if c['status'] == 'FAIL' else '⚠️')
            print(f"   {icon} {c['check']}: {c['detail']}")
        return 0 if result['grade'] <= args.min_grade else 1

    categories_to_scan = []
    if args.all or not args.category:
        categories_to_scan = [
            ('scenarios/*/SCENARIO.md', 'scenario', 'Scenarios'),
            ('agents/*.agent.md', 'agent', 'Agents'),
            ('prompts/*.prompt.md', 'prompt', 'Prompts'),
            ('instructions/*.instructions.md', 'instruction', 'Instructions'),
            ('skills/*/SKILL.md', 'skill', 'Skills'),
            ('standards/*.md', 'standard', 'Standards'),
            ('evaluations/*.md', 'evaluation', 'Evaluations'),
            ('templates/*.template.md', 'template', 'Templates'),
        ]
    else:
        mapping = {
            'scenarios': ('scenarios/*/SCENARIO.md', 'scenario', 'Scenarios'),
            'agents': ('agents/*.agent.md', 'agent', 'Agents'),
            'prompts': ('prompts/*.prompt.md', 'prompt', 'Prompts'),
            'instructions': ('instructions/*.instructions.md', 'instruction', 'Instructions'),
            'skills': ('skills/*/SKILL.md', 'skill', 'Skills'),
            'standards': ('standards/*.md', 'standard', 'Standards'),
            'evaluations': ('evaluations/*.md', 'evaluation', 'Evaluations'),
            'templates': ('templates/*.template.md', 'template', 'Templates'),
        }
        categories_to_scan = [mapping[args.category]]

    for pattern, asset_type, label in categories_to_scan:
        print(f"\n{'='*60}")
        print(f"  {label} Compliance Check")
        print(f"{'='*60}")
        results = scan_category(checker, pattern, asset_type, label)

        grade_icons = {'A': '🟢', 'B': '🔵', 'C': '🟡', 'D': '🟠', 'F': '🔴'}
        for name, r in sorted(results.items()):
            icon = grade_icons.get(r['grade'], '⚪')
            print(f"  {icon} {name:35s} {r['score']:5.1f}% {r['grade']}  {r['summary']}")

        cat = checker.results['categories'][label]
        print(f"\n  Average: {cat['avg_score']}% | Distribution: {cat['grade_distribution']}")

    # Overall summary
    if args.all or len(categories_to_scan) > 1:
        print(f"\n{'='*60}")
        print(f"  OVERALL COMPLIANCE REPORT")
        print(f"{'='*60}")
        print(f"  Total checks: {checker.total_checks}")
        print(f"  PASS: {checker.total_pass}  WARN: {checker.total_warn}  FAIL: {checker.total_fail}")
        overall_score = round((checker.total_pass + checker.total_warn * 0.5) / checker.total_checks * 100, 1) if checker.total_checks > 0 else 0
        overall_grade = 'A' if overall_score >= 90 else 'B' if overall_score >= 80 else 'C' if overall_score >= 70 else 'D' if overall_score >= 60 else 'F'
        print(f"  Overall Score: {overall_score}% (Grade: {overall_grade})")

        if args.json:
            print(json.dumps(checker.results, indent=2, ensure_ascii=False))

        # Exit with failure if below minimum grade
        grade_order = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'F': 1}
        if grade_order.get(overall_grade, 0) < grade_order.get(args.min_grade, 3):
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
