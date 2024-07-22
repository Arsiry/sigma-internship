from collections import defaultdict

# Глобальный словарь для подсчета частоты появления сумм
sum_count = defaultdict(int)

def karatsuba(x, y):
    # Базовый случай: если числа маленькие, возвращаем их произведение
    if x < 10 or y < 10:
        return x * y
    
    # Определяем максимальное количество цифр между двумя числами
    n = max(len(str(x)), len(str(y)))
    half_n = n // 2
    
    # Разделяем числа на две части
    high1, low1 = divmod(x, 10**half_n)
    high2, low2 = divmod(y, 10**half_n)
    
    # Рекурсивно считаем три необходимые произведения
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    if z1 == 12:
        print("1")
    z2 = karatsuba(high1, high2)
    
    # Считаем конечный результат
    return (z2 * 10**(2*half_n)) + ((z1 - z2 - z0) * 10**half_n) + z0

def karatsuba1(x, y):
    # Базовый случай: если числа маленькие, возвращаем их произведение
    if x < 10 or y < 10:
        return x * y
    
    # Определяем максимальное количество цифр между двумя числами
    n = max(len(str(x)), len(str(y)))
    half_n = n // 2
    
    # Разделяем числа на две части
    high1, low1 = divmod(x, 10**half_n)
    high2, low2 = divmod(y, 10**half_n)
    
    # Рекурсивно считаем три необходимые произведения
    z0 = karatsuba1(low1, low2)
    z1 = karatsuba1((low1 + high1), (low2 + high2))
    z2 = karatsuba1(high1, high2)
    
    # Вычисляем ad + bc
    ad_bc = z1 - z2 - z0
    sum_count[ad_bc] += 1
    
    # Считаем конечный результат
    return (z2 * 10**(2*half_n)) + ((ad_bc * 10**half_n)) + z0

# Использование функции:
X = 1685287499328328297814655639278583667919355849391453456921116729
Y = 7114192848577754587969744626558571536728983167954552999895348492
result = karatsuba(X, Y)
print(result)
karatsuba1(X, Y)

# Выводим результаты
for s, count in sum_count.items():
    if ((s == 105) or (s == 72) or (s == 12)):
        print(f"Сумма {s} встречается {count} раз(а)")
