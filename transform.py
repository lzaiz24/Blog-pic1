import re


def replace_links_in_file(input_file_path, output_file_path, old_base_url, new_base_url):
    # 读取原始Markdown文本
    with open(input_file_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()

    # 构建用于匹配的正则表达式
    pattern = re.compile(re.escape(old_base_url) + r'([^)]+)')

    # 执行替换
    modified_text = pattern.sub(new_base_url + r'\1', markdown_text)

    # 将替换后的文本写回文件
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(modified_text)


# 示例文件路径
input_file_path = 'out.md'
output_file_path = 'final.md'

# 旧的基础URL
old_base_url = "https://github.com/lzaiz24/Blog-pic1/tree/main"

# 新的基础URL
new_base_url = "https://picbed1.lzaiz24.top"

# 替换链接并写回文件
replace_links_in_file(input_file_path, output_file_path,
                      old_base_url, new_base_url)
