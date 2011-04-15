"""
Oracle SQL*Plus launcher.
"""

import avb_tools_conf
import io, sys, os, os.path
from avb_tools.core.basetools import TempFileTool
from avb_tools.core.exceptions import EmptyInputException

class SqlPlusTool(TempFileTool):
    def __init__(self):
        x = sys.stdin.read()
        if x == '@':
            raise EmptyInputException()
        x = x.strip()
        if len(x) == 0:
            raise EmptyInputException()
        if x[-1] != ';':
            x += ';'
        x = x.replace(chr(10), ' ').replace(chr(13), ' ')
        super(SqlPlusTool, self).__init__(io.StringIO(x[1:]), sys.stdout)

tool = SqlPlusTool()
tool.run()
