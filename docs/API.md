# API 文档

## 主要函数

### `find_html_files(paths)`

查找指定路径中的所有HTML文件。

**参数：**
- `paths` (list): 文件或目录路径列表

**返回：**
- `list`: HTML文件路径列表

### `extract_num_pair(s)`

从字符串中提取数字对。

**参数：**
- `s` (str): 包含数字的字符串（如"31:29"或"28"）

**返回：**
- `tuple`: (左数字, 右数字) 或 (数字, None)

### `clean_td_content(td)`

清理表格单元格内容，保留数字格式。

**参数：**
- `td`: BeautifulSoup的td元素

**返回：**
- `str` 或 `None`: 清理后的内容，如果格式不符则返回None

### `check_and_fix_table(table, filename, table_idx, log_lines)`

检查并修正表格中的数字格式。

**参数：**
- `table`: BeautifulSoup的table元素
- `filename` (str): 文件名
- `table_idx` (int): 表格索引
- `log_lines` (list): 日志行列表

**返回：**
- `tuple`: (是否有效, 是否已修改)

### `process_file(filepath, log_lines)`

处理单个HTML文件。

**参数：**
- `filepath` (str): 文件路径
- `log_lines` (list): 日志行列表

## 使用示例

```python
from bit_field_modify import extract_num_pair, find_html_files

# 提取数字对
left, right = extract_num_pair("31:29")
print(f"Left: {left}, Right: {right}")  # Left: 31, Right: 29

# 查找HTML文件
html_files = find_html_files(["./examples"])
print(html_files)  # ['./examples/sample.html']
```