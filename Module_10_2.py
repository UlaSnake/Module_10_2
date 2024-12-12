import threading
import time

# Общее количество врагов
total_enemies = 100


class Knight(threading.Thread):
    def __init__(self, name, power):
        """
        Инициализация рыцаря.

        :param name: Имя рыцаря (строка).
        :param power: Сила рыцаря (целое число).
        """
        super().__init__()  # Инициализация родительского класса Thread
        self.name = name  # Имя рыцаря
        self.power = power  # Сила рыцаря
        self.days = 0  # Счетчик дней сражения

    def run(self):
        """
        Метод, который выполняется при запуске потока.
        Рыцарь сражается с врагами до тех пор, пока они не будут побеждены.
        """
        global total_enemies  # Используем глобальную переменную total_enemies
        print(f"{self.name}, на нас напали!")  # Сообщение о начале битвы

        while total_enemies > 0:  # Пока есть враги
            time.sleep(1)  # Задержка в 1 секунду (1 день сражения)
            self.days += 1  # Увеличиваем счетчик дней сражения

            # Уменьшаем количество врагов на силу рыцаря
            total_enemies -= self.power

            # Выводим информацию о текущем состоянии боя
            if total_enemies < 0:
                total_enemies = 0  # Убедимся, что количество врагов не меньше нуля

            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {total_enemies} воинов.")

        # После победы выводим сообщение о победе
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание экземпляров класса Knight
first_knight = Knight('Sir Lancelot', 10)  # Первый рыцарь с силой 10
second_knight = Knight("Sir Galahad", 20)  # Второй рыцарь с силой 20

# Запуск потоков для обоих рыцарей
first_knight.start()
second_knight.start()

# Ожидание завершения обоих потоков
first_knight.join()
second_knight.join()

# Вывод сообщения об окончании битвы
print("Все битвы закончились!")