""" Containers module. """

from dependency_injector import containers, providers

from . import finders, listers, entities


class Container(containers.DeclarativeContainer):

    config = providers.Configuration(yaml_files=["config.yml"])

    movie = providers.Factory(entities.Movie)

    csv_finder = providers.Singleton(
        finders.CsvMovieFinder,
        movie_factory=movie.provider,
        path=config.finder.csv.path,
        delimiter=config.finder.csv.delimiter,
    )

    lister = providers.Factory(
        listers.MovieLister,
        movie_finder=csv_finder
    )
