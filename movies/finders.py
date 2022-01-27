""" Movie finders module. """

import csv
from typing import Callable, List

from .entities import Movie


class MovieFinder:

    def __init__(self, movie_factory: Callable[..., Movie]) -> None:
        self._movie_factory = movie_factory

    def find_all(self) -> List[Movie]:
        raise NotImplementedError()


class CsvMovieFinder(MovieFinder):

    def __init__(
            self,
            movie_factory: Callable[..., Movie],
            path: str,
            delimiter: str,
    ) -> None:
        self._csv_file_path = path
        self._delimiter = delimiter
        super().__init__(movie_factory)

    def find_all(self) -> List[Movie]:
        with open(self._csv_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self._delimiter)
            return [self._movie_factory(*row) for row in csv_reader]
