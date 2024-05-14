import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:
# тест № 1- добавление 2-х новых книг
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

# тест №2 - добавление новой книги
    def test_add_new_book(self, collector):
        collector.add_new_book("Буратино")
        assert "Буратино" in collector.get_books_genre()
# тест №3 - установление жанра книги, если книга есть в books_genre ее жанр входи в список genre
    def test_set_book_genre(self, collector):
        collector.add_new_book("Чиполино")
        collector.set_book_genre("Чиполино", "Фантастика")
        assert collector.get_book_genre("Чиполино") == "Фантастика"
# тест №4 - вывод жанра книги по ее названию
    def test_get_book_genre(self, collector):
        collector.add_new_book("Образец")
        collector.set_book_genre("Образец", "Фантастика")
        assert collector.get_book_genre("Образец") == "Фантастика"
# тест №5 - вывод списка книг с опредленным жанром
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Звездные войны")
        collector.add_new_book("Чужой")
        collector.set_book_genre("Звездные войны", "Фантастика")
        collector.set_book_genre("Чужой", "Ужасы")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Звездные войны"]
        assert collector.get_books_with_specific_genre("Ужасы") == ["Чужой"]
# тест №6 - вывод текущего словаря books_genre
    def test_get_books_genre(self, collector):
        collector.add_new_book("Тайна 3 планеты")
        collector.add_new_book("Кошмар")
        collector.set_book_genre("Тайна 3 планеты", "Фантастика")
        collector.set_book_genre("Кошмар", "Ужасы")
        assert collector.get_books_genre() == {"Тайна 3 планеты": "Фантастика", "Кошмар": "Ужасы"}
# тест №7 - возврат книг, которые подходят детям
    def test_get_books_for_children(self, collector):
        collector.add_new_book("Гостья из будущего")
        collector.add_new_book("Дети кукурузы")
        collector.set_book_genre("Гостья из будущего", "Фантастика")
        collector.set_book_genre("Дети кукурузы", "Ужасы")
        assert collector.get_books_for_children() == ["Гостья из будущего"]
# тест №8 - добавление книги в список избранных
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Любимая книга")
        collector.add_book_in_favorites("Любимая книга")
        assert "Любимая книга" in collector.get_list_of_favorites_books()
# тест №9 - удаление книги из списка избарнных
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Уже не любимая книга")
        collector.add_book_in_favorites("Уже не любимая книга")
        collector.delete_book_from_favorites("Уже не любимая книга")
        assert "Уже не любимая книга" not in collector.get_list_of_favorites_books()
# тест №10 - вывод списка избранных книг
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("Хорошая книга")
        collector.add_new_book("Лучшая книга")
        collector.add_book_in_favorites("Хорошая книга")
        collector.add_book_in_favorites("Лучшая книга")
        assert collector.get_list_of_favorites_books() == ["Хорошая книга", "Лучшая книга"]

    # Негативные тесты
# тест №11 - добавление пустого ввода в названии книги
    def test_add_new_book_with_empty_name(self, collector):
        collector.add_new_book("")
        assert "" not in collector.get_books_genre()
# тест №12 - добавление книги в названии которого 41 символ
# тест №13 - добавление книги в названии которого 40 символов
    @pytest.mark.parametrize('name', ['Ллллллллллллллллллллллллллллллллллллллллл', 'ьььььььььььььььььььььььььььььььььььььььь'])
    def test_add_new_book_length_name(self, collector, name):
        collector.add_new_book(name)
        assert collector.get_book_genre(name) is None
# тест №14 - установление не существующего жанра для книги
    def test_set_book_genre_with_incorrect_genre(self, collector):
        collector.add_new_book("Книга 1")
        collector.set_book_genre("Книга 1", "Жанр")
        assert collector.get_book_genre("Книга 1") is not None
