from typing import Self
import schedule
import datetime
import random
import time
from timeline import *
from support import *
import enum
import psycopg2
from peewee import *



try:
    connection = PostgresqlDatabase("postgres",
        host="127.0.0.1", user="admin", password="root"
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        print(cursor.fetchone())

except Exception as _ex:
    print("[INFO] Ошибка при работе с Базой данных", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] Соединение с Базой данных закрыто.")

class BaseModel(Model):
    class Meta:
        database = connection

class TaskManagerTable(BaseModel):
    id_task = IntegerField(column_name="id")
    task_table_type = TextField(column_name="task_type")
    task_table_name = TextField(column_name="task_name")
    task_table_deadline = DateField(column_name="task_deadline")
    task_table_status = TextField(column_name="task_status")
    task_table_item = TextField(column_name="task_item")
    class Meta:
        table_name = "task_manager"


        
def main():
    pass


task_dict = {}


class TaskStatus(enum.Enum):
    ACTIVE = 1
    INACTIVE = 2


class MainTask:
    __id: int
    __name: str
    __deadline: datetime
    __status: int

    def __init__(self) -> None:
        self.__id = random.randint(1, 1000000)
        self.__name = None
        self.__deadline = None
        self.__status = None

    def set_status(self, num: TaskStatus):
        status = TaskStatus
        if num == 1:
            status = "Ваша задача: {}".format(TaskStatus.ACTIVE)
        elif num == 2:
            status = "Ваша задача: {}".format(TaskStatus.INACTIVE)
        self.__status = status

    def get_status(self) -> TaskStatus:
        return self.__status

    def get_id(self):
        return self.__id

    def set_deadline(self, deadline):
        self.__deadline = deadline

    def get_deadline(self):
        return self.__deadline

    def set_taskname(self):
        name = set_name_task()
        self.__name = name

    def get_taskname(self):
        return self.__name


class CleaningTask(MainTask):
    __item: str

    def __init__(self):
        super().__init__()
        self.__item = None

    def set_item(self):
        self.__item = clean_item()

    def get_item(self):
        return self.__item

    def set_task_parameters() -> None:
        launch = CleaningTask()
        launch.set_taskname()
        launch.set_item()
        try:
            deadline = user_set_deadline()
            launch.set_deadline(deadline)
        except ValueError:
            print(
                "Вводить надо только дату,автоматически установлена текущая время и дата"
            )
            deadline = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            launch.set_deadline(deadline)
        launch.set_status(1)
        task_dict[launch.get_id()] = launch

        print("Запомните ID вашей задачи!", launch.get_id())

        TaskManagerTable.create(id_task = launch.get_id(),task_table_type = "Уборка",task_table_name = launch.get_taskname(),task_table_deadline = launch.get_deadline(),
                                task_table_status = launch.get_status(),task_table_item = launch.get_item())

    def __repr__(self):
        Cleaning = type(self).__name__
        return f"{Cleaning}({self.get_id()!r},{self.get_deadline()!r},{self.get_status()!r},{self.get_taskname()!r},{self.__item})"

    def __str__(self):
        return f"Ваш ID: {self.get_id()} Дедлайн: {self.get_deadline()} {self.get_status()} Название: {self.get_taskname()} Комната/предмет: {self.__item}"


class TrainingTask(MainTask):
    __muscle: str

    def __init__(self):
        super().__init__()
        self.__muscle = None

    def set_muscle(self):
        self.__muscle = training_muscle()

    def get_muscle(self):
        return self.__muscle

    def set_task_parameters():
        launch = TrainingTask()
        launch.set_taskname()
        launch.set_muscle()
        try:
            deadline = user_set_deadline()
            launch.set_deadline(deadline)
        except ValueError:
            print(
                "Вводить надо только дату,автоматически установлена текущая время и дата"
            )
            deadline = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            launch.set_deadline(deadline)
        launch.set_status(1)
        task_dict[launch.get_id()] = launch
        print("Запомните ID вашей задачи!", launch.get_id())
        TaskManagerTable.create(id_task = launch.get_id(),task_table_type = "Тренировка",task_table_name = launch.get_taskname(),task_table_deadline = launch.get_deadline(),
                                task_table_status = launch.get_status(),task_table_item = launch.get_muscle())
    def __repr__(self):
        Training = type(self).__name__
        return f"{Training}({self.get_id()!r},{self.get_deadline()!r},{self.get_status()!r},{self.get_taskname()!r},{self.__muscle})"

    def __str__(self):
        return f"Ваш ID: {self.get_id()} Дедлайн: {self.get_deadline()} {self.get_status()} Название: {self.get_taskname()} Группа мышц: {self.__muscle}"


class HomeworkTask(MainTask):
    __study: str

    def __init__(self):
        super().__init__()
        self.__study = None

    def set_study(self):
        self.__study = homework()

    def get_study(self):
        return self.__study

    def set_task_parameters():
        launch = HomeworkTask()
        launch.set_taskname()
        launch.set_study()
        try:
            deadline = user_set_deadline()
            launch.set_deadline(deadline)
        except ValueError:
            print(
                "Вводить надо только дату,автоматически установлена текущая время и дата"
            )
            deadline = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            launch.set_deadline(deadline)
        launch.set_status(1)
        task_dict[launch.get_id()] = launch
        print("Запомните ID вашей задачи!", launch.get_id())
        TaskManagerTable.create(id_task = launch.get_id(),task_table_type = "Учёба",task_table_name = launch.get_taskname(),task_table_deadline = launch.get_deadline(),
                                task_table_status = launch.get_status(),task_table_item = launch.get_study())
    def __repr__(self):
        Student = type(self).__name__
        return f"{Student}({self.get_id()!r},{self.get_deadline()!r},{self.get_status()!r},{self.get_taskname()!r},{self.__study})"

    def __str__(self):
        return f"Ваш ID: {self.get_id()} Дедлайн: {self.get_deadline()} {self.get_status()} Название: {self.get_taskname()} Группа мышц: {self.__study}"


def one_more_task():
    one_more_task = input("Хотите создать еще одну задачу?(д = да/н = нет)")
    if one_more_task == "д":
        create_task()
    else:
        CRUDoperations()


def create_task():
    launch = task_type_by_class()
    if launch == 1:
        CleaningTask.set_task_parameters()
        one_more_task()
    elif launch == 2:
        TrainingTask.set_task_parameters()
        one_more_task()
    elif launch == 3:
        HomeworkTask.set_task_parameters()
        one_more_task()


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
        change = type(task_dict[change_task_by_id])
        change.set_task_parameters()

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
            test = TaskManagerTable.select()
            test_selected = test.dicts().execute()
            for test in test_selected:
                print("тест: ", test)
        else:
            key.set_status(1)
            print(key)
            test = TaskManagerTable.select()
            print(test)

while True:
    if __name__ == "__main__":
        main()
    CRUDoperations()
    
    try:
        connection = psycopg2.connect(
        host="127.0.0.1", user="admin", password="root", dbname="postgres"
    )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            print(cursor.fetchone())

        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO task_manager (task_type) VALUES ('launch') """)

    except Exception as _ex:
        print("[INFO] Ошибка при работе с Базой данных", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] Соединение с Базой данных закрыто.")
