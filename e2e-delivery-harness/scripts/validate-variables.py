#!/usr/bin/env python3
"""
P2-1: Variable Schema Validation Script
Validates Prompt input variables against JSON Schema definitions and checks completeness.
"""
import json
import re
import sys
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

PROMPTS_DIR = Path("./prompts")
SCENARIOS_DIR = Path("./scenarios")


def extract_json_schema(content):
    """Extract JSON Schema block from prompt content."""
    match = re.search(r'```json\n(\{.*?\n\})\n```', content, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            return None
    return None


def extract_variables_table(content):
    """Extract variables from markdown table format."""
    variables = {}
    in_table = False
    for line in content.split('\n'):
        if '| Variable | Type | Required' in line:
            in_table = True
            continue
        if in_table:
            if line.strip().startswith('| `') and '|' in line:
                parts = [p.strip() for p in line.split('|') if p.strip()]
                if len(parts) >= 5:
                    var_name = parts[0].strip('`')
                    var_type = parts[1]
                    required = parts[2].lower() == 'true'
                    default = parts[3] if parts[3] != '-' else None
                    validation = parts[4] if len(parts) > 4 else ''
                    description = parts[5] if len(parts) > 5 else ''
                    variables[var_name] = {
                        'type': var_type,
                        'required': required,
                        'default': default,
                        'validation': validation,
                        'description': description
                    }
            elif line.strip() == '' or line.strip().startswith('##'):
                break
    return variables


def check_variable_compliance(prompt_path):
    """Check a single prompt file for variable schema compliance."""
    with open(prompt_path, 'r') as f:
        content = f.read()

    issues = []
    warnings = []

    # Check 1: Has Input Variables section?
    if '## Input Variables' not in content and '## 输入变量' not in content:
        issues.append("MISSING: No '## Input Variables' section found")
        return issues, warnings, {}

    # Check 2: Extract variables from table
    variables = extract_variables_table(content)
    if not variables:
        issues.append("MISSING: No variables table found (expected format: | Variable | Type | Required |...)")
        return issues, warnings, {}

    # Check 3: Has JSON Schema?
    schema = extract_json_schema(content)
    if not schema:
        warnings.append("WARN: No JSON Schema block found (recommended for machine validation)")

    # Check 4: Required variables have no defaults
    for name, var in variables.items():
        if var['required'] and var['default']:
            warnings.append(f"WARN: Variable '{name}' is required but has a default value ({var['default']})")
        if var['required'] and not var['validation']:
            warnings.append(f"WARN: Required variable '{name}' has no validation rule")

    # Check 5: Schema consistency (if schema exists)
    if schema:
        schema_props = schema.get('properties', {})
        schema_required = schema.get('required', [])
        for name, var in variables.items():
            if name not in schema_props and name != 'Variable':  # skip header
                warnings.append(f"MISMATCH: Variable '{name}' in table but not in JSON Schema")
        for name in schema_required:
            if name not in variables:
                warnings.append(f"MISMATCH: '{name}' required in Schema but not in variables table")

    return issues, warnings, variables


def validate_values(variables, values_file):
    """Validate provided values against variable definitions."""
    if not HAS_YAML:
        print("⚠️  PyYAML not installed. Skipping value validation. Install with: pip install pyyaml")
        return []

    with open(values_file, 'r') as f:
        values = yaml.safe_load(f) or {}

    results = []
    for name, var in variables.items():
        if var['required'] and name not in values:
            results.append({
                'variable': name,
                'status': 'FAIL',
                'reason': f"Required variable '{name}' is missing"
            })
        elif name in values:
            val = values[name]
            # Type checking
            expected_type = var['type']
            type_ok = True
            if expected_type == 'integer' and not isinstance(val, int):
                type_ok = False
            elif expected_type == 'number' and not isinstance(val, (int, float)):
                type_ok = False
            elif expected_type == 'boolean' and not isinstance(val, bool):
                type_ok = False
            elif expected_type == 'array' and not isinstance(val, list):
                type_ok = False
            elif expected_type == 'object' and not isinstance(val, dict):
                type_ok = False

            if type_ok:
                results.append({'variable': name, 'status': 'PASS', 'value': str(val)[:80]})
            else:
                results.append({
                    'variable': name,
                    'status': 'FAIL',
                    'reason': f"Type mismatch: expected {expected_type}, got {type(val).__name__}"
                })
        else:
            results.append({'variable': name, 'status': 'SKIP', 'reason': 'Optional, not provided'})

    return results


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Validate Prompt variable schemas')
    parser.add_argument('--scenario', type=str, help='Scenario name to validate')
    parser.add_argument('--variables', type=str, help='YAML file with variable values to validate')
    parser.add_argument('--all', action='store_true', help='Check all scenarios')
    args = parser.parse_args()

    if args.all:
        prompt_files = sorted(PROMPTS_DIR.glob("*.prompt.md"))
        total_issues = 0
        total_warnings = 0
        for pf in prompt_files:
            name = pf.stem.replace('.prompt', '')
            issues, warnings, variables = check_variable_compliance(pf)
            status = '✅' if not issues else '❌'
            print(f"{status} {name}: {len(variables)} vars, {len(issues)} issues, {len(warnings)} warnings")
            total_issues += len(issues)
            total_warnings += len(warnings)
        print(f"\nTotal: {len(prompt_files)} prompts, {total_issues} issues, {total_warnings} warnings")
    elif args.scenario:
        pf = PROMPTS_DIR / f"{args.scenario}.prompt.md"
        if not pf.exists():
            print(f"❌ Prompt file not found: {pf}")
            return 1
        issues, warnings, variables = check_variable_compliance(pf)
        print(f"=== {args.scenario} Variables ===")
        print(f"Count: {len(variables)}")
        for name, var in variables.items():
            req = 'REQUIRED' if var['required'] else 'optional'
            print(f"  {req:8s} {var['type']:10s} {name}: {var['description'][:60]}")
        if issues:
            print(f"\n❌ Issues ({len(issues)}):")
            for i in issues:
                print(f"  - {i}")
        if warnings:
            print(f"\n⚠️  Warnings ({len(warnings)}):")
            for w in warnings:
                print(f"  - {w}")

        if args.variables and variables:
            print(f"\n=== Value Validation ===")
            results = validate_values(variables, args.variables)
            for r in results:
                icon = '✅' if r['status'] == 'PASS' else ('❌' if r['status'] == 'FAIL' else '⏭️')
                print(f"  {icon} {r['variable']}: {r.get('reason', r.get('value', ''))}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
