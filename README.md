# Модуль фитнес-трекера

## Задача
Разработать программный модуль фитнес-трекера через ООП, который обрабатывает данные для трех видов тренировок: 
для бега, спортивной ходьбы и плавания.

Этот модуль
- принимает от блока датчиков информацию о прошедшей тренировке,
- определяет вид тренировки,
- рассчитывает результаты тренировки,
- выводит информационное сообщение о результатах тренировки.

Информационное сообщение должно включать такую информацию:
- тип тренировки (бег, ходьба или плавание),
- длительность тренировки,
- дистанция, которую преодолел пользователь, в километрах,
- среднюю скорость на дистанции, в км/ч,
- расход энергии, в килокалориях.

## Класс информационного сообщения
```python
class InfoMessage
```
#### Свойства класса
- training_type — тип тренировки,
- duration — длительность тренировки,
- distance — дистанция, преодолённая за тренировку,
- speed — средняя скорость движения,
- calories — потраченные за время тренировки килокалории.


#### Методы класса

- get_message() — метод возвращает строку сообщения.
```python
# выводимое сообщение
# все значения типа float округляются до 3 знаков после запятой
'Тип тренировки: {training_type}; Длительность: {duration} ч.; Дистанция: {distance} км; Ср. скорость: {speed} км/ч; Потрачено ккал: {calories}'.
```


## Базовый класс
```python
class Training
```
#### Свойства класса

- action — количество совершённых действий (число шагов при ходьбе и беге либо гребков — при плавании)
- duration — длительность тренировки
- weight — вес спортсмена
- M_IN_KM = 1000 — константа для перевода значений из метров в километры
- LEN_STEP — расстояние, которое спортсмен преодолевает за один шаг или гребок

#### Методы базового класса
- get_distance() — метод возвращает значение дистанции, преодолённой за тренировку.
```python
# базовая формула расчёта
шаг * LEN_STEP / M_IN_KM
```
- get_mean_speed() — метод возвращает значение средней скорости движения во время тренировки.
```python
# базовая формула расчёта
дистанция / длительность
```
- get_spent_calories() — метод возвращает число потраченных калорий.
- show_training_info() — метод возвращает объект класса сообщения.

## Классы-наследники
### Класс тренировки для бега
```python
class Running
```

#### Методы класса
Переопределяется метод:
- get_spent_calories() — метод возвращает число потраченных калорий.
```python
# формула расчёта
(18 * средняя_скорость – 20) * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах
```
### Класс тренировки спортивной ходьбы
```python
class SportsWalking
```
#### Свойства класса
Добавляются свойства:
- height — рост

#### Методы класса
Переопределяется метод:
* get_spent_calories() — метод возвращает число потраченных калорий.
```python
# формула расчёта
(0.035 * вес + (скорость ** 2 // рост) * 0.029 * вес) * время_тренировки_в_минутах
```

### Класс тренировки в бассейне
```python
class Swimming
```
#### Свойства класса
Добавляются свойства:
- length_pool — длина бассейна;
- count_pool — количество проплытых бассейнов.

#### Методы класса
Переопределяется метод:
- get_mean_speed() — метод возвращает значение средней скорости движения во время тренировки.
```python
# формула расчёта
длина_бассейна * count_pool / M_IN_KM / время_тренировки
```
- get_spent_calories() — метод возвращает число потраченных калорий.
```python
# формула расчёта
(скорость + 1.1) * 2 * вес
```
## Функции модуля
```python
def read_package()
```
- Функция read_package() принимает на вход код тренировки и список её параметров.
- Функция должна определить тип тренировки и создать объект соответствующего класса,
передав ему на вход параметры, полученные во втором аргументе. Этот объект функция должна вернуть.

```python
def main(training)
```
#### Функция `main()` должна принимать на вход экземпляр класса `Training`.

- При выполнении функции `main()`для этого экземпляра должен быть вызван метод `show_training_info()`;
результатом выполнения метода должен быть объект класса `InfoMessage`, его нужно сохранить в переменную `info`.
- Для объекта `InfoMessage`, сохранённого в переменной `info`, должен быть вызван метод,
который вернёт строку сообщения с данными о тренировке; эту строку нужно передать в функцию `print()`.

## Технологии
- Python 3.9
## Авторы
Лайшев Марат
