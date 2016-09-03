import urllib2
from bs4 import BeautifulSoup
import pkg_resources


class NetflixGenre:
    
    def __init__(self, genre_id):
        self.genre_id = genre_id
        self._title = None
        self._films = None
        self._cookie = self._read_cookie()
        self._soup = self.netflixGenrePage(genre_id)

    @staticmethod
    def _read_cookie():
        filename = pkg_resources.resource_filename('netflix_genre', './cookie')
        return open(filename, 'rb').read()

    def netflixGenrePage(self, genre_id):
        opener = urllib2.build_opener()
        opener.addheaders.append(('Cookie', self._cookie))
        page = opener.open('https://www.netflix.com/browse/genre/%d' %genre_id)
        pagetxt = page.read()
        soup = BeautifulSoup(pagetxt, "lxml")
        return soup

    @property
    def title(self):
        if self._title is None:
            try:
                title = self._soup.find('span', {'class', 'genreTitle'}).text
            except AttributeError:
                title = '<not found>'
            self._title = title
        return self._title

    @property
    def films(self):
        if self._films is None:
            title_containers = self._soup.findAll('div', {'class':'title-card-container'})
            titles = []
            for t in title_containers:
                for t_ in t.children:
                    title = t_['aria-label']#.encode('utf-8')
                    if title:
                        titles.append(title)
            self._films = titles
        return self._films



        
