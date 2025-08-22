# Contributing to HTML Table Bit Field Modifier

感谢您对本项目的关注！我们欢迎各种形式的贡献。

## 如何贡献

### 报告Bug

如果您发现了bug，请创建一个issue并包含以下信息：

- 详细的bug描述
- 重现步骤
- 期望的行为
- 实际的行为
- 您的环境信息（Python版本、操作系统等）

### 提出新功能

如果您有新功能的想法：

1. 首先创建一个issue讨论这个功能
2. 等待维护者的反馈
3. 如果获得批准，您可以开始实现

### 提交代码

1. Fork这个仓库
2. 创建您的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建一个Pull Request

### 代码规范

- 遵循PEP 8 Python代码规范
- 为新功能添加测试
- 确保所有测试通过
- 更新相关文档

### 测试

运行测试：

```bash
python -m pytest tests/
```

运行带覆盖率的测试：

```bash
python -m pytest tests/ --cov=. --cov-report=html
```

## 开发环境设置

1. 克隆仓库：
```bash
git clone https://github.com/Allenliu999/html-table-bit-field-modifier.git
cd html-table-bit-field-modifier
```

2. 创建虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
pip install pytest pytest-cov
```

## 许可证

通过贡献代码，您同意您的贡献将在MIT许可证下授权。