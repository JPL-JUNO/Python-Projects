"""
@File         : main.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-28 20:18:47
@Email        : cuixuanstephen@gmail.com
@Description  : 猜单词游戏程序
"""

import random

WORDS = (
    "python",
    "jumble",
    "easy",
    "difficult",
    "answer",
    "continue",
    "phone",
    "position",
    "pose",
    "game",
    "random",
    "uniform",
)

print(
    """
********************************
        欢迎参与猜单词游戏
    把字母组合成一个正确的单词 
********************************
"""
)

continue_mask = "Y"
while continue_mask.lower() == "y":
    word = random.choice(WORDS)

    correct = word

    jumble = ""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]

        word = word[:position] + word[position + 1 :]

    print("乱序后单词：", jumble)

    guess = input("请你猜测：")
    while guess != "" and guess != correct:
        print("对不起，不正确！")
        guess = input("继续猜：")
    if guess == correct:
        print("回答正确！")
    continue_mask = input("是否继续（Y/N）：")
