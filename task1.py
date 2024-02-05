import pulp

model = pulp.LpProblem("Maximizing Production", pulp.LpMaximize)

# Визначення змінних
lemonade = pulp.LpVariable("lemonade", lowBound = 0, cat = 'Integer')
juice = pulp.LpVariable("juice", lowBound = 0, cat = 'Integer')

# Функція цілі (максимізація виробництва)
model += lemonade + juice, "Production"

# Додавання обмежень
model += 2 * lemonade + juice <= 100 # Обмеження для Води
model += lemonade <= 50 # Обмеження для Цукру
model += lemonade <= 30 # Обмеження для Лимонного соку
model += 2 * juice <= 40# Обмеження для Фруктового пюре

model.solve()

# Вивід результатів
print(f"Виробляти Лимонаду: {lemonade.varValue} од.")
print(f"Виробляти Фруктового соку: {juice.varValue} од.")