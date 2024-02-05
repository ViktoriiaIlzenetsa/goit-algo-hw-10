import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return 2 * x ** 3 * np.log(x ** 2 + 1)

a = 0  # Нижня межа
b = 1  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.25, 1.25, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = 2 * x^3 * ln(x^2 + 1) від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


def is_inside(x, y):
    return y <= 2 * x ** 3 * np.log(x ** 2 + 1)

def monte_carlo_simulation(a, b, num_experiments):
    """Виконує серію експериментів методом Монте-Карло."""
    average_area = 0

    for _ in range(num_experiments):
        # Генерація випадкових точок
        points = [(random.uniform(a, b), random.uniform(f(a), f(b))) for _ in range(15000)]
        # Відбір точок, що знаходяться всередині трикутника
        inside_points = [point for point in points if is_inside(point[0], point[1])]

        # Розрахунок площі за методом Монте-Карло
        M = len(inside_points)
        N = len(points)
        area = (M / N) * ((b - a) * (f(b) - f(a)))

        # Додавання до середньої площі
        average_area += area

    # Обчислення середньої площі
    average_area /= num_experiments
    return average_area



# Кількість експериментів
num_experiments = 100

# Теоретична площа
result, error = spi.quad(f, a, b)


# Виконання симуляції
average_area = monte_carlo_simulation(a, b, num_experiments)
print(f"Теоретична площа під графіком (with quad): {result}")
print(f"Середня площа під графіком за {num_experiments} експериментів: {average_area}")



