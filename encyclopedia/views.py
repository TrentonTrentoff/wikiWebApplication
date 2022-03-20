from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article(request, article):
    if not util.get_entry(article):
        return render (request, "encyclopedia/content.html", {
        "title": None,
        "content": None
    })
    else:
        return render (request, "encyclopedia/content.html", {
        "title": article,
        "content": util.get_entry(article)
    })