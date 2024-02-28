import schedule
import datetime
import random
import time
from timeline import *
from support import *

task_dict = {}


class Task:
    def __init__(self):
        self.id = random.randint(1, 1000000)
        self.__name = None
        self.__deadline = None
        self.__status = None

    def set_status(self, num):
        if num == 1:
            status = "Задача активна"
        elif num == 2:
            status = "Задача неактивна"
        self.__status = status

    def get_status(self):
        return self.__status

    def set_deadline(self):
        deadline = taskdeadline()
        self.__deadline = deadline

    def get_deadline(self):
        return self.__deadline

    def set_taskname(self):
        name = taskname()
        self.__name = name

    def get_taskname(self):
        return self.__name


class Cleaning(Task):
    def __init__(self):
        super().__init__()
        item = clean_item()
        self.item = item

    def task_info():
        launch = Cleaning()
        launch.set_taskname()
        launch.set_deadline()
        launch.set_status(1)

        task_cleaning = (
            launch.get_deadline().strftime("%Y-%m-%d-%H.%M.%S"),
            launch.get_taskname(),
            launch.item,
            launch.get_status(),
        )
        task_dict[launch.id] = task_cleaning
        print("Запомните ID вашей задачи!", launch.id)


class Training(Task):
    def __init__(self):
        super().__init__()
        muscle = training_muscle()
        self.muscle = muscle

    def task_info():
        launch = Training()
        launch.set_taskname()
        launch.set_deadline()

        task_training = (
            launch.get_deadline().strftime("%Y-%m-%d-%H.%M.%S"),
            launch.get_taskname(),
            launch.muscle,
            launch.get_status(),
        )
        task_dict[launch.id] = task_training
        print("Запомните ID вашей задачи!", launch.id)


class Student(Task):
    def __init__(self):
        super().__init__()
        study = homework()
        self.study = study

    def task_info():
        launch = Student()
        launch.set_taskname()
        launch.set_deadline()
        launch.set_status(1)

        task_student = (
            launch.get_deadline().strftime("%Y-%m-%d-%H.%M.%S"),
            launch.get_taskname(),
            launch.study,
            launch.get_status(),
        )
        task_dict[launch.id] = task_student
        print("Запомните ID вашей задачи!", launch.id)


def CRUDoperations():
    CRUDoperation = int(
        input(
            "Если хотите просмотреть имеющиеся задачи нажмите(1), чтобы удалить(2), или изменить(3),запустить авто-проверку заданий (0)"
        )
    )
    if CRUDoperation == 1:
        check_tusk = int(input("хотите посмотреть все задачи?(1),по конкретному ID(2)"))
        if check_tusk == 1:
            print(task_dict)
        if check_tusk == 2:
            check_tusk_id = int(input("Введите ваш ID:"))
            if check_tusk_id in task_dict:
                print(task_dict.get(check_tusk_id))
            else:
                print("Такого ID в базе нет!")

    if CRUDoperation == 2:
        del_tusk = int(input("Введите ID задания которое надо удалить: "))
        task_dict.pop(del_tusk)
        print("Удалено!БимБим БомБом")

    if CRUDoperation == 3:
        change_task = int(input("По какому ID меняем задание?: "))
        if type(task_dict[change_task]) == Cleaning:
            Cleaning.task_info()
        if type(task_dict[change_task]) == Training:
            Training.task_info()
        if type(task_dict[change_task]) == Student:
            Student.task_info()
    if CRUDoperation == 0:
        schedule.every(3).seconds.do(schedule_check)
        while True:
            schedule.run_pending()
            time.sleep(1)


def schedule_check():
    bla = "Задача активна"
    for item in task_dict.values():
        if bla in item:
            print((item))


while True:
    launch = tasktype()
    if launch == 1:
        Cleaning.task_info()
    elif launch == 2:
        Training.task_info()
    elif launch == 3:
        Student.task_info()

    CRUDoperations()
