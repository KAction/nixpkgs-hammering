#!/usr/bin/env python3

import os
import subprocess

script_dir = os.path.dirname(os.path.realpath(__file__))


def test_variant(rule, variant):
    attr_path=f'{rule}.{variant}'
    test_build = subprocess.run(
        [
            os.path.join(script_dir, 'tools/nixpkgs-hammer'),
            '-f', './tests',
            attr_path
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    if test_build.returncode != 0:
        print('\t\terror building the test')
    elif f'explanations/{rule}.md'.encode('utf-8') not in test_build.stdout:
        print('\t\terror matching the rule')
    else:
        print('\t\tok')


def test_rule(rule, variants):
    print(f'Testing {rule}')

    for variant in variants:
        print(f'\t{variant}')
        test_variant(rule, variant)


if __name__ == '__main__':
    test_rule(
        'build-tools-in-build-inputs',
        [
            'cmake',
            'meson',
            'ninja',
            'pkg-config',
        ],
    )
