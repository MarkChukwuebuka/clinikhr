
from django.urls import path

from .views import home, services, about, contact, who_we_serve, resources, how_we_work, bfri_assessment

urlpatterns = [
    path('', home, name='home'),
]
