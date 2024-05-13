Реализованно 12 тестов.
Из них 9 позитивных:
1. (PASSED) test_add_new_book - добавление новой книги
2. (PASSED) test_set_book_genre - установление жанра книги, если книга есть в books_genre ее жанр входи в список genre
3. (PASSED) test_get_book_genre - вывод жанра книги по ее названию
4. (PASSED) test_get_books_with_specific_genre - вывод списка книг с опредленным жанром
5. (PASSED) test_get_books_genre - вывод текущего словаря books_genre
6. (PASSED) test_get_books_for_children - возврат книг, которые подходят детям
7. (PASSED) test_add_book_in_favorites - добавление книги в список избранных
8. (PASSED) test_delete_book_from_favorites - удаление книги из списка избарнных
9. (PASSED) test_get_list_of_favorites_books - вывод списка избранных книг

Из них 3 негативных:
1. (PASSED) test_add_new_book_with_empty_name - добавление пустого ввода в названии книги
2. (PASSED) test_add_new_book_with_long_name - добавление книги в названии которого более 41 символа
3. (FAILED) test_set_book_genre_with_incorrect_genre - установление не существующего жанра для книги