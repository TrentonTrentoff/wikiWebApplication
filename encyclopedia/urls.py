from django.urls import path

from . import views
app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search", views.search, name="search"),
    path("wiki/new", views.newpage, name="newpage"),
    path("wiki/random", views.random, name="random"),
    path("wiki/<str:article>", views.article, name="article"),
    path("wiki/<str:article>/editpage", views.editpage, name="editpage")
]
