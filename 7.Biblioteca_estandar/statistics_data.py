import statistics
import csv

monthly_sales = {}
#Leer datos de un archivo CSV
with open('curso_de_python/7.Biblioteca_estandar/monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(f"Sales: {sales}")

#Calcular el promedio
average = statistics.mean(sales)
print(f"Average: {average}")

#Calcular la mediana
median = statistics.median(sales)
print(f"Median: {median}")

#Calcular el desvío estándar
standard_deviation = statistics.stdev(sales)
print(f"Standard Deviation: {standard_deviation}")

#Calcular la varianza
variance = statistics.variance(sales)
print(f"Variance: {variance}")

#Calcular la moda
mode = statistics.mode(sales)
print(f"Mode: {mode}")