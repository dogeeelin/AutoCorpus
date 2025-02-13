import os
import re
import spacy
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from collections import defaultdict


nlp = spacy.load("en_core_web_sm")

def get_top_k_words_in_folder(folder_path, pos_tag, k):
    # 用于存储符合词性要求的词的词频
    word_freq = defaultdict(int)

    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):  # 假设只处理 Markdown 文件
                file_path = os.path.join(root, file)
                # 读取文件内容
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # 正则表达式匹配包含"that"的句子
                that_pattern = re.compile(r"([^.!?]*that[^.!?]*[.!?])", re.IGNORECASE)
                that_matches = that_pattern.findall(content)

                for sentence in that_matches:
                    # 使用 spaCy 处理句子
                    doc = nlp(sentence)

                    # 遍历句子中的每个词符
                    for i in range(len(doc) - 1):
                        token = doc[i]
                        next_token = doc[i + 1]

                        # 如果下一个词是 "that" 并且当前词的词性符合要求
                        if next_token.text.lower() == "that" and token.pos_ == pos_tag:
                            # 词形还原
                            lemma_word = token.lemma_.lower()
                            # 更新词频
                            word_freq[lemma_word] += 1

    # 获取词频最高的前 k 个词
    top_k_words = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)[:k]
    return top_k_words

# 示例调用
folder_path = '/home/linyun/MinerU/paper-md/光学'
pos_tag = 'VERB'
k = 30
result = get_top_k_words_in_folder(folder_path, pos_tag, k)
for word, freq in result:
    print(f"Word: {word}, Frequency: {freq}")
