"""Wrapper for Oracle SQL*Plus"""

from avb_tools.core.basetools import ProcessRunnerTool

class CmdWinBatchTool(ProcessRunnerTool):
	"""
	Tool for execute Windows Batch script.
	"""
	def __init__(self, input_stream, output_stream, prolog="", epilog="", encoding="utf-8"):
		super(CmdWinBatchTool, self).__init__(input_stream, output_stream, prolog, epilog, encoding)
		

	def _prepare_popen(self):
		result = Popen(["sqlplus.exe", "-S", "system/avb1-pass@avb1", "@"+self.tmp_file], stdout=PIPE)
		return result
