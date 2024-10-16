import requests
from django.shortcuts import render


def fetch_data(request):

    url = 'http://localhost:8080/api/projects'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    else:
        data = None

    context = {
        'data': data
    }

    return render(request, "C:\\Users\\Arseniy\\PycharmProjects\\demoTrello\\myapp\\templates\\data.html", context)
