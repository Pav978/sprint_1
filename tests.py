from main import BooksCollector
import unittest

class BooksCollectorTest(unittest.TestCase):
# 1 тест "Метод добавляет новую книгу"
    def test_add_new_book(self):
        books_collector = BooksCollector()
        books_collector.add_new_book("Буратино")
        self.assertIn("Буратино", books_collector.get_books_genre())

# 2 тест "Метод установливает жанр для книги"
    def test_set_book_genre(self):
        books_collector = BooksCollector()
        books_collector.add_new_book("Чиполино")
        books_collector.set_book_genre("Чиполино", "Фантастика")
        self.assertEqual(books_collector.get_book_genre("Чиполино"), "Фантастика")
# 3 тест "Метод выводит жанр книги по ее имени"

    def test_get_book_genre(self):
        books_collector = BooksCollector()
        books_collector.add_new_book("Образец")
        books_collector.set_book_genre("Образец", "Фантастика")
        self.assertEqual(books_collector.get_book_genre("Образец"), "Фантастика")

# 4 тест "Метод выводит список книг с опредленным жанром"
    def test_get_books_with_specific_genre(self):
        books_collector = BooksCollector()
        books_collector.add_new_book("Звездные войны")
        books_collector.add_new_book("Чужой")
        books_collector.set_book_genre("Звездные войны", "Фантастика")
        books_collector.set_book_genre("Чужой", "Ужасы")
        self.assertEqual(books_collector.get_books_with_specific_genre("Фантастика"), ["Звездные войны"])
        self.assertEqual(books_collector.get_books_with_specific_genre("Ужасы"), ["Чужой"])

# 5 тест "Метод выводит текущий словарь books_genre"
    def test_get_books_genre(self):
        books_collector = BooksCollector()
        books_collector.add_new_book("Тайна 3 планеты")
        books_collector.add_new_book("Кошмар")
        books_collector.set_book_genre("Тайна 3 планеты", "Фантастика")
        books_collector.set_book_genre("Кошмар", "Ужасы")
        self.assertEqual(books_collector.get_books_genre(), {"Тайна 3 планеты": "Фантастика", "Кошмар": "Ужасы"})

# 6 тест "Метод возвращает книги, которые подходят детям"
    def test_get_books_for_children(self):
        books_collector = BooksCollector()
        books_collector.add_new_book("Гостья из будущего")
        books_collector.add_new_book("Дети кукурузы")
        books_collector.set_book_genre("Гостья из будущего", "Фантастика")
        books_collector.set_book_genre("Дети кукурузы", "Ужасы")
        self.assertEqual(books_collector.get_books_for_children(), ["Гостья из будущего"])
# 7 тест "Метод добавляет книгу в избранное"
    def test_add_book_in_favorites(self):
        books_collector = BooksCollector()
        books_collector.add_new_book("Любимая книга")
        books_collector.add_book_in_favorites("Любимая книга")
        self.assertIn("Любимая книга", books_collector.get_list_of_favorites_books())

# 8 тест "Метод удаляет книгу из избранного"
    def test_delete_book_from_favorites(self):
        books_collector = BooksCollector()
        books_collector.add_new_book("Уже не любимая книга")
        books_collector.add_book_in_favorites("Уже не любимая книга")
        books_collector.delete_book_from_favorites("Уже не любимая книга")
        self.assertNotIn("Уже не любимая книга", books_collector.get_list_of_favorites_books())

# 9 тест "Метод выводит список избранных книг"
    def test_get_list_of_favorites_books(self):
        books_collector = BooksCollector()
        books_collector.add_new_book("Хорошая книга")
        books_collector.add_new_book("Лучшая книга")
        books_collector.add_book_in_favorites("Хорошая книга")
        books_collector.add_book_in_favorites("Лучшая книга")
        self.assertEqual(books_collector.get_list_of_favorites_books(), ["Хорошая книга", "Лучшая книга"])

    # негативные тесты

# 10 тест проверка пустого названия книги
    def test_add_new_book_with_empty_name(self):
        books_collector = BooksCollector()
        books_collector.add_new_book("")
        self.assertNotIn("", books_collector.get_books_genre())

# 11 тест проверка длинного названия книги
    def test_add_new_book_with_long_name(self):
        books_collector = BooksCollector()
        long_name = "К" * 41
        self.assertNotIn(long_name, books_collector.get_books_genre())

# 12 тест проверка несуществующего жанра
    def test_set_book_genre_with_incorrect_genre(self):
        books_collector = BooksCollector()
        books_collector.add_new_book("Каламбур")
        books_collector.set_book_genre("Калабур", "Несуществующий жанр")
        self.assertEqual(books_collector.get_book_genre("Каламбур"), None)
