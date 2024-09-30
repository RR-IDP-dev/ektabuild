#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#  Copyright (c) 2023 Rajesh Radhakrishnan
#
#  This file is part of the Ektabuild project, which is licensed under the MIT License.
#  See the LICENSE file in the project root for more information.
# -----------------------------------------------------------------------------

import sys
from ektabuild.cli import parse_args
from ektabuild.orchestrator import Orchestrator

def main():
    """
    The main entry point of the Ektabuild application.

    This function parses command-line arguments, initializes the orchestrator,
    and runs the deployment workflow.
    """
    try:
        # Parse command-line arguments
        args = parse_args()

        # Initialize the orchestrator with the parsed arguments
        orchestrator = Orchestrator(args)

        # Execute the main workflow
        orchestrator.run()

    except Exception as e:
        # Handle exceptions and provide user-friendly error messages
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
