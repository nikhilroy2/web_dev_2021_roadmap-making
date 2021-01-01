from django.shortcuts import render, HttpResponse
from .models import PersonInfo
# Create your views here.
def Index(request):
    obj = [
        {
            "id": 1,
            "name": "Nikhil",
            "country": "Bangladesh"
        },
        {
            "id": 2,
            "name": "Sonchoy",
            "country": "India"
        },
        {
            "id": 3,
            "name": "Toslim",
            "country": "Nepal"
        }
    ]
    personObj = PersonInfo.objects.all()

    context = {
        "obj": obj,
        "personObj": personObj
    }
    return render(request, 'app1/index.html', {'name': context["obj"], "personObj": context["personObj"]})