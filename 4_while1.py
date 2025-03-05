"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    vvod = input("Как дела?")
    while vvod != "Хорошо":
        vvod = input("Как дела?")


if __name__ == "__main__":
    hello_user()
