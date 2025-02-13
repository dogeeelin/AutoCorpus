#!/bin/bash

# 定义关键词数组
keywords=("经济学" "光学" "化学" "语言学")

# 遍历每个关键词
for keyword in "${keywords[@]}"; do
    echo "Processing files for: $keyword"
    
    # 创建输出目录（如果不存在）
    mkdir -p "output/$keyword"
    
    # 构建源文件夹路径
    source_dir="paper-pdf/${keyword}-100-pdf"
    
    # 检查源文件夹是否存在
    if [ ! -d "$source_dir" ]; then
        echo "Warning: Directory $source_dir not found, skipping..."
        continue
    fi
    
    # 遍历该关键词对应文件夹中的所有 PDF 文件
    for pdf_file in "$source_dir"/*.pdf; do
        # 检查文件是否存在
        if [ -f "$pdf_file" ]; then
            echo "Processing: $pdf_file"
            magic-pdf -p "$pdf_file" -o "output/$keyword" -m auto
        fi
    done
done

echo "All processing completed!"