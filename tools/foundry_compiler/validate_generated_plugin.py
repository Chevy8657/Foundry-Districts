#!/usr/bin/env python3
"""
Validate a generated plugin skeleton produced by the Foundry compiler.

Checks (architecture-only):
- manifest.yaml exists and contains constitution_refs with business and engineering refs
- compliance-proof-template.json exists and contains referenced_constitution_revisions with business and engineering refs
- registration-intent.json exists and contains constitution_refs and status == PENDING_KERNEL_REGISTRATION

This script performs structural checks only and contains no business logic.
"""

import json
import os
import sys


def load_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"ERROR: Failed to load JSON from {path}: {e}")
        return None


def load_yaml_like(path):
    # minimal parser for manifest.yaml produced by the compiler (simple key: value, lists)
    data = {}
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        lines = [l.rstrip('\n') for l in f]
    key = None
    for line in lines:
        if not line.strip():
            continue
        if line.startswith('  - '):
            if key is None:
                continue
            data.setdefault(key, [])
            data[key].append(line[4:].strip())
        elif line.startswith('  '):
            # simple dict entry under a parent
            parts = line.strip().split(':', 1)
            if len(parts) == 2 and key:
                subk = parts[0].strip()
                subv = parts[1].strip()
                data.setdefault(key, {})
                data[key][subk] = subv
        else:
            parts = line.split(':', 1)
            if len(parts) == 2:
                key = parts[0].strip()
                val = parts[1].strip()
                if val == '':
                    # parent for upcoming list or map
                    data[key] = {}
                else:
                    data[key] = val
    return data


def validate(plugin_dir):
    results = []
    manifest_path = os.path.join(plugin_dir, 'manifest.yaml')
    proof_path = os.path.join(plugin_dir, 'compliance-proof-template.json')
    intent_path = os.path.join(plugin_dir, 'registration-intent.json')

    # manifest
    if not os.path.exists(manifest_path):
        results.append(('manifest_exists', False, 'manifest.yaml missing'))
    else:
        manifest = load_yaml_like(manifest_path)
        if manifest is None:
            results.append(('manifest_parse', False, 'manifest.yaml could not be parsed'))
        else:
            refs = manifest.get('constitution_refs') or manifest.get('constitution_refs:') or manifest.get('constitution_refs')
            # our simple parser returns dict under 'constitution_refs' as dict of strings
            if not refs or not isinstance(refs, dict):
                results.append(('manifest_const_refs', False, 'constitution_refs missing or invalid in manifest.yaml'))
            else:
                if 'business_constitution_ref' in refs and 'engineering_constitution_ref' in refs:
                    results.append(('manifest_const_refs', True, 'both constitution refs present in manifest.yaml'))
                else:
                    results.append(('manifest_const_refs', False, 'one or more constitution refs missing in manifest.yaml'))

    # compliance proof
    if not os.path.exists(proof_path):
        results.append(('proof_exists', False, 'compliance-proof-template.json missing'))
    else:
        proof = load_json(proof_path)
        if proof is None:
            results.append(('proof_parse', False, 'compliance-proof-template.json could not be parsed'))
        else:
            refs = proof.get('referenced_constitution_revisions')
            if refs and 'business_constitution_ref' in refs and 'engineering_constitution_ref' in refs:
                results.append(('proof_const_refs', True, 'both constitution refs present in compliance-proof-template.json'))
            else:
                results.append(('proof_const_refs', False, 'one or more constitution refs missing in compliance-proof-template.json'))

    # registration intent
    if not os.path.exists(intent_path):
        results.append(('intent_exists', False, 'registration-intent.json missing'))
    else:
        intent = load_json(intent_path)
        if intent is None:
            results.append(('intent_parse', False, 'registration-intent.json could not be parsed'))
        else:
            refs = intent.get('constitution_refs')
            status = intent.get('status')
            if not refs or 'business_constitution_ref' not in refs or 'engineering_constitution_ref' not in refs:
                results.append(('intent_const_refs', False, 'constitution_refs missing or incomplete in registration-intent.json'))
            else:
                results.append(('intent_const_refs', True, 'both constitution refs present in registration-intent.json'))
            if status == 'PENDING_KERNEL_REGISTRATION':
                results.append(('intent_status', True, 'registration-intent.json status is PENDING_KERNEL_REGISTRATION'))
            else:
                results.append(('intent_status', False, f"registration-intent.json status is not PENDING_KERNEL_REGISTRATION: {status}"))

    # Summary PASS if all checks True
    all_pass = all(r[1] for r in results)
    return all_pass, results


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: validate_generated_plugin.py <path-to-generated-plugin-dir>')
        sys.exit(1)
    plugin_dir = sys.argv[1]
    ok, res = validate(plugin_dir)
    for k, passed, msg in res:
        print(f"{k}: {'PASS' if passed else 'FAIL'} - {msg}")
    print('\nOverall:', 'PASS' if ok else 'FAIL')
    sys.exit(0 if ok else 2)
