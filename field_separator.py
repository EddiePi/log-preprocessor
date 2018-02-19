import re
source_file = "spark-log.log"
target_file = "spark-only-content.log"
fr = open(source_file)
fw = open(target_file, "a")

def match_line(line):
	result = re.match('(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}[,\.]\d{3}) (?P<loglevel>[A-Z]+) (?P<class>[\w+\.*]+:) (?P<content>.*)', line)
	# if result:
	# 	print "timestamp: ", result.group("timestamp")
	# 	print "loglevel: ", result.group("loglevel")
	# 	print "class: ", result.group("class")
	# 	print "content: ", result.group("content")
	# else:
	# 	print "not match"
	return result

#filter out the content with class, url, etc.
def need_filter(content):

	#filter out class name
	match_class = re.match('.*[a-zA-Z]+(\.[a-zA-Z]+)+.*', content)
	if match_class:
		print "filtered: true: " + content
		return True

	#filter out file and url
	match_url = re.match('.*(file:|https*:|hdfs).*', content)
	if match_url:
		print "filtered: true: " + content
		return True
	return False

# start of main function
i = 0
while 1:
	line = fr.readline()
	if not line:
		break
	i += 1
	lineResult = match_line(line)
	if lineResult:
		content = lineResult.group("content")
		if (not need_filter(content)):
			fw.write(content + "\n")
	else:
		print "not match. line: ", i






