from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import TemplateView

# Function based view
def testPageView(request):
    return HttpResponse("Testing")

# Class Based View
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'