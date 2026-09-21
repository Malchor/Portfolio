import random
import csv


class CoffeeShop:
    def __init__(self, name, max_capacity=10):
        self.name = name
        self.customers = []
        self.max_capacity = max_capacity

    def add_customer(self, customer_name):
        if len(self.customers) >= self.max_capacity:
            raise Exception("Coffee shop is full! Cannot add more customers.")
        if customer_name in self.customers:
            raise Exception(f"{customer_name} is already in the coffee shop.")
        self.customers.append(customer_name)

    def remove_customer(self, customer_name):
        if customer_name not in self.customers:
            raise Exception(f"{customer_name} is not in the coffee shop.")
        self.customers.remove(customer_name)

    def list_customers(self):
        return self.customers


def wc(file_path):
    try:
        with open(file_path, "r") as f:
            text = f.read()

        words = text.split()
        lines = text.split("\n")
        characters = len(text)

        return len(lines), len(words), characters

    except FileNotFoundError:
        return 0, 0, 0


def generate_weather_data(temp_ranges):
    seasons = ["Winter", "Spring", "Summer", "Autumn"]
    data = [["Season", "Day", "Hour", "Temperature"]]

    for season in seasons:
        min_temp, max_temp = temp_ranges[season]

        for day in range(1, 91):
            for hour in range(24):
                temp = random.randint(min_temp, max_temp)
                data.append([season, day, hour, temp])

    return data


def save_weather_to_csv(data, file_name):
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)


class Task:
    def __init__(self, message):
        self._message = message

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, new_message):
        if len(new_message) > 0:
            self._message = new_message


class TaskList:
    def __init__(self):
        self.tasks = []

    def create_new_task(self, message):
        new_task = Task(message)
        self.tasks.append(new_task)

    def get_task_message_by_index(self, index):
        return self.tasks[index].message

    def remove_task_at_index(self, index):
        del self.tasks[index]

    def get_num_tasks(self):
        return len(self.tasks)

    def set_task_message_at_index(self, index, message):
        self.tasks[index].message = message


class Recipe:
    def __init__(self, name, time, steps):
        self.name = name
        self.time = time
        self.steps = steps

    def get_name(self):
        return self.name

    def get_time(self):
        return self.time

    def get_steps(self):
        return self.steps


class RecipeBook:
    def __init__(self):
        self.recipes = []

    def add(self, r):
        self.recipes.append(r)

    def get_all(self):
        return self.recipes


class Laptop:
    def __init__(self, brand, price, ram):
        self.brand = brand
        self.price = price
        self.ram = ram

    def get_price(self):
        return self.price

    def __str__(self):
        return f"{self.brand}-{self.ram}GB-${self.price}"


class GamingLaptop(Laptop):
    def __init__(self, brand, price, ram, gpu):
        super().__init__(brand, price, ram)
        self.gpu = gpu

    def __str__(self):
        return f"{self.brand}-{self.ram}GB-{self.gpu}-${self.price}"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, l):
        self.items.append(l)

    def remove(self, l):
        self.items.remove(l)

    def get_all(self):
        return self.items

    def total(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total
