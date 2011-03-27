"""
Oracle SQL*Plus launcher.
"""

import avb_tools_conf
import io, sys, os, os.path
from avb_tools.core.basetools import TempFileTool

#temp_file_tool = TempFileTool(io.StringIO("select * from dual;"), sys.stdout)
#temp_file_tool.run()

class SqlPlusTool(TempFileTool):
    def __init__(self):
        x = sys.stdin.read()
        super(SqlPlusTool, self).__init__(io.StringIO(x), sys.stdout)

#tool = SqlPlusTool()
#tool.run()

print("xxx")
x = sys.stdin.read()
print(x)

