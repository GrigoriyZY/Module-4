# Домашнее задание по уроку "Пространство имен"

def test_function():

    def inner_function():
        print('Я в области видимости функции test_function')
        return
        
    inner_function()    № Пенес вызов вложенной функции внутрь функции test_function в соответствии с требованиями задачи
    return 


test_function()
# inner_function() - Деактивировал вызов вложенной функции
