from django.urls import path

from game.views import register_view, home_page_view, profile_view

urlpatterns = [
    path('register', register_view),
    path('', home_page_view),
    path('profile', profile_view),
]
