"""
#--------------------------------------------------------------------------#
# Web URL : These routes are used to navigate inside the app.
#--------------------------------------------------------------------------#
"""

from django.urls import path
from apps.home.views import HomeRoutes


home = HomeRoutes()

webRoutes = [
    path('', home.index, name="home.index"),
    path('about', home.about, name="home.about"),
]

urlpatterns = webRoutes
