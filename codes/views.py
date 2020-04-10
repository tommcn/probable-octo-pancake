import datetime

import pytz 

from django.shortcuts import render, redirect

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

def soumission(request):
    if request.method == 'POST':
        nom = request.POST["nom"]
        classes = request.POST["classe_groupe"]
        prof = request.POST["prof"]
        commnence = request.POST["commnence"]
        code = request.POST["code"]
        link = request.POST["link"]
 #       try:
        n = classe()
        n.nom = nom
        n.classe_groupe = classes
        n.prof = prof
        n.commnence = commnence
        n.fini = commnence
        n.code = code
        n.link = link
        n.save()
        print(n)
 #       except Exception as e:
 #       print(e)
 #           return render(request, "codes/submit.html") 
        return redirect("codes")
    else:
        return render(request, "codes/submit.html")




def in_the_past(value):
    """
    Is the datetime object in the past (boolean)
    """
    now = datetime.datetime.now(pytz.utc)
    return value < now

def in_the_future(value):
    """
    Is the datetime object in the future (boolean)
    """
    now = datetime.datetime.now(pytz.utc)
    return value > now
