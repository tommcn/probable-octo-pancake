import datetime

import pytz 

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .models import classe, GROUPES_CHOICES

# pylint: disable=no-member

# Create your views here.
def login_view(request):    # Login page for restricteed pages
    if request.method == 'POST':
        username = "user"
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "codes/login.html", {"message": "Mauvais mot de passe."})
    else:
        if request.user.is_authenticated:
            return redirect("/")
        else:
            return render(request, "codes/login.html")

def logout_view(request):
    logout(request)
    return redirect("/")

@login_required
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

    c = classe.objects.all().order_by('commnence').filter(posted=True)

    return render(request, "codes/index.html", context={"classes": c})

@login_required
def display_class(request, q="math"):
    """
    Displays a classe chosen by the user in a variable "focus"
    """
    c = classe.objects.all().order_by('commnence').filter(posted=True)
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

@login_required
def codes(request):
    """
    Show all the codes and relevant information in a table for quick search
    """
    c = classe.objects.all().order_by('commnence').filter(posted=True)
    return render(request, "codes/codes.html", context={"classes": c})

@login_required
def soumission(request):
    if request.method == 'POST':
        nom = request.POST["nom"]
        classes = request.POST["classe_groupe"]
        prof = request.POST["prof"]
        commnence = request.POST["commnence"]
        code = request.POST["code"]
        link = request.POST["link"]
        try:
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
        except Exception as e:
           print(e)
           return render(request, "codes/submit.html") 
        return redirect("codes:codes")
    else:
        return render(request, "codes/submit.html", context={"choises": GROUPES_CHOICES})

@login_required
def user_classes(request):
    if request.method == 'GET':
        if request.user.username != "user":
            all_c = classe.objects.all().order_by('commnence').filter(posted=True)
            c = request.user.profile.subscribed_to.all()
            all_g = GROUPES_CHOICES
            checked = []
            for i in request.user.profile.subscribed_to.all():
                checked.append(i.classe_groupe)

            return render(request, "codes/custom_classes.html", context={"classes": c, "all_classes": all_c, "all_g": all_g, "checked": checked})

        else:
            c = classe.objects.all().order_by('commnence').filter(posted=True)
            message = "Pour accéder a cette page, il faut s'être identifié avec un compte google"
            return render(request, "codes/codes.html", context={"classes": c, "message": message})
    else:
        checked = []
        for key in request.POST:
            checked.append(key)
        checked.pop(0) # CSRF
        request.user.profile.subscribed_to.clear()
        ac = classe.objects.all().order_by('commnence').filter(posted=True)
        for i in checked:
            for c in ac:
                if i == c.classe_groupe:
                    request.user.profile.subscribed_to.add(c)
            
        all_c = classe.objects.all().order_by('commnence').filter(posted=True)
        c = request.user.profile.subscribed_to.all()
        all_g = GROUPES_CHOICES
        return render(request, "codes/custom_classes.html", context={"classes": c, "all_classes": all_c, "all_g": all_g, "checked": checked})



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
