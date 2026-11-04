import json


categories = ['Food', 'Home']


expense_list=[]


try:
    with open('expenses.json', 'r') as file:
        expense_list = json.load(file)
except FileNotFoundError:
    with open('expenses.json', 'w') as file:
        json.dump(expense_list, file, indent=4, ensure_ascii=False)


try:
    with open('categories.json', 'r') as file:
        categories = json.load(file)
except FileNotFoundError:
    with open('categories.json', 'w') as file:
        json.dump(categories, file, indent=4, ensure_ascii=False)


def get_next_id():

    ids = []

    for expense in expense_list:
        ids.append(expense['id'])

    if ids:
        return max(ids) + 1 

    else:
        return 1

def add_category(category):
    with open('categories.json', 'w') as file:
        categories.append(category)
        json.dump(categories, file, indent=4, ensure_ascii=False)
    print('Категория успешно добавлена')


def show_expenses():
    print('==== Мои расходи =====')
    if expense_list:
        for i in expense_list:
            print(f"ID: {i['id']}")
            print(f'Название: {i['name']}')
            print(f'Сумма: {i['amount']}')
            print(f'Категория: {i['category']}')
            print()


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
            'id': get_next_id(),
            'name': name,
            'amount': amount,
            'category': category
        }


        expense_list.append(expense)
        with open('expenses.json', 'w') as file:
            json.dump(expense_list, file, indent=4, ensure_ascii=False)

    else:

        while True:
            question = input('Такой категории нету хотите добавить свою категорию: да/нет: ').capitalize()
            if question == 'Нет':
                print('Хорошо спасибо')
                break

            elif question == 'Да':
                add_category(category)
                expense = {
                    'id': get_next_id(),
                    'name': name,
                    'amount': amount,
                    'category': category
                }

                expense_list.append(expense)
                with open('expenses.json', 'w') as file:
                    json.dump(expense_list, file, indent=4, ensure_ascii=False)
                break

            else:
                print('Надо написать да или нет')

while True:
    print('1. Добавить расход')
    print('2. Добавить категорию')
    print('3. Посмотреть список трат')
    print('4. Выход')
    print()

    while True:
        try:
            choice2 = int(input('Выберите действие которую хотите выполнить: '))
            break
        except ValueError:
            print('Выбор должен быть числом')


    if choice2 == 1:
        add_expense()


    elif choice2 == 2:
        category = input('Введите название новой категории: ')
        add_category(category)


    elif choice2 == 3:
        show_expenses()


    elif choice2 == 4:
        print('Спасибо за использвание нашим приложением')
        break


    else:
        print('Выберите действие из списка')