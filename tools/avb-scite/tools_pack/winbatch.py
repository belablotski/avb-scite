"""
Windows batch-files launcer.
"""

import avb_tools_conf
import io, sys, os, os.path
from avb_tools.core.basetools import TempFileTool
from avb_tools.core.exceptions import EmptyInputException
from avb_tools.cmd.winbatch import CmdWinBatchTool

if __name__ == '__main__':
    print(sys.argv)
    exit()

    x = sys.stdin.read()
    if x == '@':
        raise EmptyInputException()
    tool = CmdWinBatchTool(io.StringIO(x[1:]), sys.stdout)
    tool.run()

