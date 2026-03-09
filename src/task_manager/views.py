from django.shortcuts import render

from django.http import HttpResponse

# MTV
def index(request):
    cities = [
        {"name": "Mumbai", "population": 19000000, "country": "India"},
        {"name": "Calcutta", "population": 15000000, "country": "India"},
        {"name": "New York", "population": 20000000, "country": "USA"},
        {"name": "Chicago", "population": 7000000, "country": "USA"},
        {"name": "Tokyo", "population": 33000000, "country": "Japan"},
    ]
    context = {
        "cities":cities
    }
    return render(request,"tasks.html",context=context)


def about(request):
    return render(request,"about.html")


def index_2(request,task):
    return HttpResponse(f"<h1>Index 2. {task}</h1>")