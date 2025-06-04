#2
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def inscribe_square(self, square):
        return 2 * self.radius == square.side

class Square:
    def __init__(self, side):
        self.side = side

    def inscribe_triangle(self, triangle):
        required_side = (triangle.side * math.sqrt(3)) / (2 + math.sqrt(3))
        return math.isclose(self.side, required_side, rel_tol=1e-9)

class Triangle:
    def __init__(self, side):
        self.side = side

def check_inscription(circle, square, triangle):
    return circle.inscribe_square(square) and square.inscribe_triangle(triangle)


triangle_side = float(input("Введите сторону треугольника: "))
square_side = float(input("Введите сторону квадрата: "))
circle_radius = float(input("Введите радиус круга: "))

triangle = Triangle(triangle_side)
square = Square(square_side)
circle = Circle(circle_radius)

if check_inscription(circle, square, triangle):
    print("Да")
else:
    print("Нет")

#3
def bmi_category(bmi, age, gender):
    if age < 18:
        return "Для детей и подростков используйте перцентильные таблицы."
    elif age >= 65:
        if bmi < 24:
            return "Возможен дефицит массы тела. Рекомендуется консультация врача."
        elif 24 <= bmi <= 29:
            return "Норма для пожилого возраста."
        else:
            return "Избыточный вес. Обратитесь к врачу."
    else:
        if bmi < 16.5:
            return "Выраженный дефицит массы тела. Требуется врачебная помощь."
        elif 16.5 <= bmi < 18.5:
            return "Недостаточная масса тела. Рекомендуется питание богатое белками и углеводами."
        elif 18.5 <= bmi < 25:
            return "Норма. Поддерживайте текущий режим."
        elif 25 <= bmi < 30:
            if gender == 'М' and age < 40:
                return "Избыточный вес. Рекомендуется спорт и коррекция питания."
            else:
                return "Избыточный вес. Умеренная диета и физическая активность."
        else:
            return "Ожирение. Необходима консультация врача и диетолога."


weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (м): "))
age = int(input("Введите возраст: "))
gender = input("Введите пол (М/Ж): ").upper()
bmi = weight / (height ** 2)
print(f"Ваш ИМТ: {round(bmi, 1)}")
print(bmi_category(bmi, age, gender))

#4
zoos = {
    "Зоопарк 1": {
        "Львы": 5,
        "Тигры": 3,
        "Жирафы": 6
    },
    "Зоопарк 2": {
        "Львы": 2,
        "Тигры": 6,
        "Жирафы": 1
    },
    "Зоопарк 3": {
        "Львы": 3,
        "Тигры": 1,
        "Жирафы": 8
    }
}

print("Информация по зоопаркам:")
for zoo, animals in zoos.items():
    total = sum(animals.values())
    print(f"{zoo}:")
    for animal, count in animals.items():
        print(f"  {animal}: {count}")
    print(f"  Всего животных: {total}")

print("Зоопарки с наибольшим количеством животных каждого вида:")
species = set()
for animals in zoos.values():
    species.update(animals.keys())

for animal in species:
    max_count = 0
    max_zoo = ""
    for zoo, animals in zoos.items():
        if animal in animals and animals[animal] > max_count:
            max_count = animals[animal]
            max_zoo = zoo
    print(f"{animal}: {max_zoo} ({max_count} особей)")

#5
friendly_pairs = []
for a in range(200, 301):
    sum_a = 0
    for i in range(1, a):
        if a % i == 0:
            sum_a += i
    if sum_a > a and sum_a <= 300:
        sum_b = 0
        for i in range(1, sum_a):
            if sum_a % i == 0:
                sum_b += i
        if sum_b == a:
            friendly_pairs.append((a, sum_a))
for pair in friendly_pairs:
    print(*pair)

#6
start, end = map(int, input().split())
print([x for x in range(start, end+1) if str(x) == str(x)[::-1]])

#7
from random import *

arr = [randint(-100, 100) for _ in range(10)]
count = 0
print(arr)
for i in range(1, len(arr) - 1):
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        count += 1
print(count)

#8
bin_number = input("Введите двоичное число: ")
print(f'Двоичное число: {bin_number}\nДесятичное число {int(bin_number, 2)}')

#9
class Car:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power
    def __str__(self):
        return f'Автомобиль: {self.brand} {self.model}, {self.power} л.с.'


cars = [
    Car("BMW", "X3", 190),
    Car("Audi", "Q3", 211),
    Car("Mercedes-Benz", "GLE", 381)
]

max_power = None
for car in cars:
    print(car)
    if max_power is None or car.power > max_power.power:
        max_power = car
print(f'Самый мощный автомобиль: {max_power.brand} {max_power.model} с мощностью {max_power.power} л.с.')

#10
import math

class Shape:
    @staticmethod
    def square(shape_type, *args):
        if shape_type == "треугольник":
            a, b, c = args
            p = (a + b + c) / 2
            return math.sqrt(p * (p - a) * (p - b) * (p - c))  # Формула Герона
        elif shape_type == "прямоугольник":
            a, b = args
            return a * b
        elif shape_type == "круг":
            r = args[0]
            return math.pi * r ** 2
        else:
            return "Неизвестная фигура"

    @staticmethod
    def perimeter(shape_type, *args):
        if shape_type == "треугольник":
            return sum(args)
        elif shape_type == "прямоугольник":
            a, b = args
            return 2 * (a + b)
        elif shape_type == "круг":
            r = args[0]
            return 2 * math.pi * r
        else:
            return "Неизвестная фигура"


shape_type = input("Фигура треугольник/прямоугольник/круг: ")
action = input("Вычислить площадь/периметр: ")
if shape_type == "треугольник":
    a, b, c = map(float, input("Введите 3 стороны через пробел: ").split())
    args = (a, b, c)
elif shape_type == "прямоугольник":
    a, b = map(float, input("Введите длину и ширину через пробел: ").split())
    args = (a, b)
elif shape_type == "круг":
    r = float(input("Введите радиус: "))
    args = (r,)

if action == "площадь":
    print(f"Площадь {shape_type}а: {Shape.square(shape_type, *args)}")
elif action == "периметр":
    print(f"Периметр {shape_type}а: {Shape.perimeter(shape_type, *args)}")

#11
class Students:
    def __init__(self, full_name, birth_year, admission_year, math_grades, physics_grades, inf_grades):
        self.full_name = full_name
        self.birth_year = birth_year
        self.admission_year = admission_year
        self.math_grades = math_grades
        self.physics_grades = physics_grades
        self.inf_grades = inf_grades
    
    def age(self, current_year=2023):
        return current_year - self.birth_year
    
    def course(self, current_year=2023):
        return current_year - self.admission_year + 1  # +1 потому что первый год - это первый курс
    
    def average_grade(self):
        total_grades = self.math_grades + self.physics_grades + self.inf_grades
        return sum(total_grades) / len(total_grades)
    
    def student_data(self):
        age = self.age()
        course = self.course()
        avg_grade = self.average_grade()
        return f"{self.full_name}, {age} лет, {course} курс, средний балл: {avg_grade:.2f}"


def write_to_file(students, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for student in students:
            file.write(student.student_data() + '\n')


students = [
    Students("Иванов Иван Иванович", 2000, 2020, [4, 5, 4, 5], [3, 4, 5, 4], [5, 5, 5, 5]),
    Students("Петров Петр Петрович", 2001, 2021, [3, 4, 3, 4], [4, 4, 5, 4], [4, 3, 4, 5]),
    Students("Сидорова Анна Михайловна", 1999, 2019, [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5])
]
write_to_file(students, "students.txt")
