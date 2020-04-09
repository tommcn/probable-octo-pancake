from django.shortcuts import render

from .models import classe

# Create your views here.
def index(request):
    c = classe.objects.all().order_by('commnence')
    return render(request, "codes/index.html", context={"classes": c})

def display_class(request, q="math"):
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
    c = classe.objects.all().order_by('commnence')
    return render(request, "codes/codes.html", context={"classes": c})



