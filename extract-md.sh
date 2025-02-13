#!/bin/bash

# 定义关键词数组（与pdf-to-md.sh保持一致）
keywords=("经济学" "光学" "化学" "语言学")

# 遍历每个关键词（学科）
for keyword in "${keywords[@]}"; do
    echo "Processing files for: $keyword"
    
    # 为每个学科创建对应的目标文件夹
    mkdir -p "paper-md/$keyword"
    
    # 查找并复制该学科下的所有md文件
    find "output/$keyword" -type f -name "*.md" -exec cp {} "paper-md/$keyword/" \;
done

# 显示复制完成的消息
echo "所有MD文件已按学科分类复制到paper-md文件夹中"