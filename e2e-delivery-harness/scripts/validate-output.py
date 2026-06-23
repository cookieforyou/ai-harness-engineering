#!/usr/bin/env python3
"""
P2-3: Output Validation Automation Script
Validates AI agent output against scenario-specific quality checklists.
Supports automatic scoring based on evaluations/ regression checklists.
"""
import re
import sys
import json
from pathlib import Path
from datetime import datetime

SCENARIOS_DIR = Path("./scenarios")
EVALUATIONS_DIR = Path("./evaluations")


def load_checklist(checklist_path):
    """Load a checklist file and extract check items."""
    with open(checklist_path, 'r') as f:
        content = f.read()

    items = []
    # Extract checkbox items: - [ ] or - [x] or - [PASS] etc
    for line in content.split('\n'):
        match = re.match(r'^- \[([ xX])\]\s+(.+)$', line)
        if match:
            items.append({
                'text': match.group(2).strip(),
                'expected': 'checked',  # all items should be checked
                'checked': match.group(1) in ('x', 'X')
            })

        # Extract PASS/PARTIAL/FAIL/NA items
        match_pf = re.match(r'^\|\s*([A-Z_][A-Z_0-9-]*)\s*\|(.+?)\|', line)
        if match_pf:
            items.append({
                'id': match_pf.group(1).strip(),
                'text': match_pf.group(2).strip(),
                'type': 'metric',
                'expected': 'PASS'
            })

    return items


def validate_output(output_file, checklist_name=None):
    """Validate an output file against checklists."""
    with open(output_file, 'r') as f:
        content = f.read()

    results = {
        'file': output_file,
        'timestamp': datetime.now().isoformat(),
        'checks': [],
        'summary': {'pass': 0, 'fail': 0, 'warn': 0, 'total': 0}
    }

    # Auto-detect which checks to run based on content
    checks_to_run = []

    # Completeness: Check for expected sections
    sections_found = len(re.findall(r'^##\s+.+$', content, re.MULTILINE))
    checks_to_run.append({
        'check': 'COMPLETENESS',
        'criterion': 'Has at least 3 major sections',
        'result': 'PASS' if sections_found >= 3 else 'FAIL',
        'detail': f'Found {sections_found} sections'
    })

    # Structure: Check for YAML/JSON blocks
    yaml_blocks = len(re.findall(r'```yaml', content))
    json_blocks = len(re.findall(r'```json', content))
    checks_to_run.append({
        'check': 'STRUCTURE',
        'criterion': 'Has machine-readable blocks (YAML/JSON)',
        'result': 'PASS' if (yaml_blocks + json_blocks) >= 1 else 'WARN',
        'detail': f'{yaml_blocks} YAML + {json_blocks} JSON blocks'
    })

    # Traceability: Check for IDs
    dc_ids = len(re.findall(r'DC-\d{3}', content))
    risk_ids = len(re.findall(r'RISK-\d{3}', content))
    checks_to_run.append({
        'check': 'TRACEABILITY',
        'criterion': 'Has decision/risk ID references',
        'result': 'PASS' if (dc_ids + risk_ids) >= 1 else 'WARN',
        'detail': f'{dc_ids} DC-* + {risk_ids} RISK-* references'
    })

    # Quantifiability: Check for numeric metrics
    metrics = len(re.findall(r'[≥≤><]\s*\d+\.?\d*%?', content))
    checks_to_run.append({
        'check': 'QUANTIFIABLE',
        'criterion': 'Has quantifiable metrics with thresholds',
        'result': 'PASS' if metrics >= 3 else 'WARN',
        'detail': f'{metrics} metric references found'
    })

    # Handover: Check for handover YAML
    has_handover = bool(re.search(r'handover:|handoff:', content, re.IGNORECASE))
    checks_to_run.append({
        'check': 'HANDOVER',
        'criterion': 'Has handover/handoff section',
        'result': 'PASS' if has_handover else 'FAIL',
        'detail': 'Handover section ' + ('found' if has_handover else 'missing')
    })

    # Actionability: Check for checkboxes or action items
    action_items = len(re.findall(r'^- \[[ x]\]', content))
    checks_to_run.append({
        'check': 'ACTIONABLE',
        'criterion': 'Has actionable checklist items',
        'result': 'PASS' if action_items >= 3 else 'WARN',
        'detail': f'{action_items} checkbox items found'
    })

    results['checks'] = checks_to_run
    for c in checks_to_run:
        results['summary']['total'] += 1
        if c['result'] == 'PASS':
            results['summary']['pass'] += 1
        elif c['result'] == 'FAIL':
            results['summary']['fail'] += 1
        else:
            results['summary']['warn'] += 1

    # Calculate score
    total = results['summary']['total']
    passed = results['summary']['pass']
    warn = results['summary']['warn']
    results['summary']['score'] = round((passed + warn * 0.5) / total * 100, 1) if total > 0 else 0
    results['summary']['grade'] = (
        'A' if results['summary']['score'] >= 90 else
        'B' if results['summary']['score'] >= 80 else
        'C' if results['summary']['score'] >= 70 else
        'D' if results['summary']['score'] >= 60 else 'F'
    )

    return results


def validate_scenario_outputs(scenario_name):
    """Validate all outputs for a given scenario."""
    scenario_dir = SCENARIOS_DIR / scenario_name
    if not scenario_dir.exists():
        print(f"❌ Scenario not found: {scenario_name}")
        return None

    # Find output files referenced in scenario
    results = []
    scenario_file = scenario_dir / 'SCENARIO.md'
    if scenario_file.exists():
        result = validate_output(str(scenario_file))
        result['label'] = f'{scenario_name}/SCENARIO.md'
        results.append(result)

    return results


def format_results(results):
    """Format validation results for display."""
    output = []
    output.append("=" * 60)
    output.append("  Output Validation Report")
    output.append("=" * 60)

    for r in (results or []):
        if 'label' in r:
            output.append(f"\n📄 {r['label']}")
        s = r['summary']
        output.append(f"   Score: {s['score']}% (Grade: {s['grade']})")
        output.append(f"   PASS={s['pass']} WARN={s['warn']} FAIL={s['fail']} TOTAL={s['total']}")
        output.append(f"   Timestamp: {r['timestamp']}")
        output.append("")
        for c in r['checks']:
            icon = '✅' if c['result'] == 'PASS' else ('❌' if c['result'] == 'FAIL' else '⚠️')
            output.append(f"   {icon} {c['check']}: {c['detail']}")

    return '\n'.join(output)


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Validate AI agent output quality')
    parser.add_argument('--file', type=str, help='Output file to validate')
    parser.add_argument('--scenario', type=str, help='Scenario name (validates all scenario outputs)')
    parser.add_argument('--checklist', type=str, help='Specific evaluation checklist to use')
    parser.add_argument('--json', action='store_true', help='Output results as JSON')
    args = parser.parse_args()

    results = []

    if args.file:
        results.append(validate_output(args.file))
        if 'label' not in results[-1]:
            results[-1]['label'] = args.file

    if args.scenario:
        scenario_results = validate_scenario_outputs(args.scenario)
        if scenario_results:
            results.extend(scenario_results)

    if not results:
        # Default: validate all scenario outputs
        for sf in sorted(SCENARIOS_DIR.glob("*/SCENARIO.md")):
            results.append(validate_output(str(sf)))
            results[-1]['label'] = f"{sf.parent.name}/SCENARIO.md"

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(format_results(results))

    # Return overall success/failure
    all_pass = all(r['summary']['fail'] == 0 for r in results)
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
