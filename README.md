Реализованно 14 тестов.
Из них 10 позитивных:
1. (FAILED )test_add_new_book_add_two_books - добавление 2-х новых книг
2. (PASSED) test_add_new_book - добавление новой книги
3. (PASSED) test_set_book_genre - установление жанра книги, если книга есть в books_genre ее жанр входи в список genre
4. (PASSED) test_get_book_genre - вывод жанра книги по ее названию
5. (PASSED) test_get_books_with_specific_genre - вывод списка книг с опредленным жанром
6. (PASSED) test_get_books_genre - вывод текущего словаря books_genre
7. (PASSED) test_get_books_for_children - возврат книг, которые подходят детям
8. (PASSED) test_add_book_in_favorites - добавление книги в список избранных
9. (PASSED) test_delete_book_from_favorites - удаление книги из списка избарнных
10. (PASSED) test_get_list_of_favorites_books - вывод списка избранных книг

Из них 4 негативных:
1. (PASSED) test_add_new_book_with_empty_name - добавление пустого ввода в названии книги
2. (PASSED) test_add_new_book_length_name - добавление книги в названии которого 41 символ
3. (FAILED) test_add_new_book_length_name - добавление книги в названии которого 40 символов
4. (PASSED) test_set_book_genre_with_incorrect_genre - установление не существующего жанра для книги