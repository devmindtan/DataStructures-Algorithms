import os

# đường dẫn thư mục gốc
# C1
root_path = r"C:\Documents\Code\DataStructures-Algorithms"
# C2
root_path = "C:\\Documents\\Code\\DataStructures-Algorithms"

count = 0

for root, dirs, files in os.walk(root_path):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    filtered_files = [f for f in files if f.endswith('.py')]
    count += len(filtered_files)

print("Tổng số bài đã giải:", count)
