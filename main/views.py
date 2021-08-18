from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from main.forms import ContactForm


def home(request):
    form = ContactForm()

    context = {
        "name": "Gideon Anyalewechi",
        "role": "Backend Developer",
        "email": "ganyalewechi1997@gmail.com",
        "address": "Awka, Nigeria.",
        "phone": "+2439014610125",
        "zuri_url": "https://zuri.team",
        "form": form,
    }

    return render(request, "index.html", context)


def send_email(request):
    if request.POST:
        form = ContactForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            name = data.get("name")
            email = data.get("email")
            subject = data.get("subject")
            message = data.get("message")

            try:
                # having doubts about leaving this here for speed reasons
                # email to visitor
                send_mail(
                    subject=f"Re: {subject}",
                    message=f"Thank you for reaching out, I have received your message and will be in touch with you shortly.\n\nMessage Review:\n{message}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email],
                )
                messages.success(
                    request,
                    f"Thank you {name}. Your message - {subject} - has been received. I will be in touch as soon as possible.",
                )
            except Exception:
                messages.error(
                    request,
                    f"Sorry {name}. Your message - {subject} - could not be processed. Please try again later.",
                )

    return redirect("home")
