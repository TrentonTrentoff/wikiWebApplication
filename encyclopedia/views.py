from turtle import title
from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import util

class NewSearchForm(forms.Form):
    search = forms.CharField(label = "Search")

class NewArticleForm(forms.Form):
    title = forms.CharField(label="Title of Article")
    content = forms.CharField(widget=forms.Textarea, label = "Content of Article")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": NewSearchForm()
    })

def article(request, article):
    if not util.get_entry(article):
        return render (request, "encyclopedia/content.html", {
        "title": article,
        "content": "There is no article under this name!",
        "form": NewSearchForm()
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

def newpage(request):
    if request.method == "GET":
        return render (request, "encyclopedia/newpage.html", {
            "contentTitle": "Create a new page!",
            "form": NewSearchForm(),
            "articleForm": NewArticleForm()
        })
    else:
        content = NewArticleForm(request.POST)
        if content.is_valid():
            title = content.cleaned_data["title"]
            content = content.cleaned_data["content"]
        allResults = util.list_entries()
        if title in allResults:
            return render (request, "encyclopedia/newpage.html", {
            "contentTitle": "Error, article already exists, try again!",
            "form": NewSearchForm(),
            "articleForm": NewArticleForm()
        })
        else:
            title = title.capitalize()
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("encyclopedia:article", args=[title]))

def editpage(request):
    pass