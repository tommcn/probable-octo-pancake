from django.shortcuts import render

from .models import classe

# Create your views here.
def index(request):
    """
    The view shows a blank screen with both navbars    
    """
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
    for i in c:
        if i.code == q:
            return render(request, "codes/index.html", context={"classes": c, "focus": i})
    return render(request, "codes/index.html", context={"classes": c})

def codes(request):
    """
    Show all the codes and relevant information in a table for quick search
    """
    c = classe.objects.all().order_by('commnence')
    return render(request, "codes/codes.html", context={"classes": c})



