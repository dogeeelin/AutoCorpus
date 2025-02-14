def remove_math_blocks_from_md(input_path, output_path):
    """
    处理markdown文件，移除其中被 $$ $$ 包裹的数学公式块，但保留行内公式（单个 $ 包裹的）
    
    Args:
        input_path (str): 输入markdown文件的路径
        output_path (str): 输出markdown文件的路径
    """
    import re
    
    try:
        # 读取输入文件
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 移除数学公式块，包括可能的换行符
        cleaned_text = re.sub(r'\$\$(.*?)\$\$', '', content, flags=re.DOTALL)
        
        # 移除可能产生的多余空行，但保留最多两个连续空行
        cleaned_text = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned_text)
        
        # 写入输出文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text.strip())
            
        print(f"Successfully processed {input_path} -> {output_path}")
        
    except FileNotFoundError:
        print(f"Error: Could not find input file {input_path}")
    except Exception as e:
        print(f"Error occurred while processing file: {str(e)}")

def remove_html_tables(input_path, output_path):
    """
    处理markdown文件，删除所有<html>标签之间的内容
    
    Args:
        input_path (str): 输入markdown文件的路径
        output_path (str): 输出markdown文件的路径
    """
    import re
    
    try:
        # 读取输入文件
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 删除<html>标签之间的内容
        cleaned_text = re.sub(r'<html>.*?</html>', '', content, flags=re.DOTALL)
        
        # 移除可能产生的多余空行
        cleaned_text = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned_text)
        
        # 写入输出文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text.strip())
            
        print(f"Successfully removed HTML tables from {input_path}")
        
    except FileNotFoundError:
        print(f"Error: Could not find input file {input_path}")
    except Exception as e:
        print(f"Error occurred while processing file: {str(e)}")


def remove_references_section(input_path, output_path):
    """
    处理markdown文件，删除从"# REFERENCES"到下一个标题之间的内容
    
    Args:
        input_path (str): 输入markdown文件的路径
        output_path (str): 输出markdown文件的路径
    """
    import re
    
    try:
        # 读取输入文件
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找 "# REFERENCES" 部分
        pattern1 = r'# REFERENCES.*?(?=\n#|\Z)'
        pattern2 = r'# Articles.*?(?=\n#|\Z)'
        cleaned_text = re.sub(pattern1, '', content, flags=re.DOTALL | re.IGNORECASE)
        cleaned_text = re.sub(pattern2, '', cleaned_text, flags=re.DOTALL | re.IGNORECASE)

        
        # 移除可能产生的多余空行，但保留最多两个连续空行
        cleaned_text = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned_text)
        
        # 写入输出文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text.strip())
            
        print(f"Successfully processed {input_path} -> {output_path}")
        
    except FileNotFoundError:
        print(f"Error: Could not find input file {input_path}")
    except Exception as e:
        print(f"Error occurred while processing file: {str(e)}")

def remove_appendix_section(input_path, output_path):
    """
    处理markdown文件，删除从包含"appendix"的一级标题到下一个一级标题之间的内容
    
    Args:
        input_path (str): 输入markdown文件的路径
        output_path (str): 输出markdown文件的路径
    """
    import re
    
    try:
        # 读取输入文件
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找包含 "appendix" 的一级标题部分（不区分大小写）
        pattern = r'\n# [^\n]*appendix[^\n]*\n.*?(?=\n# |\Z)'
        cleaned_text = re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
        
        # 移除可能产生的多余空行，但保留最多两个连续空行
        cleaned_text = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned_text)
        
        # 写入输出文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text.strip())
            
        print(f"Successfully removed appendix section from {input_path}")
        
    except FileNotFoundError:
        print(f"Error: Could not find input file {input_path}")
    except Exception as e:
        print(f"Error occurred while processing file: {str(e)}")

def remove_image_references(input_path, output_path):
    """
    处理markdown文件，删除所有图片引用（![...](...)格式）
    
    Args:
        input_path (str): 输入markdown文件的路径
        output_path (str): 输出markdown文件的路径
    """
    import re
    
    try:
        # 读取输入文件
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 删除图片引用
        # 匹配 ![任意文本](任意路径) 格式
        pattern = r'!\[.*?\]\(.*?\)'
        cleaned_text = re.sub(pattern, '', content)
        
        # 移除可能产生的多余空行
        cleaned_text = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned_text)
        
        # 写入输出文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text.strip())
            
        print(f"Successfully removed image references from {input_path}")
        
    except FileNotFoundError:
        print(f"Error: Could not find input file {input_path}")
    except Exception as e:
        print(f"Error occurred while processing file: {str(e)}")

