from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import util

class NewSearchForm(forms.Form):
    search = forms.CharField(label = "Search")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": NewSearchForm()
    })

def article(request, article):
    if not util.get_entry(article):
        return render (request, "encyclopedia/content.html", {
        "title": article,
        "content": "There is no article under this name!"
    })
    else:
        return render (request, "encyclopedia/content.html", {
        "title": article,
        "content": util.get_entry(article),
        "form": NewSearchForm()
    })

def search(request):
    if request.method == "POST":
        search = NewSearchForm(request.POST)
        if search.is_valid():
            search = search.cleaned_data["search"]
        if not util.get_entry(search):
            allResults = util.list_entries()
            searchResults = []
            for result in allResults:
                tempSearch = search.lower()
                tempResult = result.lower()
                if tempSearch in tempResult:
                    searchResults.append(result)
            return render (request, "encyclopedia/search.html", {
                "entries": searchResults,
                "form": NewSearchForm()
        })
        else:
            return HttpResponseRedirect(reverse("encyclopedia:article", args=[search]))