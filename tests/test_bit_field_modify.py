#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import tempfile
import os
from bit_field_modify import extract_num_pair, find_html_files, clean_td_content
from bs4 import BeautifulSoup


class TestBitFieldModify(unittest.TestCase):
    
    def test_extract_num_pair(self):
        """测试数字对提取功能"""
        # 测试范围格式
        left, right = extract_num_pair("31:29")
        self.assertEqual(left, 31)
        self.assertEqual(right, 29)
        
        # 测试单个数字
        left, right = extract_num_pair("28")
        self.assertEqual(left, 28)
        self.assertIsNone(right)
        
        # 测试带空格的格式
        left, right = extract_num_pair(" 15 : 8 ")
        self.assertEqual(left, 15)
        self.assertEqual(right, 8)
    
    def test_find_html_files(self):
        """测试HTML文件查找功能"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # 创建测试文件
            html_file = os.path.join(temp_dir, "test.html")
            txt_file = os.path.join(temp_dir, "test.txt")
            
            with open(html_file, 'w') as f:
                f.write("<html></html>")
            with open(txt_file, 'w') as f:
                f.write("test")
            
            # 测试目录扫描
            html_files = find_html_files([temp_dir])
            self.assertEqual(len(html_files), 1)
            self.assertTrue(html_files[0].endswith("test.html"))
            
            # 测试单文件
            html_files = find_html_files([html_file])
            self.assertEqual(len(html_files), 1)
            self.assertEqual(html_files[0], html_file)
    
    def test_clean_td_content(self):
        """测试表格单元格内容清理功能"""
        # 测试范围格式
        soup = BeautifulSoup("<td> 31 : 29 </td>", 'html.parser')
        td = soup.find('td')
        result = clean_td_content(td)
        self.assertEqual(result, "31:29")
        
        # 测试单个数字
        soup = BeautifulSoup("<td> 28 </td>", 'html.parser')
        td = soup.find('td')
        result = clean_td_content(td)
        self.assertEqual(result, "28")
        
        # 测试无效格式
        soup = BeautifulSoup("<td>invalid</td>", 'html.parser')
        td = soup.find('td')
        result = clean_td_content(td)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()