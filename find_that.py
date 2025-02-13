import re
import os
import spacy

nlp = spacy.load("en_core_web_sm")

def count_pos_before_that(file_path):
    # 读取Markdown文件
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # 正则表达式匹配一级标题
    title_pattern = re.compile(r"^#\s+(.*)$", re.MULTILINE)
    titles = title_pattern.findall(content)

    # 正则表达式匹配包含"that"的句子
    that_pattern = re.compile(r"([^.!?]*that[^.!?]*[.!?])", re.IGNORECASE)

    # 按一级标题分割内容
    sections = re.split(r"^#\s+.*$", content, flags=re.MULTILINE)

    # 用于统计that前面不同词性的数量
    pos_count = {}

    # 遍历每个部分
    for i, section in enumerate(sections):
        if i == 0:
            continue  # 跳过第一个空部分
        that_matches = that_pattern.findall(section)
        if that_matches:
            for sentence in that_matches:
                # 使用spaCy处理句子
                doc = nlp(sentence)
                # 找到"that"的索引
                that_indexes = [i for i, token in enumerate(doc) if token.text.lower() == 'that']
                for that_index in that_indexes:
                    prev_token_index = that_index - 1
                    if prev_token_index >= 0:
                        prev_token = doc[prev_token_index]
                        prev_tag = prev_token.pos_
                        # 更新词性计数
                        if prev_tag in pos_count:
                            pos_count[prev_tag] += 1
                        else:
                            pos_count[prev_tag] = 1

    return pos_count


def print_sentence_info(file_path):
    # 读取 Markdown 文件
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # 正则表达式匹配一级标题
    title_pattern = re.compile(r"^#\s+(.*)$", re.MULTILINE)
    titles = title_pattern.findall(content)

    # 正则表达式匹配包含 "that" 的句子
    that_pattern = re.compile(r"([^.!?]*that[^.!?]*[.!?])", re.IGNORECASE)

    # 按一级标题分割内容
    sections = re.split(r"^#\s+.*$", content, flags=re.MULTILINE)

    # 遍历每个部分
    for i, section in enumerate(sections):
        if i == 0:
            continue  # 跳过第一个空部分
        current_title = titles[i - 1]
        that_matches = that_pattern.findall(section)
        if that_matches:
            print(f"Title: {current_title}")
            for sentence in that_matches:
                # 使用 spaCy 处理句子，自动完成分词和词性标注
                doc = nlp(sentence)
                # 找到 "that" 的索引
                that_indexes = [i for i, token in enumerate(doc) if token.text.lower() == 'that']
                for that_index in that_indexes:
                    prev_token_index = that_index - 1
                    if prev_token_index >= 0:
                        prev_token = doc[prev_token_index]
                        print("-" * 200)
                        print(f" - Sentence: {sentence.strip()}")
                        print(f"   Word before 'that': {prev_token.text}")
                        print(f"   Part of speech: {prev_token.pos_}")
            print()



def print_sentence_info_from_folder(folder_path, output_file_path, pos):
    # 打开输出文件以写入模式
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        # 遍历文件夹中的所有文件
        for filename in os.listdir(folder_path):
            if filename.endswith(".md"):
                file_path = os.path.join(folder_path, filename)
                # 读取 Markdown 文件
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()

                # 正则表达式匹配一级标题
                title_pattern = re.compile(r"^#\s+(.*)$", re.MULTILINE)
                titles = title_pattern.findall(content)

                # 正则表达式匹配包含 "that" 的句子
                that_pattern = re.compile(r"([^.!?]*that[^.!?]*[.!?])", re.IGNORECASE)

                # 按一级标题分割内容
                sections = re.split(r"^#\s+.*$", content, flags=re.MULTILINE)

                # 遍历每个部分
                for i, section in enumerate(sections):
                    if i == 0:
                        continue  # 跳过第一个空部分
                    current_title = titles[i - 1]
                    that_matches = that_pattern.findall(section)
                    if that_matches:
                        output_file.write(f"Title: {current_title}\n")
                        for sentence in that_matches:
                            # 使用 spaCy 处理句子，自动完成分词和词性标注
                            doc = nlp(sentence)
                            # 找到 "that" 的索引
                            that_indexes = [i for i, token in enumerate(doc) if token.text.lower() == 'that']
                            for that_index in that_indexes:
                                prev_token_index = that_index - 1
                                if prev_token_index >= 0:
                                    prev_token = doc[prev_token_index]
                                    if prev_token.pos_ == pos:
                                        output_file.write("-" * 200 + "\n")
                                        output_file.write(f" - Sentence: {sentence.strip()}\n")
                                        output_file.write(f"   Word before 'that': {prev_token.text}\n")
                                        output_file.write(f"   Part of speech: {prev_token.pos_}\n")
                        output_file.write("\n")


