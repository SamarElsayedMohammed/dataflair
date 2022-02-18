from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from django.views.generic.base import RedirectView 

def student_show(request):
    student = Student.objects.order_by('roll_no')
    return render(request, 'student/student_show.html', {'student': student})


def index(request):
    html = """<h1 style ="color:red;"><i>Data Flair Django</i></h1>Hello, you just configured you First URL"""
    return HttpResponse(html)

def data_flair(request):
    return redirect('/student/dataflair')

def inf1(request):
    return redirect('student/inf2')

def inf2(request):
    return redirect('student/inf1')

# def setcookie(request):
#     html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
#     html.set_cookie('dataflair', 'Hello this is your Cookies', max_age = None)
#     return html

def setcookie(request):
    html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
    if request.COOKIES.get('visits'):
        html.set_cookie('dataflair', 'Welcome Back')
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits', value + 1)
    else:
        value = 1
        text = "Welcome for the first time"
        html.set_cookie('visits', value)
        html.set_cookie('dataflair', text)
    return html


def showcookie(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('dataflair')
        html = HttpResponse("<center><h1>{0}<br>You have requested this page {1} times</h1></center>".format(text, value))
        html.set_cookie('visits', int(value) + 1)
        return html
    else:
        return redirect('/setcookie')

def delete_co(request):
    if request.COOKIES.get('visits'):
       response = HttpResponse("<h1>dataflair<br>Cookie deleted</h1>")
       response.delete_cookie("visits")
    else:
        response = HttpResponse("<h1>dataflair</h1>need to create cookie before deleting")
    return response


# def showcookie(request):
#     show = request.COOKIES['dataflair']
#     html = "<center> New Page <br>{0}</center>".format(show)
#     return HttpResponse(html)

class tutorial(RedirectView): 
    url = 'http://localhost:8000/student/dataflair/'


def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>dataflair</h1>")
def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("dataflair<br> cookie createed")
    else:
        response = HttpResponse("Dataflair <br> Your browser doesnot accept cookies")
    return response


def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>dataflair<br> the session is set</h1>")


def access_session(request):
    response = "<h1>Welcome to Sessions of dataflair</h1><br>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('create/')


def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except  KeyError:
        pass
    return HttpResponse("<h1>dataflair<br>Session Data cleared</h1>")

