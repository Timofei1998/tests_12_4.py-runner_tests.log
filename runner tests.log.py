2024-10-02 18:12:13,019 | INFO | "test_challenge" выполнен успешно
2024-10-02 18:12:13,020 | WARNING | Неверный тип данных для объекта Runner
Имя может быть только строкой, передано int
2024-10-02 18:12:13,021 | WARNING | Traceback (most recent call last):
  File "C:\Users\User\PycharmProjects\main.py\module_12\tests_12__4.py", line 83, in test_run
    runner = Runner(2)
             ^^^^^^^^^
  File "C:\Users\User\PycharmProjects\main.py\module_12\tests_12__4.py", line 15, in __init__
    raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
TypeError: Имя может быть только строкой, передано int

2024-10-02 18:12:13,021 | WARNING | Неверная скорость для Runner
Скорость не может быть отрицательной, сейчас -5
2024-10-02 18:12:13,024 | WARNING | Traceback (most recent call last):
  File "C:\Users\User\PycharmProjects\main.py\module_12\tests_12__4.py", line 72, in test_walk
    runner = Runner("Вася", -5)
             ^^^^^^^^^^^^^^^^^^
  File "C:\Users\User\PycharmProjects\main.py\module_12\tests_12__4.py", line 20, in __init__
    raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')
ValueError: Скорость не может быть отрицательной, сейчас -5