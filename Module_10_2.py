import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power, enemies):
        """
        Инициализация рыцаря.

        :param name: Имя рыцаря (строка).
        :param power: Сила рыцаря (целое число).
        :param enemies: Количество врагов, с которыми будет сражаться рыцарь (целое число).
        """
        super().__init__()  # Инициализация родительского класса Thread
        self.name = name  # Имя рыцаря
        self.power = power  # Сила рыцаря
        self.enemies = enemies  # Количество врагов
        self.days = 0  # Счетчик дней сражения

    def run(self):
        """
        Метод, который выполняется при запуске потока.
        Рыцарь сражается с врагами до тех пор, пока они не будут побеждены.
        """
        print(f"{self.name}, на нас напали!")  # Сообщение о начале битвы

        while self.enemies > 0:  # Пока есть враги у текущего рыцаря
            time.sleep(1)  # Задержка в 1 секунду (1 день сражения)
            self.days += 1  # Увеличиваем счетчик дней сражения

            # Уменьшаем количество врагов на силу рыцаря
            self.enemies -= self.power

            # Выводим информацию о текущем состоянии боя
            if self.enemies < 0:
                self.enemies = 0  # Убедимся, что количество врагов не меньше нуля

            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")

        # После победы выводим сообщение о победе
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание экземпляров класса Knight с разным количеством врагов
first_knight = Knight('Sir Lancelot', 10, 100)  # Первый рыцарь с силой 10 и 100 врагами
second_knight = Knight("Sir Galahad", 20, 100)  # Второй рыцарь с силой 20 и 100 врагами

# Запуск потоков для обоих рыцарей
first_knight.start()
second_knight.start()

# Ожидание завершения обоих потоков
first_knight.join()
second_knight.join()

# Вывод сообщения об окончании битвы
print("Все битвы закончились!")