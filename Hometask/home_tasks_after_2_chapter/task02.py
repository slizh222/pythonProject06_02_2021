# Ввод суммы объема прожаж
# вывод информации о прибыли от объема продаж

volume_of_sales = int(input("Введите общий объем продаж: "))

# Прибыль обычно составляет 23% от объема продаж
profit = volume_of_sales * 0.23
print("Прибыль,полученная от объема продаж", profit)
