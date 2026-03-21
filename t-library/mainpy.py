# %%
import json as j
import sys

# %%


def load():

    try:
        with open("book.json", "r", encoding="utf-8") as a:
            library = j.load(a)

    except:
        with open("book.json", "w", encoding="utf-8") as a:
            j.dump([], a, ensure_ascii=False, indent=4)
        return []

    return library


library = load()

# %%


def add_save(library, book):

    if library == []:
        book["id"] = 0
    else:
        book["id"] = library[-1]["id"] + 1

    library.append(book)

    with open("book.json", "w", encoding="utf-8") as a:
        j.dump(library, a, ensure_ascii=False, indent=4)

# %%


def save_book(library, book):

    for i, book1 in enumerate(library):
        if book1.get("id") == book.get("id"):
            library[i] = book

    with open("book.json", "w", encoding="utf-8") as a:
        j.dump(library, a, ensure_ascii=False, indent=4)

# %%


def save_all(library):
    with open("book.json", "w", encoding="utf-8") as f:
        j.dump(library, f, ensure_ascii=False, indent=4)

# %%


def add_book():

    print("""
          --- Добавление новой книги ---
          """)

    while True:
        name = input("Введите название книги: ")
        if name != "":
            break
        else:
            print("""
                      Название не может быть пустым. Повторите ввод
                      """)

    print("""
          Для пропуска одного из следующих пунктов нажмите Enter
          """)

    author = input("Введите автора:")
    if author == "":
        author = "(не указан)"

    genre = input("Введите жанр:")
    if genre == "":
        genre = "(не указан)"

    while True:
        year = input("Введите год издания:")
        if year == "":
            year = "(не указан)"
            break
        else:
            try:
                year = int(year)
                break
            except:
                print("""
                      Год издания должен быть числом, повторите ввод
                      """)

    desc = input("Введите краткое описание:")
    if desc == "":
        desc = "(не указано)"

    print("""
          Вы ввели следующие данные:
          """)

    print("Название: " + name)
    print("Автор: " + author)
    print("Жанр: " + genre)
    print("Год издания: " + str(year))
    print("Описание: " + desc)

    print("""
          Сохранить? 
          
          1. Да
          2. Нет
          """)

    while True:
        a = input("Ваш выбор: ")
        if a == "1":
            break
        elif a == "2":
            return
        else:
            print("""
                Выберите один из вариантов
                """)

    book = {"id": None,
            "Название": name,
            "Автор": author,
            "Жанр": genre,
            "Год издания": year,
            "Краткое описание": desc,
            "Статус": False,
            "Избранное": False}

    add_save(library, book)

# %%


def year_key(book):

    try:
        return int(book.get("Год издания"))
    except:
        return float("inf")

# %%


def sort_filt(library):

    print("""
          Как показать книги?
          
          1. Все книги (без сортировки)
          2. Сортировать по названию
          3. Сортировать по автору
          4. Сортировать по году
          5. Фильтр по жанру
          6. Фильтр по статусу (прочитана/не прочитана)
          0. Главное меню
          """)

    while True:
        a = input("Ваш выбор: ")
        if a == "1" or a == "2" or a == "3" or a == "4" or a == "0" or a == "5" or a == "6":
            break
        else:
            print("""
              Выберите один из вариантов
              """)

    if a == "0":
        return

    elif a == "1":
        books = library

    elif a == "2":
        books = sorted(library, key=lambda q: q.get("Название").lower())

    elif a == "3":
        books = sorted(library, key=lambda q: q.get("Автор").lower())

    elif a == "4":
        books = sorted(library, key=year_key)

    elif a == "5":
        g = input("Введите жанр: ")
        books = []
        for book in library:
            if book.get("Жанр") == g:
                books.append(book)
        if books == []:
            print("""
              Вы еще не добавили книги этого жанра
              """)

    elif a == "6":
        books = []
        for book in library:
            if book.get("Статус") == True:
                books.append(book)
        if books == []:
            print("""
              "Вы еще не добавили книги в 'Прочитанное'
              """)

    display_books(books)

# %%


def search(library):

    res = None
    search = input("Введите название, автора или ID книги:").strip().lower()

    for book in library:
        if str(book.get("id")) == search or book.get("Название").strip().lower() == search or book.get("Автор").strip().lower() == search:
            res = book
            break

    if res == None:
        print("""
            Книга не найдена
            """)
    else:
        print("""
            Найдена книга:
            """)
        print(f"ID: {res.get("id")}")
        print(f"Название: {res.get("Название")}")
        print(f"Автор: {res.get("Автор")}")
        print(f"Жанр: {res.get("Жанр")}")
        print(f"Год издания: {res.get("Год издания")}")
        print(f"Краткое описание: {res.get("Краткое описание")}")
        print(
            f"Статус: {"Прочитана" if res.get("Статус") else "Не прочитана"}")
        print(f"Избранное: {"Да" if res.get("Избранное") else "Нет"}")
        print("""
            ----------------------------------------
            """)
    return res

