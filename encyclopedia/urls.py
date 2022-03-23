from django.urls import path

from . import views
app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search", views.search, name="search"),
    path("wiki/new", views.newpage, name="newpage"),
    path("wiki/<str:article>", views.article, name="article"),
]
