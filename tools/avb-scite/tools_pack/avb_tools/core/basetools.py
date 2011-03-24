"""Core classes for making tools."""

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class AvbSciteToolBase(object):
	def __init__(self, input_stream, output_stream):
		self.input_stream = input_stream
		self.output_stream = output_stream
		#self.pos_args = args
		#self.kw_args = kwargs
		
	def run(self):
		raise NotImplementedError("Method is't implemented.")


class EchoTool(AvbSciteToolBase):
	def __init__(self, input_stream, output_stream, *args, **kwargs):
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
	t = AvbSciteToolBase(None, None)
	t.run()
