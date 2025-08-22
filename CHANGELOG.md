# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-22

### Added
- Initial release of HTML Table Bit Field Modifier
- Support for checking and fixing HTML table bit field formats
- Automatic validation of number sequences (31 to 0)
- Batch processing of HTML files and directories
- Comprehensive logging system
- Unit tests with pytest
- GitHub Actions CI/CD pipeline
- MIT License
- Complete documentation

### Features
- Validates first row starts with 31
- Validates last row ends with 0
- Ensures consecutive number decrements
- Supports both single numbers and ranges (e.g., "31:29")
- Preserves HTML formatting while fixing content
- Generates detailed processing logs