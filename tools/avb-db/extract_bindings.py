"""Extract binding variables from SQL query.

TODO:
	Skip comments -- and /* */
	Skip strings 'xxx' and 'xxx''s'
"""
import sys, re

def remove_comments(sql):
	sql = re.sub("(?m)--.*$", "", sql)
	sql = re.sub(r"/\*.*\*/", "", sql)
	return sql

def get_sql():
	#F = open('784.sql')
	#sql = F.readlines();
	#F.close
	#return ''.join(sql)
	selection = sys.stdin.read()
	if selection == '_':
		exit(1)
	return selection
	
def unit_tests():
	assert remove_comments("select * -- here comment is") == "select * "
	assert remove_comments("""select * -- here comment #1 is
from dual -- here comment #2 is""") == """select * 
from dual """
	assert remove_comments("select * /*here comment is*/ from dual") == "select *  from dual"
	assert remove_comments("""select * /* here comment #1 is */
from dual /* here comment #2 is*/""") == """select * 
from dual """
	assert remove_comments("""select * -- here comment #1 is
/* here comment #2 is*/from dual""") == """select * 
from dual"""
	assert remove_comments("""select * /* comment with 'string' */ from dual -- 'string' is here too""") == "select *  from dual "


if __name__ == '__main__':
	#unit_tests()
	
	sql = get_sql()
	bindings = re.findall(":[0-9A-Za-z_]*", sql)
	bindings_counts = {}
	for binding in bindings:
		if binding in bindings_counts:
			bindings_counts[binding] += 1
		else:
			bindings_counts[binding] = 1
	print "\n".join(sorted(bindings_counts.keys()))

	