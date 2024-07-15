from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, Booking

from datetime import datetime, timedelta


def services(request):
    """Функция, отвечающая за страничку 'Услуги'"""
    template_dir = "services/services.html"

    services = Service.objects.all()

    context = {
        "services": services
    }

    return render(request, template_dir, context=context)


def detail(request, id):
    """Функция, отвечающая за страничку 'Об услуге'"""
    template_dir = "services/detail.html"

    service = get_object_or_404(Service, id=id)

    context = {
        "service": service,
    }

    return render(request, template_dir, context=context)


def booking(request, id):
    """Функция, отвечающая за страничку 'Бронь'"""
    template_dir = "services/booking.html"

    service = get_object_or_404(Service, id=id)
    user = request.user

    if user.is_authenticated:
        current_datetime = datetime.now()
        one_hour_later = current_datetime + timedelta(hours=1)
        one_month_later = current_datetime + timedelta(days=30)

        if request.method == "POST":
            datetime_str = request.POST.get("datetime")
            datetime_ = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M")
            if datetime_ > current_datetime:
                book_obj = Booking(
                    service=service,
                    user=user,
                    datetime=datetime_
                )
                book_obj.save()
                return redirect("user:user")
            return redirect("services:booking", id=service.id)

        context = {
            "service": service,
            "datetime_value": one_hour_later.strftime("%Y-%m-%d %H:%M"),
            "min_date": current_datetime.strftime("%Y-%m-%d %H:%M"),
            "max_date": one_month_later.strftime("%Y-%m-%d %H:%M"),
        }

        return render(request, template_dir, context=context)
    return redirect("auth:login")
