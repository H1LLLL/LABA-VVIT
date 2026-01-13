class Book:
    title = None
    author = None
    year = None
Vvit = Book()
Vvit.title = 'Vvit'
Vvit.author = 'Artem Evgenych'
Vvit.year = 1999
def get_info():
    return f'''Название книги: {Vvit.title}.\n Автор: {Vvit.author}.\n Год издания: {Vvit.year}.'''
print(get_info())
