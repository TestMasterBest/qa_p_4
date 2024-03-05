#!/usr/bin/env python
# -*- coding: utf-8  -*-
import pytest
from main import BooksCollector


class TestBooksCollector:
    @pytest.mark.parametrize('book_names', ['', 'Энциклопедия_мировой_литературы_на_английском_языке',
                                        'Методика_преподавания_математики_в_начальной_школе',
                                        'Остров_сокровищ_и_его_хранитель_Джим'])
    def test_add_new_book(self,book_names):
        books_collector = BooksCollector()
        books_collector.add_new_book(book_names)
        assert book_names in books_collector.get_books_genre()

    @pytest.mark.parametrize('book_genre', ['Классика', 'Фантастика', 'Детский'])
    def test_set_book_genre(self,book_genre):
        books_collector = BooksCollector()
        books_collector.add_new_book("Преступление и наказание")
        books_collector.set_book_genre("Преступление и наказание", book_genre)
        assert books_collector.get_book_genre("Преступление и наказание") == book_genre

    @pytest.mark.parametrize('specific_genre, expected_book', [('Исторический', 'Война и мир'),
                                                           ('Приключения', 'Остров сокровищ и его хранитель Джим')])
    def test_get_books_with_specific_genre(self,specific_genre, expected_book):
        books_collector = BooksCollector()
        books_collector.add_new_book(expected_book)
        books_collector.set_book_genre(expected_book, specific_genre)
        assert expected_book in books_collector.get_books_with_specific_genre(specific_genre)

    def test_add_delete_book_in_favorites(self):
        books_collector = BooksCollector()
        books_collector.add_new_book("Сказка о царе Салтане")
        books_collector.add_book_in_favorites("Сказка о царе Салтане")
        assert "Сказка о царе Салтане" in books_collector.get_list_of_favorites_books()

        books_collector.delete_book_from_favorites("Сказка о царе Салтане")
        assert "Сказка о царе Салтане" not in books_collector.get_list_of_favorites_books()

    def test_get_books_for_children(self):
    # Создаем экземпляр коллекции книг
        books_collector = BooksCollector()

    # Добавляем книги с разными жанрами
        books_collector.add_new_book("Книга1")
        books_collector.add_new_book("Книга2")

    # Устанавливаем жанры для книг на русском языке
        books_collector.set_book_genre("Книга1", "Фантастика")
        books_collector.set_book_genre("Книга2", "Мультфильмы")

    # Устанавливаем возрастной рейтинг для некоторых жанров
        books_collector.set_genre_age_rating("Ужасы", 18)
        books_collector.set_genre_age_rating("Детективы", 16)

    # Проверка, что возрастной рейтинг установлен корректно
        assert books_collector.get_genre_age_rating("Ужасы") == 18
        assert books_collector.get_genre_age_rating("Детективы") == 16

    # Проверяем, что возрастной рейтинг не установлен для несуществующего жанра
        assert books_collector.get_genre_age_rating("Романтика") is None


    # Проверка, что возвращается только книга с жанром "Мультфильмы"
        assert books_collector.get_books_for_children() ==  ["Книга2"]

    #  Проверка количества книг, возвращаемых для детей
        assert len(books_collector.get_books_for_children()) == 1

