'''
Urls for shortener app ushapp/urls.py
'''

from django.urls import path

# Import the home view
from .views import home_view, redirect_url_view

appname = "ushapp"

urlpatterns = [
    # Home view
    path('', home_view, name='home'),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
]
