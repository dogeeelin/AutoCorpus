import spacy
import json
from pathlib import Path
from tqdm import tqdm
import argparse  # 导入 argparse

# 读取一个json文件，分别统计每一行行键值对中值的len（值是一个列表）
def count_json_word(json_file):
    """
    读取json文件并统计每个键值对中值的长度
    
    Args:
        json_file (str): JSON文件路径
    
    Returns:
        dict: 包含每个键值对值长度的字典
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        results = {}
        for key in data:
            results[key] = len(data[key])
        
        return results
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {}


def read_txt_to_list(file_path):
    """
    读取文本文件并将每一行存储为列表中的一个元素
    
    Args:
        file_path (str): 文本文件的路径
    
    Returns:
        list: 包含文件每一行的列表
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # 读取所有行
            lines = [line.strip() for line in lines]  # 去除每行的换行符和空格
        return lines
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return []


def extract_sentences_with_words(folder_path, subject_tag, pos_tag, word_list, naming_tag):
    """
    从markdown文件夹中提取包含指定词汇的句子，考虑词形变化
    
    Args:
        folder_path (str): markdown文件夹路径
        subject_tag (str): 学科标签
        pos_tag (str): 词性标签 ('VERB', 'NOUN', 'ADJ', 'ADV')
        word_list (list): 需要查找的单词列表
        naming_tag (str): 输出文件的命名标签
    """
    try:
        # 加载spacy英语模型
        nlp = spacy.load("en_core_web_sm")
        
        # 创建结果字典
        results = {}
        for word in word_list:
            results[word] = []
        
        # 获取所有markdown文件
        md_files = Path(folder_path).glob("*.md")
        
        # 遍历每个markdown文件
        for md_file in md_files:
            # 读取markdown文件
            with open(md_file, 'r', encoding='utf-8') as f:
                text = f.read()
            
            # 处理文本
            doc = nlp(text)
            
            # 遍历每个句子
            for sent in doc.sents:
                # 对于每个句子，检查是否包含目标词
                for token in sent:
                    # 获取词的原形
                    if pos_tag == "ADJ":
                        lemma = token.text.lower()
                    else:
                        lemma = token.lemma_.lower()
                    
                    # 如果词的原形在目标词列表中，且词性匹配
                    if lemma in word_list and token.pos_ == pos_tag:
                        # 将句子添加到对应词的列表中
                        results[lemma].append(sent.text.strip())
        
        # 移除重复的句子
        for word in results:
            results[word] = list(dict.fromkeys(results[word]))
        
        # 构建输出文件名
        output_file = f"{subject_tag}_{naming_tag}_{pos_tag.lower()}.json"
        
        # 写入JSON文件
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"Successfully extracted sentences to {output_file}")
        
        return results
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None

# 使用示例
if __name__ == "__main__":
    # # 设置命令行参数解析
    # parser = argparse.ArgumentParser(description="Extract sentences containing specific words from markdown files.")
    # parser.add_argument("--subject_tag", type=str, help="The subject tag for the extraction.")
    # parser.add_argument("--pos_tag", type=str, choices=['VERB', 'NOUN', 'ADJ'], help="The part of speech tag.")
    # parser.add_argument("--word_list_path", type=str, help="Path to the text file containing the list of words.")
    
    # args = parser.parse_args()
    
    # # 从命令行参数获取值
    # subject_tag = args.subject_tag
    # pos_tag = args.pos_tag
    # folder_path = f"/home/linyun/AutoCorpus/paper-md-new/{subject_tag}"
    # word_list = read_txt_to_list(args.word_list_path)
    # naming_tag = "stance-words"
    
    # results = extract_sentences_with_words(folder_path, subject_tag, pos_tag, word_list, naming_tag) 

    print(count_json_word("光学_stance-words_adj.json"))