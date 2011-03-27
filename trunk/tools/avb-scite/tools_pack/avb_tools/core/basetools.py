"""Core classes for making tools."""

import os.path
import datetime
import random
from subprocess import *
from avb_tools.settings import TEMP_DIR

class ToolBase(object):
	def __init__(self, input_stream, output_stream):
		self.input_stream = input_stream
		self.output_stream = output_stream
		
	def run(self):
		raise NotImplementedError("Method is't implemented.")


class EchoTool(ToolBase):
	def __init__(self, input_stream, output_stream):
		pass
		
	def run(self):
		raise NotImplementedError("Method is't implemented.")


class TempFileTool(ToolBase):
	"""
	Work with command-line tool which doesn't support piped input.	
	All content from input_stream will be saved to temp file, possible
	with prolog and epilog. After that certain command-line tool will be 
	started to process created temp file.
	"""
	def __gen_temp_file_path(self):
		now = datetime.datetime.now()
		rnd = random.randint(1000, 9999)
		return os.path.join(TEMP_DIR, now.strftime("%Y%m%d%H%M%S") + '_' + now.strftime("%f") + '_' + str(rnd) + '.tmp')

	def __init__(self, input_stream, output_stream, prolog="", epilog="", encoding="utf-8"):
		super(TempFileTool, self).__init__(input_stream, output_stream)
		self.tmp_file = self.__gen_temp_file_path()
		self.prolog = prolog
		self.epilog = epilog
		self.encoding = encoding
		print(self.tmp_file)

	def _save_input_stream(self):
		F = open(self.tmp_file, "wt")#, encoding=self.encoding)
		try:
			buf = self.input_stream.read()
			print(buf)
			if len(self.prolog) > 0:
				F.write(self.prolog)
			F.write(buf)
			if len(self.epilog) > 0:
				F.write(self.epilog)
		finally:
			F.close()
			
	def _run_suprocess(self):
		print("system/qwerty1@ORCL_VM1 @" + self.tmp_file)
		po = Popen(["sqlplus.exe", "system/qwerty1@ORCL_VM1", "@"+self.tmp_file], stdout=PIPE, stderr=PIPE)
		pid = po.pid
			
	def run(self):
		self._save_input_stream()
		self._run_suprocess()
		