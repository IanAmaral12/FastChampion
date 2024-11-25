from django.shortcuts import render

def home_organizador(request):
    if request.method == "GET":
        return render(request, 'home_organizador.html')
