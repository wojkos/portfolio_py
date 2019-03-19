from django.conf.urls import url,include
from django.contrib import admin
from schoolapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'^$',views.IndexView.as_view()),
    url(r'^schoolapp/',include('schoolapp.urls',namespace='schoolapp')),
]