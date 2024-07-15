from django.shortcuts import render


def homepage(request):
    """Функция, отвечающая за страничку 'Главная'"""
    template_dir = "homepage/homepage.html"

    context = {}

    return render(request, template_dir, context=context)
