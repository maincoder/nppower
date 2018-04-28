from django.conf.urls import url

from . import views

app_name = "audio"
urlpatterns = [

    url(r'^audio$', views.audioView.as_view(), name='audio'),
]
