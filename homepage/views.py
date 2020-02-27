from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, "homepage.html")

def aboutme(request):
    return render(request, "aboutme.html")