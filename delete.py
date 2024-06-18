import os

def delete_pdfs(directory):
    # 遍历目录树
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 检查文件是否为PDF
            if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)  # 删除文件
                    print(f"Deleted: {file_path}")  # 输出被删除文件的路径
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

# 使用示例
directory = "./"  # 将其替换为你的目标目录
delete_pdfs(directory)
