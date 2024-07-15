from django.shortcuts import render


def about(request):
    """Функция, отвечающая за страничку 'О нас'"""
    template_dir = "about/about.html"

    context = {}

    return render(request, template_dir, context=context)
