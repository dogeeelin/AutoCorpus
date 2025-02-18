import spacy
import json
from pathlib import Path

def classify_clauses(json_file_path):
    """
    从JSON文件中读取句子，分类出that从句和to从句
    
    Args:
        json_file_path (str): JSON文件路径
    """
    try:
        # 加载spacy英语模型
        nlp = spacy.load("en_core_web_sm")
        
        # 读取JSON文件
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 创建结果字典
        results = {}
        
        # 遍历每个单词及其句子
        for word, sentences in data.items():
            # 初始化该单词的分类
            results[word] = {
                "that-clause": [],
                "to-clause": []
            }
            
            # 遍历每个句子
            for sentence in sentences:
                doc = nlp(sentence)
                
                # 遍历句子中的每个token
                for i, token in enumerate(doc):
                    # 获取词的原形
                    lemma = token.lemma_.lower()
                    
                    # 如果找到了目标词
                    if lemma == word.lower():
                        # 检查后面的词是否是 'that' 或 'to'
                        if i + 1 < len(doc):
                            next_token = doc[i + 1]
                            
                            # 检查that从句
                            if next_token.text.lower() == 'that':
                                results[word]["that-clause"].append(sentence)
                            
                            # 检查to从句
                            elif next_token.text.lower() == 'to':
                                results[word]["to-clause"].append(sentence)
        
        # 移除空的分类
        final_results = {}
        for word, clauses in results.items():
            if clauses["that-clause"] or clauses["to-clause"]:
                final_results[word] = {
                    k: v for k, v in clauses.items() if v
                }
        
        # 构建输出文件名
        output_file = Path(json_file_path).stem + '_clauses.json'
        
        # 写入新的JSON文件
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(final_results, f, ensure_ascii=False, indent=2)
        
        print(f"Successfully classified clauses to {output_file}")
        
        return final_results
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None


import json

def count_clauses(json_file_path, word_list, tag_type):
    """
    统计指定词列表中每个词的从句数量
    
    Args:
        json_file_path (str): JSON文件路径
        word_list (list): 要统计的词列表
        tag_type (str): 'that' 或 'to'，指定要统计的从句类型
    
    Returns:
        dict: 包含每个词的从句数量和总数的字典
    """
    try:
        # 验证tag_type参数
        if tag_type not in ['that', 'to']:
            raise ValueError("tag_type must be either 'that' or 'to'")
            
        # 构建tag字符串
        tag_clause = f"{tag_type}-clause"
        
        # 读取JSON文件
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 创建结果字典
        results = {}
        total_count = 0
        
        # 遍历词列表
        for word in word_list:
            # 如果词在数据中且有指定类型的从句
            if word in data and tag_clause in data[word]:
                count = len(data[word][tag_clause])
                results[word] = count
                total_count += count
        
        # 添加总数
        results['total_number'] = total_count
        
        # print(f"{tag_clause} in this corpus is: {results}")
        return results
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None


# 使用示例
if __name__ == "__main__":
    # 示例词列表
    tag = '光学'
    pos = 'noun'
    in_or_that = 'to'
    word_list = word_list = word_list = word_list = [
    "agreement", "decision", "desire", "failure", "inclination", 
    "intention", "obligation", "opportunity", "plan", "promise", 
    "proposal", "reluctance", "responsibility", "right", "tendency", 
    "threat", "wish", "willingness"
]
    # 统计that从句
    that_results = count_clauses(f"{tag}_stance-words_{pos}_clauses.json", word_list, in_or_that)
    print(f"{tag} {pos} {in_or_that} ease 从句统计结果：", that_results)