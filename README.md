# HTML Table Bit Field Modifier

一个用于检查和修正HTML文件中表格数字格式的Python工具。该工具专门用于处理位字段表格，确保数字按照特定规则排列（从31开始递减到0）。

## 功能特性

- 🔍 自动扫描HTML文件中的表格
- 🔧 检查并修正表格中的数字格式
- 📝 生成详细的处理日志
- 📁 支持批量处理文件和目录
- 🎯 专门针对位字段表格优化

## 安装

### 环境要求

- Python 3.6+
- BeautifulSoup4

### 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 基本用法

```bash
python bit_field_modify.py <HTML文件或目录>
```

### 示例

```bash
# 处理单个HTML文件
python bit_field_modify.py example.html

# 处理整个目录
python bit_field_modify.py ./html_files/

# 处理多个文件和目录
python bit_field_modify.py file1.html file2.html ./directory/
```

## 工作原理

该工具会检查HTML表格中的数字格式，确保：

1. **首行数字**：第一行的第一个数字必须是31
2. **末行数字**：最后一行的最后一个数字必须是0
3. **数字连贯性**：相邻行之间的数字必须连贯递减（差值为1）

### 支持的数字格式

- 单个数字：`31`, `30`, `29`, ..., `0`
- 数字范围：`31:29`, `28:24`, `23:16`, ..., `7:0`

## 输出

- 修正后的HTML文件会直接覆盖原文件
- 处理日志保存在 `process_html_tables.log` 文件中

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 贡献

欢迎提交Issue和Pull Request！

## 作者

[@Allenliu999](https://github.com/Allenliu999)