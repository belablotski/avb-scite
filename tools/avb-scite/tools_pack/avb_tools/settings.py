"""
Settings for avb_tools
"""

# Allow settings to be configured externally (from avb_tools_conf.py)
ALLOW_EXTERNAL_CONFIGURATION = True

# Root directory for tools pack
TOOLS_ROOT = "will be configured from avb_tools_conf.py"

# Directory to save temporary files.
# This location should be secure enough.
# It's possible to automate this with tempfile.mkdtemp()
# http://docs.python.org/library/tempfile.html#tempfile.mkdtemp
# Directory should exist.
TEMP_DIR = "will be configured from avb_tools_conf.py"
