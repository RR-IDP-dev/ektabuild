# -----------------------------------------------------------------------------
#  Copyright (c) 2024 Rajesh Radhakrishnan
#
#  This file is part of the Ektabuild project, which is licensed under the MIT License.
#  See the LICENSE file in the project root for more information.
# -----------------------------------------------------------------------------

import argparse

def parse_args(args=None):
    parser = argparse.ArgumentParser(description="Ektabuild - Build complex application stacks on private and/or public cloud.")
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to the application stack YAML file."
    )
    parser.add_argument(
        "--workspace",
        type=str,
        default=None,
        help="Optional name for the workspace directory."
    )
    # Add more arguments as needed
    return parser.parse_args(args)