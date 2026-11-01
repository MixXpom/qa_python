from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    def test_set_book_genre_horror(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == 'Ужасы'

    def test_get_book_genre_known_name(self):
        collector = BooksCollector()
        collector.add_new_book('Котопес', 'Мультфильм')
        assert collector.get_book_genre('Котопес') == 'Мультфильм'


    def test_get_books_with_specific_genre_horror(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Котопес', 'Мультфильм')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби']

    
    def test_get_books_genre_three_names(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Котопес', 'Мультфильм')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Ужасы', 'Котопес': 'Мультфильм', 'Что делать, если ваш кот хочет вас убить': 'Комедии'}

    def test_get_books_for_children_comedy(self):
        collector = BooksCollector()
        collector.genre_age_rating = ['Ужасы', 'Триллеры']
        collector.genre = ['Комедии', 'Сказки', 'Приключения']
        collector.add_new_book('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert collector.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить']  

    def test_add_book_in_favorites_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Котопес', 'Мультфильм')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.favorites == ['Гордость и предубеждение и зомби']

    def test_delete_book_from_favorites_one_name(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Котопес', 'Мультфильм')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Котопес')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.favorites == ['Котопес']

    def test_get_list_of_favorites_books_one_name(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Котопес', 'Мультфильм')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби'] 