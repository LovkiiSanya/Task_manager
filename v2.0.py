from typing import Self
import schedule
import datetime
import random
import time
from timeline import *
from support import *
import enum

task_dict = {}


class TaskStatus(enum.Enum):
    Активна = 1
    Неактивна = 2


class MainTask:
    def __init__(self):
        self.__id = random.randint(1, 1000000)
        self.__name = None
        self.__deadline = None
        self.__status = None

    def set_status(self, num):
        status = TaskStatus
        if num == 1:
            status = "Ваша задача: {}".format(status(1).name)
        elif num == 2:
            status = "Ваша задача: {}".format(status(2).name)
        self.__status = status

    def get_status(self):
        return self.__status

    def get_id(self):
        return self.__id

    def set_deadline(self):
        deadline = user_set_deadline()
        self.__deadline = deadline

    def get_deadline(self):
        return self.__deadline

    def set_taskname(self):
        name = set_name_task()
        self.__name = name

    def get_taskname(self):
        return self.__name


class CleaningTask(MainTask):
    def __init__(self):
        super().__init__()
        item = clean_item()
        self.item = item

    def set_task_parameters():
        launch = CleaningTask()
        launch.set_taskname()
        launch.set_deadline()
        launch.set_status(1)
        task_dict[launch.get_id()] = launch
        print("Запомните ID вашей задачи!", launch.get_id())

    def __repr__(self):
        Cleaning = type(self).__name__
        return f"{Cleaning}({self.get_id()!r},{self.get_deadline()!r},{self.get_status()!r},{self.get_taskname()!r},{self.item})"

    def __str__(self):
        return f"Ваш ID: {self.get_id()} Дедлайн: {self.get_deadline()} {self.get_status()} Название: {self.get_taskname()} Комната/предмет: {self.item}"


class TrainingTask(MainTask):
    def __init__(self):
        super().__init__()
        muscle = training_muscle()
        self.muscle = muscle

    def set_task_parameters():
        launch = TrainingTask()
        launch.set_taskname()
        launch.set_deadline()
        launch.set_status(1)
        task_dict[launch.get_id()] = launch
        print("Запомните ID вашей задачи!", launch.get_id())

    def __repr__(self):
        Training = type(self).__name__
        return f"{Training}({self.get_id()!r},{self.get_deadline()!r},{self.get_status()!r},{self.get_taskname()!r},{self.muscle})"

    def __str__(self):
        return f"Ваш ID: {self.get_id()} Дедлайн: {self.get_deadline()} {self.get_status()} Название: {self.get_taskname()} Группа мышц: {self.muscle}"


class HomeworkTask(MainTask):
    def __init__(self):
        super().__init__()
        study = homework()
        self.study = study

    def set_task_parameters():
        launch = HomeworkTask()
        launch.set_taskname()
        launch.set_deadline()
        launch.set_status(1)
        task_dict[launch.get_id()] = launch
        print("Запомните ID вашей задачи!", launch.get_id())

    def __repr__(self):
        Student = type(self).__name__
        return f"{Student}({self.get_id()!r},{self.get_deadline()!r},{self.get_status()!r},{self.get_taskname()!r},{self.study})"

    def __str__(self):
        return f"Ваш ID: {self.get_id()} Дедлайн: {self.get_deadline()} {self.get_status()} Название: {self.get_taskname()} Группа мышц: {self.study}"


def create_task():
    launch = task_type_by_class()
    if launch == 1:
        CleaningTask.set_task_parameters()
        one_more_task = input("Хотите создать еще одну задачу?(д = да/н = нет)")
        if one_more_task == "д":
            create_task()
        else:
            CRUDoperations()
    elif launch == 2:
        TrainingTask.set_task_parameters()
        one_more_task = input("Хотите создать еще одну задачу?(д = да/н = нет)")
        if one_more_task == "д":
            create_task()
        else:
            CRUDoperations()
    elif launch == 3:
        HomeworkTask.set_task_parameters()
        one_more_task = input("Хотите создать еще одну задачу?(д = да/н = нет)")
        if one_more_task == "д":
            create_task()
        else:
            CRUDoperations()


def CRUDoperations():
    CRUDoperation = int(
        input(
            "Если хотите создать новую задачу нажмите (1)\nЕсли хотите просмотреть имеющиеся задачи нажмите(2) \nЧтобы удалить(3) \nЧтобы изменить(4) \nЗапустить авто-проверку заданий (0)"
        )
    )
    if CRUDoperation == 1:
        create_task()
    if CRUDoperation == 2:
        check_tusk = int(input("хотите посмотреть все задачи?(1),по конкретному ID(2)"))
        if check_tusk == 1:
            print(task_dict)
        if check_tusk == 2:
            check_tusk_id = int(input("Введите ваш ID:"))
            if check_tusk_id in task_dict:
                print(task_dict.get(check_tusk_id))
            else:
                print("Такого ID в базе нет!")

    if CRUDoperation == 3:
        del_tusk_by_id = int(input("Введите ID задания которое надо удалить: "))
        task_dict.pop(del_tusk_by_id)
        print("Удалено!БимБим БомБом")

    if CRUDoperation == 4:
        change_task_by_id = int(input("По какому ID меняем задание?: "))
        if type(task_dict[change_task_by_id]) == CleaningTask:
            CleaningTask.set_task_parameters()
        if type(task_dict[change_task_by_id]) == TrainingTask:
            TrainingTask.set_task_parameters()
        if type(task_dict[change_task_by_id]) == HomeworkTask:
            HomeworkTask.set_task_parameters()
    if CRUDoperation == 0:
        schedule.every(3).seconds.do(schedule_check)
        while True:
            schedule.run_pending()
            time.sleep(1)


def schedule_check():
    for key in task_dict.values():
        if key.get_deadline() < datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"):
            key.set_status(2)
            print(key)
        else:
            print(key)


while True:
    CRUDoperations()
