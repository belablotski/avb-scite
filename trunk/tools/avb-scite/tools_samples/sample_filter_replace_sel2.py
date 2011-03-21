"""
Replace editor selection. 
If selection region is empty - script will do nothing.
This behavior is done with: command.input.22.*=_$(CurrentSelection)

command.name.22.*=sample_filter_replace_sel2
command.22.*=$(SciteDefaultHome)\python.bat $(SciteDefaultHome)\tools\avb-scite\tools_samples\sample_filter_replace_sel2.py
# filter - accepts keyword arguments yes and no; quiet - accepts keyword arguments yes and no; replaceselection - accepts yes, no, and auto; savebefore - accepts yes, no, and prompt; subsystem - console, windows, shellexec, lua, director, winhelp, htmlhelp; groupundo - yes or no
command.mode.22.*=filter:no,quiet:yes,replaceselection:yes,savebefore:no,subsystem:console
command.input.22.*=_$(CurrentSelection)

"""

import sys

selection = sys.stdin.read()
if selection != '_':
	result = '/* ' + selection[1:] + ' */'
	sys.stdout.write(result)

exit(0)