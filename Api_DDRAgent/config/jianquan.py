# -*- coding: utf-8 -*-
import os

prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）
token_path = os.path.join(prj_path,'config','token')

with open(token_path) as f:
    content = f.read()

header2 = 'Token {}'.format(content)