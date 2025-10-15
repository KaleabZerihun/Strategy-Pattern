
from abc import ABC, abstractmethod
from django.utils import timezone

class MovieSortStrategy(ABC):
    @abstractmethod
    def sort(self, qs):
        """Return an ordered queryset."""
        raise NotImplementedError

class SortByReleaseDate(MovieSortStrategy):
    def sort(self, qs):
        return qs.order_by("release_date", "title")

class SortByRating(MovieSortStrategy):
    def sort(self, qs):
        return qs.order_by("-rating", "title")

class SortByPopularity(MovieSortStrategy):
    def sort(self, qs):
        return qs.order_by("-popularity", "title")

class SortByTitle(MovieSortStrategy):
    def sort(self, qs):
        return qs.order_by("title")

STRATEGY_REGISTRY = {
    "date": SortByReleaseDate(),
    "rating": SortByRating(),
    "popularity": SortByPopularity(),
    "title": SortByTitle(),
}

def get_strategy(key: str) -> MovieSortStrategy:
    return STRATEGY_REGISTRY.get(key or "date", STRATEGY_REGISTRY["date"])
