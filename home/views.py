from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils import timezone

from .models import App

# Classes
class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'app_list'

    def get_queryset(self):
        return App.objects.all()
