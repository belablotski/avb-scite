"""Wrapper for Oracle SQL*Plus"""

from avb_tools.core.basetools import TempFileTool

class CmdSqlplusTool(ToolBase):
	"""
	Tool for Oracle SQL*Plus.
	"""
	def __init__(self, input_stream, output_stream, prolog="", epilog="", encoding="utf-8"):
		super(CmdSqlplusTool, self).__init__(input_stream, output_stream, prolog, epilog, encoding)
		

	def _prepare_popen(self):
		result = Popen(["sqlplus.exe", "-S", "system/avb1-pass@avb1", "@"+self.tmp_file], stdout=PIPE)
		return result
