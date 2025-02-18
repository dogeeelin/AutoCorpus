def merge_markdown_files(input_folder, output_file):
    """
    将指定文件夹中的所有markdown文件合并成一个文件
    
    Args:
        input_folder (str): 输入文件夹的路径
        output_file (str): 输出文件的路径
    """
    import os
    
    try:
        # 获取所有markdown文件
        markdown_files = [
            os.path.join(input_folder, f) 
            for f in os.listdir(input_folder) 
            if f.endswith(('.md', '.markdown'))
        ]
        
        # 按文件名排序
        markdown_files.sort()
        
        if not markdown_files:
            print(f"No markdown files found in {input_folder}")
            return
        
        # 合并所有文件内容
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for file_path in markdown_files:
                with open(file_path, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n')  # 添加换行以防文件末尾没有换行
        
        print(f"Successfully merged {len(markdown_files)} markdown files into {output_file}")
        
    except Exception as e:
        print(f"Error occurred while merging files: {str(e)}")

if __name__ == "__main__":
    merge_markdown_files("/home/linyun/AutoCorpus/paper-md-new/化学", "/home/linyun/AutoCorpus/paper-md-new/整合/化学-all.md")