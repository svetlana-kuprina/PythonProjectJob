# Исходные данные для заполнения таблиц
import csv

import psycopg2

# cur.execute("SET search_path TO student_schema_name;")

with open('customers_data.csv', newline='') as file:
    customers_data = [row for row in csv.reader(file) if 'customer_id' not in row]

with open('employees_data.csv', newline='') as file:
    employees_data = [row for row in csv.reader(file) if 'first_name' not in row]

with open('orders_data.csv', newline='') as file:
    orders_data = [row for row in csv.reader(file) if 'order_id' not in row]

# Импортируйте библиотеку psycopg2

# Создайте подключение к базе данных
conn = psycopg2.connect(
    host="sql_db",
    database="analysis",
    user="simple",
    password="qweasd963"
)

# Открытие курсора
cur = conn.cursor()

# Не меняйте и не удаляйте эти строки - они нужны для проверки
cur.execute("create schema if not exists itresume17837;")
cur.execute("SET search_path TO itresume17837;")
cur.execute("DROP TABLE IF EXISTS orders")
cur.execute("DROP TABLE IF EXISTS customers")
cur.execute("DROP TABLE IF EXISTS employees")


# Ниже напишите код запросов для создания таблиц
cur.execute("CREATE TABLE customers(customer_id varchar(5) PRIMARY KEY, company_name varchar(100) NOT NULL, contact_name varchar(100) NOT NULL);")
cur.execute("CREATE TABLE employees(employee_id int PRIMARY KEY, first_name varchar(25) NOT NULL, last_name varchar(35) NOT NULL, title varchar(100) NOT NULL,  birth_date date NOT NULL, notes text);")
cur.execute("CREATE TABLE orders(order_id int PRIMARY KEY, customer_id varchar(5) REFERENCES customers(customer_id) NOT NULL,  employee_id int REFERENCES employees(employee_id) NOT NULL, order_date date NOT NULL,  ship_city varchar(100) NOT NULL);")

# Зафиксируйте изменения в базе данных
conn.commit()

#Теперь приступаем к операциям вставок данных
# Запустите цикл по списку customers_data и выполните запрос формата
# INSERT INTO itresume3270.table (column1, column2, ...) VALUES (%s, %s, ...) returning ", data)
# В конце каждого INSERT-запроса обязательно должен быть оператор returning

for custom in customers_data:
    cur.execute("INSERT INTO itresume17837.customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)", custom)

cur.execute("SELECT * FROM itresume17837.customers")

# Не меняйте и не удаляйте эти строки - они нужны для проверки
conn.commit()
res_customers = cur.fetchall()


# Запустите цикл по списку employees_data и выполните запрос формата
# INSERT INTO table (column1, column2, ...) VALUES (%s, %s, ...) returning *", data)
# В конце каждого INSERT-запроса обязательно должен быть оператор returning *
n_id = 0
for employees in employees_data:
    n_id = n_id + 1
    employee_id = employees.append( n_id)
    cur.execute("INSERT INTO itresume17837.employees (first_name, last_name, title, birth_date, notes, employee_id) VALUES (%s, %s, %s, %s, %s, %s)", employees)

cur.execute("SELECT * FROM itresume17837.employees")
# Не меняйте и не удаляйте эти строки - они нужны для проверки
conn.commit()
res_employees = cur.fetchall()

# Запустите цикл по списку orders_data и выполните запрос формата
# INSERT INTO table (column1, column2, ...) VALUES (%s, %s, ...) returning *", data)
# В конце каждого INSERT-запроса обязательно должен быть оператор returning *
for orders in orders_data:
    cur.execute(
        "INSERT INTO itresume17837.orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)",
        orders)
cur.execute("SELECT * FROM itresume17837.orders")
# Не меняйте и не удаляйте эти строки - они нужны для проверки
conn.commit()
res_orders = cur.fetchall()

# Закрытие курсора
cur.close()

# Закрытие соединения
conn.close()