def remove_post_conclusion(input_path, output_path):
    """
    处理markdown文件，如果存在包含"conclusion"的一级标题，
    则删除从下一个一级标题开始的所有内容。
    可以匹配的标题形式包括：
    # Conclusions
    # CONCLUSION
    # 4. Discussion and conclusions
    等变体形式
    
    Args:
        input_path (str): 输入markdown文件的路径
        output_path (str): 输出markdown文件的路径
    """
    import re
    
    try:
        # 读取输入文件
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找是否存在包含 "conclusion" 的一级标题
        # 匹配模式支持可选的数字编号和其他词语
        conclusion_pattern = r'\n# (?:\d+\.)?\s*(?:[A-Za-z\s]+and\s+)?conclusion[s]?\b'
        if re.search(conclusion_pattern, content, flags=re.IGNORECASE):
            # 找到conclusion标题后的第一个一级标题的位置
            matches = list(re.finditer(conclusion_pattern, content, flags=re.IGNORECASE))
            conclusion_pos = matches[-1].end()  # 使用最后一个匹配的conclusion标题
            
            # 查找conclusion之后的第一个一级标题
            next_heading = re.search(r'\n# ', content[conclusion_pos:])
            if next_heading:
                # 如果找到下一个一级标题，只保留到该标题之前的内容
                cleaned_text = content[:conclusion_pos + next_heading.start()]
            else:
                # 如果没有找到下一个一级标题，保持原文不变
                cleaned_text = content
        else:
            cleaned_text = content
        
        # 移除可能产生的多余空行
        cleaned_text = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned_text)
        
        # 写入输出文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text.strip())
            
        print(f"Successfully processed post-conclusion content from {input_path}")
        
    except FileNotFoundError:
        print(f"Error: Could not find input file {input_path}")
    except Exception as e:
        print(f"Error occurred while processing file: {str(e)}")

def process_md_file(input_path, output_path):
    """
    处理markdown文件：
    1. 移除数学公式块
    2. 移除参考文献部分
    3. 移除HTML表格
    4. 移除附录部分
    5. 移除图片引用
    6. 移除conclusion后的内容
    
    Args:
        input_path (str): 输入markdown文件的路径
        output_path (str): 输出markdown文件的路径
    """
    import os
    
    # 创建临时文件路径（减少到5个临时文件）
    temp_paths = [output_path + f'.temp{i}' for i in range(1, 6)]
    
    try:
        # 处理链
        remove_math_blocks_from_md(input_path, temp_paths[0])
        remove_references_section(temp_paths[0], temp_paths[1])
        remove_html_tables(temp_paths[1], temp_paths[2])
        remove_appendix_section(temp_paths[2], temp_paths[3])
        remove_image_references(temp_paths[3], temp_paths[4])
        remove_post_conclusion(temp_paths[4], output_path)
        
        # 删除所有临时文件
        for temp_file in temp_paths:
            if os.path.exists(temp_file):
                os.remove(temp_file)
        
        print(f"Successfully processed file: {input_path} -> {output_path}")
        
    except Exception as e:
        print(f"Error occurred while processing file: {str(e)}")
        # 确保清理临时文件
        for temp_file in temp_paths:
            if os.path.exists(temp_file):
                os.remove(temp_file)

def process_folder(input_folder, output_folder):
    """
    处理文件夹下的所有md文件
    
    Args:
        input_folder (str): 输入文件夹路径
        output_folder (str): 输出文件夹路径
    """
    import os
    
    try:
        # 确保输出文件夹存在
        os.makedirs(output_folder, exist_ok=True)
        
        # 遍历输入文件夹中的所有文件
        for filename in os.listdir(input_folder):
            if filename.endswith('.md'):
                # 构建完整的输入输出路径
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)
                
                # 处理单个文件
                process_md_file(input_path, output_path)
                
        print(f"Successfully processed all files from {input_folder} to {output_folder}")
        
    except Exception as e:
        print(f"Error occurred while processing folder: {str(e)}")

if __name__ == "__main__":
    # 设置输入输出文件夹路径
    input_folder = "/home/linyun/AutoCorpus/paper-md/化学"
    output_folder = "/home/linyun/AutoCorpus/paper-md-new/化学"
    
    # 处理整个文件夹
    process_folder(input_folder, output_folder)
