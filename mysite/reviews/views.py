from django.shortcuts import render, redirect

from .models import Review
from .forms import ReviewForm


def reviews(request):
    template_dir = "reviews/reviews.html"

    reviews_list = Review.objects.all().order_by("-date")

    if request.method == "POST":
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                profile = request.user.profile
                is_created = Review.objects.filter(profile=profile).exists()
                if is_created:
                    rev = Review.objects.get(profile=profile)
                    rev.text = form.cleaned_data.get("text")
                    rev.save()
                else:
                    review = form.save(commit=False)
                    review.profile = profile
                    review.save()
                return redirect("reviews:reviews")
        return redirect("auth:login")
    else:
        form = ReviewForm()

    context = {
        "reviews": reviews_list,
        "review_form": form,
    }

    return render(request, template_dir, context=context)
