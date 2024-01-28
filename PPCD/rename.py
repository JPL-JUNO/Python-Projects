"""
@File         : rename.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-28 15:08:49
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""
import os

for file in os.listdir("./"):
    os.rename(file, file.lower().replace(" ", "_"))