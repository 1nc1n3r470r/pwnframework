"""
this is a small framework designed to help in the exploitation of various flaws
please only use against your own infrastructure
"""

import sys

if sys.version_info < (3, 10):
    print("Synapse requires Python 3.10 or above.")
    sys.exit(1)