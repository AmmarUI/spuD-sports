from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'user' : 'Ammar',
    }

    return render(request, "main.html", context)    