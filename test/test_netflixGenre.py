'''
Created on 03/09/2016

@author: antonio.trenta
'''
from unittest import TestCase
from netflix_genre.NetflixGenre import NetflixGenre
from netflix_genres_scraper import scrapeNetflixUKGenres


class TestNetflixGenre(TestCase):

    def test_netflixGenrePage_existing_genre(self):
        genre_id = 2    # << existing genre

        ng = NetflixGenre(genre_id)
        title = ng.title
        films = ng.films
        self.assertTrue(title is not None)
        self.assertGreater(len(films), 0)

    def test_netflixGenrePage_missing_genre(self):
        genre_id = 6    # << missing genre

        ng = NetflixGenre(genre_id)
        title = ng.title
        films = ng.films
        self.assertEqual(title, '<not found>')
        self.assertEqual(len(films), 0)

    def test_netflixGenrePage_unicode_genre_title(self):
        genre_id = 11

        ng = NetflixGenre(genre_id)
        title = ng.title
        films = ng.films

        self.assertTrue(True)

    def test_netflix_genres_scraper_unicode_genre_title(self):
        scrapeNetflixUKGenres((11, 13), './netflix_genres_test-000.txt', verbose=True)

        self.assertTrue(True)
