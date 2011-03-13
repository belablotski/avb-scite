import sys

print "Sample script, called from SciTE tools menu..."
print "Command line arguments:"
for i in range(len(sys.argv)):
	print "  Parameter #%s=%s" % (i, sys.argv[i])

exit(0)