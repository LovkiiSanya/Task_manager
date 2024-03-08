from timeline import *


def clean_item():
    item = input(
        "Введите название комнаты или предмета который будем приводить в порядок? :"
    )
    return item


def training_muscle():
    muscle = input("Какую мышцу будем качать? : ")
    return muscle


def homework():
    homework = input("Какие уроки будем делать? : ")
    return homework


def set_name_task():
    name = input("Давайте сразу дадим название нашему заданию: ")
    return name


def task_type_by_class():
    print(
        "Выбери категорию заданий :(Бытовые дела = 1),(Тренировка = 2),(Домашняя работа = 3)"
    )
    type = int(input())
    if 1 <= type <= 3:
        return type
    else:
        print("Что-то пошло не так, давайте еще разок")

