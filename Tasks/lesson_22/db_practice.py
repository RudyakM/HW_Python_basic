import os
import sqlite3

from typing import List, Set


def execute_query(query_sql: str) -> List:
    '''
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    '''
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql)
    return result


def unwrapper(records: List) -> None:
    '''
    Функция для вывода результата выполнения запроса
    :param records: список ответа БД
    '''
    for record in records:
        print(*record)


def get_employees() -> None:
    '''
    Функция получения всех записей из таблицы employees
    '''
    query_sql = '''
        SELECT *
            FROM customers
            WHERE State = "SP"
              AND City = "São Paulo"
        ;
    '''
    result = execute_query(query_sql)
    unwrapper(result)


def get_filter_customers(state=None, city=None) -> None:
    query_sql = '''
    SELECT *
        FROM customers
    '''
    filter = ''
    if state and city:
        filter += f"\tWHERE State = '{state}'\n\tAND City = '{city}'"
    elif state:
        filter += f"\tWHERE State = '{state}'"
    elif city:
        filter += f"\tWHERE City = '{city}'"
    query_sql += filter
    result = execute_query(query_sql)
    unwrapper(result)


def get_unique_customers() -> Set:
    query_sql = '''
    SELECT FirstName
        FROM customers
    '''
    names = list(execute_query(query_sql))
    unique_names = set()
    for name in names:
        unique_names.add(name[0])
    return len(unique_names)


def get_unique_customers_by_sql() -> Set:
    query_sql = '''
    SELECT count(distinct FirstName)
        FROM customers
    '''

    unique_names_qty = list(execute_query(query_sql))[0][0]
    return unique_names_qty


def get_profit() -> None:
    query_sql = '''
    SELECT UnitPrice, Quantity
        FROM invoice_items
    '''
    data = list(execute_query(query_sql))
    result = []
    for profit in data:
        price, quantity = profit[0], profit[1]
        result.append(price * quantity)
    return result


def get_repeat_name() -> Set:
    query_sql = '''
    SELECT FirstName
        FROM customers
    '''
    names = list(execute_query(query_sql))
    repeat_names = [name[0] for i, name in enumerate(names) if i != names.index(name)]
    return repeat_names


result = get_repeat_name()
print(result)
#get_filter_customers("SP", "São Paulo")
# get_employees()