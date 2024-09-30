# -----------------------------------------------------------------------------
#  Copyright (c) 2024 Rajesh Radhakrishnan
#
#  This file is part of the Ektabuild project, which is licensed under the MIT License.
#  See the LICENSE file in the project root for more information.
# -----------------------------------------------------------------------------

class Orchestrator:
    def __init__(self, parser, cloud_providers=None, environment=None):
        self.parser = parser
        self.cloud_providers = cloud_providers
        self.environment = environment
    def run(args=None):
        """"""