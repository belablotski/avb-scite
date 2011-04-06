"""Global exceptions."""

class ToolException(Exception):
	"""Base exception for all tools exceptions."""
	pass


class EmptyInputException(ToolException):
	"""Input is empty and commandlet can't do its work. 
	For example, SciTE selection region is empty and commandlet need to be executed with piped stdin.
	"""
	def __init__(self, msg = "ERROR: Can't run command script: input is empty."):
		super(EmptyInputException, self).__init__(msg)
