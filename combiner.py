import os
#root_dir = "/home/eddie/logs/yarn-default"
root_dir = "/Users/Eddie/gitRepo/log-preprocessor/test-log-dir"
source_files = ["stderr"]
target_file = "./test-log-dir/combined_log"

g = os.walk(root_dir, topdown=False)

if os.path.exists(target_file):
	os.remove(target_file)

fw = open(target_file, "a")
for child_root, dirs, files in g:
	for file_name in files:
		if source_files.__contains__(file_name):
			fr = open(os.path.join(child_root, file_name))
			while 1:
				line = fr.readline().strip('\t\n\r')
				if not line:
					break;
				fw.write(line + "\n")
