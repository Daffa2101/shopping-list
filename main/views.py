from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'Daffa Akmal',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)