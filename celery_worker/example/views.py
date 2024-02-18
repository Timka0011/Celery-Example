from django.shortcuts import render, redirect
from .tasks import send_email_task
# Create your views here.


def index(request):

    if request.method == "POST":
        email = request.POST['email']
        message = request.POST['message']
        send_email_task.delay(email, message)
        return redirect("sources")
    return render(request, 'index.html')


def success(request):
    return render(request, 'sucess.html')