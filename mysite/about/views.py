from django.shortcuts import render


def about(request):
    template_dir = "about/about.html"
    context = {}
    return render(request, template_dir, context=context)