# %%


def add_fav(library):

    res = search(library)
    if res == None:
        return
    else:
        print("""
            Выберите действие:
              
            1. Добавить в избранное
            2. Убрать из избранного
            0. Главное меню
            """)

        while True:
            a = input("Ваш выбор: ")
            if a == "1" or a == "2" or a == "0":
                break
            else:
                print("""
                         Выберите один из вариантов
                        """)

        if a == "0":
            return
        elif a == "1":
            res["Избранное"] = True
        elif a == "2":
            res["Избранное"] = False

        save_book(library, res)

# %%


def status(library):

    res = search(library)
    if res == None:
        return
    else:
        print("""
            Выберите действие:
              
            1. Изменить статус на 'Прочитанно'
            2. Изменить статус на 'Не прочитанно'
            0. Главное меню
            """)

        while True:
            a = input("Ваш выбор: ")
            if a == "1" or a == "2" or a == "0":
                break
            else:
                print("""
                         Выберите один из вариантов
                        """)

        if a == "0":
            return
        elif a == "1":
            res["Статус"] = True
        elif a == "2":
            res["Статус"] = False

        save_book(library, res)

# %%


def display_books(library):

    if library == []:
        print("""
              Вы пока не добавили книг
              """)
        return
    print(f""" 
          --- Список книг (Всего {len(library)} книг) --- 
          """)

    for book in library:
        print(f"ID: {book.get("id")}")
        print(f"Название: {book.get("Название")}")
        print(f"Автор: {book.get("Автор")}")
        print(f"Жанр: {book.get("Жанр")}")
        print(f"Год издания: {book.get("Год издания")}")
        print(f"Краткое описание: {book.get("Краткое описание")}")
        print(
            f"Статус: {"Прочитана" if book.get("Статус") else "Не прочитана"}")
        print(f"Избранное: {"Да" if book.get("Избранное") else "Нет"}")
        print("""
              ----------------------------------------
              """)

    print("""
          Выберите действие:
          
          1. Отсортировать/отфильтровать
          2. Поменять статус
          3. Добавить/убрать из избранного
          0. Главное меню
          """)

    while True:
        a = input("Ваш выбор: ")
        if a == "1" or a == "2" or a == "3" or a == "0":
            break
        else:
            print("""
              Выберите один из вариантов
              """)

    if a == "0":
        return
    elif a == "1":
        sort_filt(library)
    elif a == "3":
        add_fav(library)
    elif a == "2":
        status(library)

# %%


def fav(library):

    books = []
    for book in library:
        if book.get("Избранное") == True:
            books.append(book)
    if books == []:
        print("""
            "Вы еще не добавили книги в 'Избранное'
            """)

    print(f""" 
          --- Список книг (Всего {len(books)} книг) --- 
          """)

    for book in books:
        print(f"ID: {book.get("id")}")
        print(f"Название: {book.get("Название")}")
        print(f"Автор: {book.get("Автор")}")
        print(f"Жанр: {book.get("Жанр")}")
        print(f"Год издания: {book.get("Год издания")}")
        print(f"Краткое описание: {book.get("Краткое описание")}")
        print(
            f"Статус: {"Прочитана" if book.get("Статус") else "Не прочитана"}")
        print(f"Избранное: {"Да" if book.get("Избранное") else "Нет"}")
        print("""
              ----------------------------------------
              """)

# %%


def delete(library):

    del_book = search(library)

    print(""" 
          Вы уверены, что хотите удалить эту книгу?
          
          1. Да
          2. Нет
          """)

    while True:
        a = input("Ваш выбор: ")
        if a == "1" or a == "2":
            break
        else:
            print("""
              Выберите один из вариантов
              """)

    if a == "1":
        library.remove(del_book)
        save_all(library)
    elif a == "2":
        return

# %%


def gmenu(library):

    print("""
    ========================================
         Добро пожаловать в Т-Библиотеку!
    ========================================
        """)

    print("""
          Выберите действие:
          
        1. Добавить книгу
        2. Показать все книги
        3. Найти книгу
        4. Мои избранные книги
        5. Удалить книгу
        0. Выйти из программы
        
----------------------------------------
        
          """)
    while True:
        a = input("Ваш выбор: ")
        if a == "1" or a == "2" or a == "3" or a == "4" or a == "0" or a == "5":
            break
        else:
            print("""
              Выберите один из вариантов
              """)

    if a == "1":
        add_book()
    elif a == "0":
        sys.exit()
    elif a == "2":
        display_books(library)
    elif a == "3":
        search(library)
    elif a == "4":
        fav(library)
    elif a == "5":
        delete(library)


while True:
    library = load()
    gmenu(library)
