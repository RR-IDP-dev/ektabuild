
# -----------------------------------------------------------------------------
#  Copyright (c) 2023 Rajesh Radhakrishnan
#
#  This file is part of the Ektabuild project, which is licensed under the MIT License.
#  See the LICENSE file in the project root for more information.
# -----------------------------------------------------------------------------

import pytest
import sys
from ektabuild.cli import parse_args
from ektabuild.main import main

def test_parse_args_with_required_arguments():
    args = parse_args(['--config', 'config.yaml'])
    assert args.config == 'config.yaml'
    assert args.workspace is None

def test_parse_args_with_all_arguments():
    args = parse_args(['--config', 'config.yaml', '--workspace', 'my_workspace'])
    assert args.config == 'config.yaml'
    assert args.workspace == 'my_workspace'

def test_parse_args_missing_required_arguments():
    with pytest.raises(SystemExit) as exc_info:
        parse_args([])
    assert exc_info.value.code == 2  # argparse exits with code 2 on error

# def test_main_with_valid_arguments(monkeypatch, capsys):
#     test_args = ['ektabuild', '--config', 'config.yaml']
#     monkeypatch.setattr(sys, 'argv', test_args)

#     # Assuming main() in main.py
#     main()

#     captured = capsys.readouterr()
#     assert "Loaded configuration from config.yaml" in captured.out

# def test_main_missing_required_arguments(monkeypatch, capsys):
#     test_args = ['ektabuild']
#     monkeypatch.setattr(sys, 'argv', test_args)

#     with pytest.raises(SystemExit) as exc_info:
#         main()
#     assert exc_info.value.code == 2  # argparse exits with code 2 on error

#     captured = capsys.readouterr()
#     assert "usage:" in captured.err  # argparse outputs usage info on error
