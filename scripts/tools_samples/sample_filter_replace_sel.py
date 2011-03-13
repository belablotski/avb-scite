import sys

selection = sys.stdin.read()
result = '/* ' + selection + ' */'
sys.stdout.write(result)

exit(0)