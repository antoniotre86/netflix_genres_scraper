from argparse import ArgumentParser

import sys
sys.path.append('..')

from netflix_genre.NetflixGenre import NetflixGenre
import time


def scrapeNetflixUKGenres(id_range, save_to='./netflix_genres.txt', verbose=True):
    for genre_id in range(*id_range):
        if verbose: print genre_id,
        ng = NetflixGenre(genre_id)
        title = ng.title
        if verbose: print title,
        if title != '<not found>':
            films = ng.films
            if verbose: print len(films)
            row = str(genre_id) + ' | "' + title + '"' + ' | ' + '"' + '", "'.join(films) + '"' + '\n'
            with open(save_to, 'ab') as fooa:
                fooa.write(row.encode('utf-8'))
        else:
            if verbose: print
            continue
        time.sleep(0.1)
        

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('id_range', nargs='+', type=int)
    parser.add_argument('-s', required=True)
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()
    scrapeNetflixUKGenres(id_range=args.id_range, save_to=args.s, verbose=args.verbose)


