"""
@File         : student_address_book.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-28 23:12:14
@Email        : cuixuanstephen@gmail.com
@Description  : 数据库使用实例——学生通讯录
"""
import sqlite3


def open_db():
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


def add_db():
    print("-" * 25, "欢迎使用添加数据功能", "-" * 25)
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
