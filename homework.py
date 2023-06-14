class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type: str,
                 duration: float, distance: float,
                 speed: float, calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


class Training:
    """Базовый класс тренировки."""
    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65
    SEKONDS: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        dist_KM = self.action * self.LEN_STEP / self.M_IN_KM
        return dist_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        spid = self.get_distance() / self.duration
        return spid

    def get_spent_calories(self):
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    COEF_1 = 18
    COEF_2 = 1.79

    def get_spent_calories(self) -> float:
        calory = ((self.COEF_1 * self.get_mean_speed() + self.COEF_2)
                  * self.weight / self.M_IN_KM
                  * (self.duration * self.SEKONDS))
        return calory


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    COEF_1 = 0.035
    M = 100
    COEF_2 = 0.029
    M_S = 0.278
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: int,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        spid_km_h = self.get_mean_speed()
        spid_m_s = spid_km_h * self.M_S
        calories = ((self.COEF_1 * self.weight
                    + (spid_m_s ** 2 / ((self.height / self.M)) * self.COEF_2)
                    * self.weight) * self.duration * self.SEKONDS)
        return calories


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    CONS_1: float = 1.1
    CONS_2: float = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        pool = self.length_pool * self.count_pool
        speed = (pool / self.M_IN_KM) / self.duration
        return speed

    def get_spent_calories(self) -> float:
        calories = ((self.get_mean_speed() + self.CONS_1)
                    * self.CONS_2 * self.weight * self.duration)
        return calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    class_datchic = {'SWM': Swimming,
                     'RUN': Running,
                     'WLK': SportsWalking}
    return class_datchic[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
