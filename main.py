import json
from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


class AddCategory(BaseModel):
    name_category: str = Field(max_length=10, min_length=1, description='Название категория')


class MessageResponse(BaseModel):
    message: str


class ExpenseDict(BaseModel):
    id: int
    name: str = Field(max_length=15, min_length=1, description="Название расхода")
    amount: float = Field(..., ge=0, description='Цена расхода')
    category: str


class ExpensesListResponse(BaseModel):
    expenses: list[ExpenseDict]


class AddExpense(BaseModel):
    name: str = Field(max_length=15, min_length=1, description="Название расхода")
    amount: float = Field(..., ge=0, description='Цена расхода')
    category: str
    add_category: str = Field(default='нет')



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

@app.post("/categories", response_model=MessageResponse)
def add_category(new_category: AddCategory):
    with open('categories.json', 'w') as file:
        categories.append(new_category.name_category)
        json.dump(categories, file, indent=4, ensure_ascii=False)
    return {'message': 'Категория успешно добавлена'}


@app.get('/expenses')
def show_expenses(limit: int = 10, search: str | None = None):
    result = expense_list
    if search:
        if expense_list:
            result = []
            for i in expense_list:
                if search.lower() in i['name'].lower():
                    result.append(i)
            return {'expenses': result[:limit]}
        if not result:
            return {'message': 'Нету такой траты'}
    return {'expenses': result[:limit]}

                

@app.post('/expenses')
def add_expense(expense: AddExpense):
    if expense.category in categories:
        expense_ = {
            'id': get_next_id(),
            'name': expense.name,
            'amount': expense.amount,
            'category': expense.category
        }

        expense_list.append(expense_)
        with open('expenses.json', 'w') as file:
            json.dump(expense_list, file, indent=4, ensure_ascii=False)

        return {'message': 'Данные успешно сохранены'}


    else:
        if expense.add_category == 'нет':
            return {'message': 'Хорошо спасибо'}

        elif expense.add_category == 'да':
            add_category(AddCategory(name_category=expense.category))
            expense_ = {
                'id': get_next_id(),
                'name': expense.name,
                'amount': expense.amount,
                'category': expense.category
            }
            expense_list.append(expense_)
            with open('expenses.json', 'w') as file:
                json.dump(expense_list, file, indent=4, ensure_ascii=False)

            return {'message': 'Категория успешно добавлена'}

        else:
            return {'message': 'Неправильный ввод надо ввести да или нет'}