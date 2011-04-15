"""Core classes for making tools."""

import os.path
import datetime
import random
from subprocess import *
from avb_tools.settings import TEMP_DIR
from .exceptions import InvalidStateException


class ProcessorBase(object):
	"""
	Base class for all processors.
	Processors are used for pre and post processing data before and after tool execution.
	"""
	def __init__(self):
		pass

	def process(s):
		return(s)


class PreProcessor(ProcessorBase):
	def __init__(self):
		super(PreProcessor, self).__init__()


class PostProcessor(ProcessorBase):
	def __init__(self):
		super(PostProcessor, self).__init__()



class ToolBase(object):
	"""Base class for all tools"""
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


class TempFileTool_old(ToolBase):
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
		print("system/avb1-pass@avb1 @" + self.tmp_file)
		#po = Popen(["sqlplus.exe", "system/avb1-pass@avb1 @"+self.tmp_file], stdout=PIPE, stderr=PIPE)
		#pid = po.pid
		#po = Popen(["cmd",], stdout=PIPE, stderr=PIPE)
		with Popen(["sqlplus.exe", "-S", "system/avb1-pass@avb1", "@"+self.tmp_file], stdout=PIPE) as proc:
			output = proc.stdout.read()
			print(str(output, encoding=self.encoding))

			
	def run(self):
		self._save_input_stream()
		self._run_suprocess()


class ProcessRunnerTool(ToolBase):
	"""Tool for launching process."""
	def __init__(self, input_stream, output_stream, prolog="", epilog="", encoding="utf-8"):
		super(CmdSqlplusTool, self).__init__(input_stream, output_stream, prolog, epilog, encoding)
		self.popen = None

	def _prepare_popen(self):
		self.popen = Popen(["sqlplus.exe", "-S", "system/avb1-pass@avb1", "@"+self.tmp_file], stdout=PIPE)

	def _run_suprocess(self):
		if self.popen == None:
			raise InvalidStateException("ERROR: Popen object isn't created.")
		with self.popen as proc:
			output = proc.stdout.read()
			print(str(output, encoding=self.encoding))
			
	def run(self):
		self._prepare_popen()
		self._run_suprocess()

		

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
		print("system/avb1-pass@avb1 @" + self.tmp_file)
		#po = Popen(["sqlplus.exe", "system/avb1-pass@avb1 @"+self.tmp_file], stdout=PIPE, stderr=PIPE)
		#pid = po.pid
		#po = Popen(["cmd",], stdout=PIPE, stderr=PIPE)
		# "system/avb1-pass@avb1"
		with Popen(["sqlplus.exe", "-S", "/@ORCL161", "@"+self.tmp_file], stdout=PIPE) as proc:
			output = proc.stdout.read()
			print(str(output, encoding=self.encoding))

			
	def run(self):
		self._save_input_stream()
		self._run_suprocess()
