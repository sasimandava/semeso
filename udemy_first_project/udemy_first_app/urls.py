from django.conf.urls import url
from django.contrib import admin
from udemy_first_app import views

#TEMPLATE TAGGING
app_name = 'udemy_first_app'

urlpatterns = [
    url(r'^$',views.semeso_news,name='semeso_news'),
]
