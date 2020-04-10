import datetime

import pytz 

from django.shortcuts import render

from .models import classe

# Create your views here.
def index(request):
    """
    The view shows a blank screen with both navbars    
    """
    c = classe.objects.all().order_by('commnence')
    for i in c:
        if in_the_past(i.commnence):
            d = datetime.timedelta(days=7)
            obj = classe.objects.filter(code=i.code)
            obj.update(commnence=i.commnence+d)

    c = classe.objects.all().order_by('commnence')

    return render(request, "codes/index.html", context={"classes": c})

def display_class(request, q="math"):
    """
    Displays a classe chosen by the user in a variable "focus"
    """
    c = classe.objects.all().order_by('commnence')
    try:
        q = int(q)
    except ValueError:
        return render(request, "codes/index.html", context={"classes": c})
    focus = []
    for i in c:
        if i.code == q:
            focus.append(i)
    if focus != []:
        return render(request, "codes/index.html", context={"classes": c, "focus": focus})
    return render(request, "codes/index.html", context={"classes": c})

def codes(request):
    """
    Show all the codes and relevant information in a table for quick search
    """
    c = classe.objects.all().order_by('commnence')
    return render(request, "codes/codes.html", context={"classes": c})





def in_the_past(value):
    """
    Is the datetime object in the past (boolean)
    """
    now = datetime.datetime.now(pytz.utc)
    print(value < now)
    return value < now

def in_the_future(value):
    """
    Is the datetime object in the future (boolean)
    """
    now = datetime.datetime.now(pytz.utc)
    print(value > now)
    return value > now
