from django.urls import path, include
from . import views

urlpatterns = [
    path('all', views.AllKeywordsView.as_view()),
    path('terms', views.KeywordListView.as_view(), name='terms'),
    path('terms/<int:page>', views.listing, name='terms-by-page'),
    path('terms.json', views.listing_api, name='terms-api'),

    # Faux Pagination Examples
    path(
        "faux",
        views.AllKeywordsView.as_view(
            template_name="core/faux_pagination.html"
        ),
    ),
    path(
        "load_more",
        views.AllKeywordsView.as_view(template_name="core/load_more.html"),
    ),
    path(
        "infinite_scrolling",
        views.AllKeywordsView.as_view(
            template_name="core/infinite_scrolling.html"
        ),
    ),
    path(
        "search",
        views.AllKeywordsView.as_view(template_name="core/search.html"),
    ),
]