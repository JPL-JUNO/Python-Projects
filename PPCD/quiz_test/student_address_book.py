"""
@File         : student_address_book.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-28 23:12:14
@Email        : cuixuanstephen@gmail.com
@Description  : 数据库使用实例——学生通讯录
"""
import sqlite3
from sqlite3 import Connection, Cursor
import functools


def print_welcome(info: str):
    print("-" * 25, info, "-" * 25)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


def open_db() -> tuple[Connection, Cursor]:
    conn = sqlite3.connect("./my_db.db")
    # conn.execute("drop table if exists address_book;")
    cur = conn.execute(
        "create table if not exists \
            address_book(usernum integer primary key, username varchar(128), \
                password varchar(128), address varchar(125), telnum varchar(128));"
    )
    return conn, cur


def show_all_db():
    print("-" * 25, "处理后的数据", "-" * 25)
    hel = open_db()
    cur = hel[1]
    cur.execute("select * from address_book;")
    res = cur.fetchall()
    for line in res:
        print(line)
    cur.close()


def info():
    usernum = input("请输入学号：")
    username = input("请输入姓名：")
    password = input("请输入密码：")
    address = input("请输入地址：")
    telnum = input("请输入联系电话：")
    return usernum, username, password, address, telnum


@print_welcome("欢迎使用添加数据功能")
def add_db():
    person = info()
    hel = open_db()
    hel[1].execute(
        "insert into address_book(usernum, username, password, address, telnum) values(?,?,?,?,?)",
        person,
    )
    hel[0].commit()
    print("-" * 25, "恭喜你，数据添加成功", "-" * 25)
    show_all_db()
    hel[0].close()


@print_welcome("欢迎使用删除数据库功能")
def del_db():
    del_choice = input("请输入想要删除学号：")
    hel = open_db()
    # 没有判断是否存在该学号
    hel[1].execute("delete from address_book where usernum = ?;", (del_choice,))
    hel[0].commit()
    print("-" * 25, "恭喜你，数据删除成功", "-" * 25)
    show_all_db()
    hel[0].close()


@print_welcome("欢迎使用修改数据库功能")
def alter():
    change_choice = input("请输入想要修改的学生的学号：")
    hel = open_db()
    person = info()
    hel[1].execute(
        "update address_book set usernum=?, username=?, password=?, address=?, telnum=?, where usernum"
        + change_choice,
        (person[0], person[1], person[2], person[3], person[4]),
    )
    hel[1].commit()
    show_all_db()
    hel[1].close()


if __name__ == "__main__":
    add_db()
    pass
