import fileinput
text = input('Введите текст: ')

def file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)
    return 'Текст записан в файл'

def app_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text)
    return 'Текст добавлен в файл+'

text = input('Введите текст: ')
result = file('exapmle2.txt', text)
print(result)

text = input('Введите текст: ')
result = app_file('User_text', text)
print(result)
fileinput.close()
