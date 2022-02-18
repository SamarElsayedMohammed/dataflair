from django.shortcuts import render
from dataflair.settings import EMAIL_HOST_USER
from .forms import Subscribe
from django.core.mail import send_mail

# Create your views here.
#DataFlair #Send Email
def subscribe(request):
    sub = Subscribe(request.POST)
    if request.method == 'POST':
        subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':sub})