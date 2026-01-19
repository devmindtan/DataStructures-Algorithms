import os

root_path = r"/home/devmindtan/Documents/Code/DataStructures-Algorithms"

count = 0

for root, dirs, files in os.walk(root_path):
	dirs[:] = [d for d in dirs if not d.startswith('.')]
	filtered_files = [f for f in files if f.endswith('.py')]
	count += len(filtered_files)

print("Tổng số bài đã giải:", count)
