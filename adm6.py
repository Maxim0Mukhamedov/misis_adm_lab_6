# Мухамедов Максим, БПМ-22-1 

import random

def random_permutation(string):
  """
  Функция генерирует случайную перестановку по введенной строке.

  Args:
    string: Строка, для которой генерируется перестановка.

  Returns:
    Случайная перестановка.
  """
  characters = list(string)

  for i in range(len(characters)):
    # Выбираем случайный индекс j в диапазоне [i, len(characters) - 1].
    j = random.randint(i, len(characters) - 1)

    # Меняем местами элементы characters[i] и characters[j].
    characters[i], characters[j] = characters[j], characters[i]

  return ''.join(characters)

# Пример использования.
print("Введите строку: ")
string = input()
random_permutation = random_permutation(string)
print("Случайная перестановка: ")
print(random_permutation)
