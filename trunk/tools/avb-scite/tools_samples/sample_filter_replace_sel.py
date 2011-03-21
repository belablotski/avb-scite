"""Replace editor selection. If selection region is empty - script will read information from console via sys.stdin"""

import sys

selection = sys.stdin.read()
result = '/* ' + selection + ' */'
sys.stdout.write(result)

exit(0)