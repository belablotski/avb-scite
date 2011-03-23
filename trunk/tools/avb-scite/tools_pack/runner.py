"""
Enter point to run scripts.
"""

import sys

sys.path.append('C:/Programs/avb-scite/tools/avb-scite/tools_pack')
#print sys.path

class ToolException(Exception):
	pass

class ToolBase:
	def __init__(self, input_stream, output_stream, *args):
		pass
		
	def run(self):
		raise NotImplementedError("Method is't implemented.")


if __name__ == '__main__2':
	input_stream = sys.stdin
	output_stream = sys.stdout

	while True:
		line = input_stream.readline()
		output_stream.write(line)
	
if __name__ == '__main__':	
	t = ToolBase(None, None, None)
	t.run()
		