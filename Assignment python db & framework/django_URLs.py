# What is Django URLs? make program to create django urls.

'''
In Django, URLs are used to map web requests to specific functions or views in your application. 
Django URLs are defined in a separate module, usually named urls.py
The function-based view and class-based view both can be used for creating Django URLs.

Here's an example of how you might define some URL patterns using the function-based view:

urlpatterns = [
    path('', home_view),   # The empty string '' represents the base URL
    path('about/', about_view),
]

And here's what that would look like if we were using a class-based view instead:

from django.views import View
from django.http import HttpResponse

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Home page")

urlpatterns = [
    path('home/', HomeView.as_view()),
]

'''