from django.shortcuts import render
from django.utils import timezone
from .models import Movie
from .strategies import get_strategy   # no services import

def upcoming_movies(request):
    sort_key = request.GET.get("sort", "date")
    strategy = get_strategy(sort_key)

    today = timezone.localdate()
    qs = Movie.objects.filter(release_date__gte=today)
    ordered = strategy.sort(qs)        # call strategy directly

    return render(request, "cinema/upcoming_list.html", {
        "movies": ordered,
        "active_sort": sort_key,
    })
