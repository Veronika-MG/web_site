from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.utils import timezone

from services.models import Booking
from .forms import ProfileImageForm
from .models import Profile


def user(request):
    """Функция, отвечающая за страничку 'Профиль'"""
    template_dir = "user/user.html"

    user = request.user

    if user.is_authenticated:
        profile = get_object_or_404(Profile, user=user)

        bookings_past = Booking.objects.filter(
            user=user, datetime__lte=timezone.now()
        ).order_by("-datetime")

        bookings_future = Booking.objects.filter(
            user=user, datetime__gte=timezone.now()
        ).order_by("-datetime")

        context = {
            "profile": profile,
            "bookings_past": bookings_past,
            "bookings_future": bookings_future,
        }

        return render(request, template_dir, context=context)
    return redirect("auth:login")


def delete_booking(request):
    """Функция, отвечающая за удаления брони"""
    id = int(request.POST.get("id"))

    booking = Booking.objects.get(id=id)
    booking.delete()

    return JsonResponse({"error": "OK"}, status=200)


def update_image(request):
    """Функция, отвечающая за страничку 'Смена фотографии"""
    template_dir = "user/update_image.html"

    if request.user.is_authenticated:
        profile = request.user.profile

        if request.method == "POST":
            form = ProfileImageForm(
                request.POST, request.FILES, instance=profile
            )
            if form.is_valid():
                profile.update()
                form.save()
                return redirect("user:user")
        else:
            form = ProfileImageForm(instance=profile)

        context = {"form": form}

        return render(request, template_dir, context=context)
    return redirect("auth:login")
