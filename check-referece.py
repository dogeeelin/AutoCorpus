import os

def check_references_in_md_files(folder_path):
    reference_count = 0
    total_files = 0

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            total_files += 1
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                if "# References" in content:
                    reference_count += 1

    print(f"总共有 {total_files} 个Markdown文件。")
    print(f"其中有 {reference_count} 个文件包含 '# References'。")

# 替换为你的文件夹路径
folder_path = "/home/linyun/MinerU/paper-md/语言学"
check_references_in_md_files(folder_path)