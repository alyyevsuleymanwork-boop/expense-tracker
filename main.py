import json

categories = ['Food', 'Home']

expense_list=[]

try:
    with open('expenses.json', 'r') as file:
        expense_list = json.load(file)
except FileNotFoundError:
    with open('expenses.json', 'w') as file:
        json.dump(expense_list, file, indent=4, ensure_ascii=False)

def add_expense():
    name = input('Название расхода: ')
    while True:
        try:
            amount = float(input('Сумма: '))
            break
        except ValueError:
            print('Сумма не может быть символом введите число')
    category = input('Категория: ').capitalize()
    if category in categories:
        expense = {
            'name': name,
            'amount': amount,
            'category': category
        }
        expense_list.append(expense)
        with open('expenses.json', 'w') as file:
            json.dump(expense_list, file, indent=4, ensure_ascii=False)
    else:
        question = input('Такой категории нету хотите добавить свою категорию: да/нет: ').capitalize()
        while True:
            if question == 'Нет':
                print('Хорошо спасибо')
                break
            elif question == 'Да':
                add_category()
            else:
                print('Надо написать да или нет')

add_expense()