def return_sentence_list(folder_path, pos):
    sentence_list = []
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            file_path = os.path.join(folder_path, filename)
            # 读取 Markdown 文件
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            # 正则表达式匹配一级标题
            title_pattern = re.compile(r"^#\s+(.*)$", re.MULTILINE)
            titles = title_pattern.findall(content)

            # 正则表达式匹配包含 "that" 的句子
            that_pattern = re.compile(r"([^.!?]*that[^.!?]*[.!?])", re.IGNORECASE)

            # 按一级标题分割内容
            sections = re.split(r"^#\s+.*$", content, flags=re.MULTILINE)

            # 遍历每个部分
            for i, section in enumerate(sections):
                if i == 0:
                    continue  # 跳过第一个空部分
                current_title = titles[i - 1]
                that_matches = that_pattern.findall(section)
                if that_matches:
                    for sentence in that_matches:
                        # 使用 spaCy 处理句子，自动完成分词和词性标注
                        doc = nlp(sentence)
                        # 找到 "that" 的索引
                        that_indexes = [i for i, token in enumerate(doc) if token.text.lower() == 'that']
                        for that_index in that_indexes:
                            prev_token_index = that_index - 1
                            if prev_token_index >= 0:
                                prev_token = doc[prev_token_index]
                                if prev_token.pos_ == pos:
                                    sentence_info = sentence.strip()
                                    sentence_list.append(sentence_info)

    return sentence_list

def count_pos_in_folder(folder_path):
    total_pos_count = {}
    total_count = 0
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                pos_count = count_pos_before_that(file_path)
                # 合并当前文件的词性计数到总计数中
                for pos, count in pos_count.items():
                    if pos in total_pos_count:
                        total_pos_count[pos] += count
                    else:
                        total_pos_count[pos] = count
                    total_count += count
    total_pos_count["total"] = total_count
    return total_pos_count

def count_total_words_in_md_folder(folder_path):
    total_words = 0
    total_that = 0
    # 遍历文件夹及其子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # 使用 spaCy 对文本进行处理
                        doc = nlp(content)
                        # 统计词符数量
                        total_words += len(doc)
                        # 统计 "that" 的数量
                        for token in doc:
                            if token.text.lower() == 'that':
                                total_that += 1
                except Exception as e:
                    print(f"读取文件 {file_path} 时出现错误: {e}")
    return total_words, total_that


# 示例调用
# file_path = "/home/linyun/MinerU/paper-md/语言学/5. Lum (2021) The intrinsic frame of reference and the Dhivehi ‘FIBO’ system.md"
# pos_count = count_pos_before_that(file_path)
# print("Statistics of parts of speech before 'that':")
# for pos, count in pos_count.items():
#     print(f"{pos}: {count}")
# print_sentence_info(file_path)


# 读取一个文件夹里的所有Markdown文件，然后统计总的词性频次

# tag = '光学'
# folder_path = f"/home/linyun/MinerU/paper-md/{tag}"  # 替换为实际的文件夹路径

# total_pos_count = count_pos_in_folder(folder_path)
# print(f"Statistics of parts of speech before 'that' in the {tag} folder:")
# for pos, count in total_pos_count.items():
#     print(f"{pos}: {count}")

# total_words, total_that = count_total_words_in_md_folder(folder_path)

# print(f"Total words of {tag} folder:", total_words)   
# print(f"Total 'that' of {tag} folder:", total_that)



# folder_path = "/home/linyun/MinerU/paper-md/语言学"
# output_file_path = "sentence.txt"
# pos = "VERB"
# sentence_list = return_sentence_list(folder_path, pos)
# print(sentence_list)
# # 写入文件
# with open(output_file_path, "w", encoding="utf-8") as output_file:
#     for sentence in sentence_list:
#         output_file.write(sentence + "\n")


if __name__ == "__main__":
    folder_path = "/home/linyun/MinerU/paper-md-new/光学"
    total_words, total_that = count_total_words_in_md_folder(folder_path)
    print(total_words)