def main():
    favorite_fruits = ['apple', 'banana', 'orange']
    print("Favorite fruits:", favorite_fruits)

    favorite_numbers = (7, 11, 42)
    print("Favorite numbers:", favorite_numbers)

    book_info = {
        'title': 'Python Programming',
        'author': 'Guido van Rossum',
        'year_published': 1991
    }

    print("Book information:", book_info)

    favorite_fruits.append('grape')
    print("Updated favorite fruits:", favorite_fruits)

    book_info['year_published'] = 2000
    print("Updated book information:", book_info)

    try:
        favorite_numbers = (5, 11, 42)
    except TypeError as e:
        print("Error occurred while modifying tuple:", e)

if name == "main":
    main()