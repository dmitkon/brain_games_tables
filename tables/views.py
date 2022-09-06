from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'templates_name': 'main.html'
    }

    return render(request, 'index.html', context=data)

def tournaments(request, name, title):
    data = {
        'templates_name': 'tournaments.html',
        'name': title
    }

    return render(request, 'index.html', context=data)
