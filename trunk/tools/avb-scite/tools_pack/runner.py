"""
Enter point to run scripts.
"""

import sys

sys.path.append('C:/Programs/avb-scite/tools/avb-scite/tools_pack')


if __name__ == '__main__2':
	input_stream = sys.stdin
	output_stream = sys.stdout

	while True:
		line = input_stream.readline()
		output_stream.write(line)
	
if __name__ == '__main__':	
	print(sys.argv)
#	t = ToolBase(None, None)
#	t.run()
	