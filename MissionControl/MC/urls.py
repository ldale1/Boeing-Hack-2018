from django.urls import path
from . import views

urlpatterns = [
	# ex: /MC/
    path('', views.index, name='index'),
]