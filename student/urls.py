from django.urls import path
from . import views
from .views import *
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.student_show, name = 'student_show'),
    path("dataflair/", index),
    path('redirect/', data_flair),
    path('djangotutor/', tutorial.as_view()),
    path('djangotutorss/', RedirectView.as_view(url = 'http://localhost:8000/student/dataflair/')),
    path('inf2/', inf2),
    path('inf1/', inf1),
    path('setcookie/', setcookie),
    path('showcookie/', showcookie),
    path('delete_co/', delete_co),
    path('testcookie/', cookie_session),
    path('deletecookie/', cookie_delete),
    path('create/', create_session),
    path('access/', access_session),
    path('delete/', delete_session),
    # path(‘delete/’, delete_session)
]