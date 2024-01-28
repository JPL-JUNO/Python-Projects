"""
@File         : example.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-28 15:09:58
@Email        : cuixuanstephen@gmail.com
@Description  : 序列应用--猜单词游戏
"""
WORDS = (
    "python",
    "jumble",
    "easy",
    "difficult",
    "answer",
    "continue",
    "iPhone",
    "position",
    "game",
)

import random

word = random.choice(WORDS)
jumble = ""
while word:  # word 不是空字符串
    # 根据 word 长度产生 word 的一个随机位置
    position = random.randrange(len(word))
    # 将 position 位置的字母添加到乱序后的单词
    jumble += word[position]
    # 将 position 位置的字母从原单词中删除
    word = word[:position] + word[(position + 1) :]
print(jumble)
