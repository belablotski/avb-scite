"""
Configure tools_pack
"""

import sys, os, os.path
import avb_tools.settings

TOOLS_ROOT = os.path.split(sys.argv[0])[0]
TEMP_DIR = os.path.join(TOOLS_ROOT, "temp")

if avb_tools.settings.ALLOW_EXTERNAL_CONFIGURATION:
    avb_tools.settings.TOOLS_ROOT = TOOLS_ROOT
    avb_tools.settings.TEMP_DIR = TEMP_DIR

def init():
    if not TOOLS_ROOT in sys.path:
        sys.path.append(TOOLS_ROOT)
        print(sys.path)
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

init()