import markdown,time

from markdown.extensions.toc import TocExtension
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils.text import slugify
from .models_mongo import *

       

class audioView(ListView):
    model = Race
    template_name = 'audio/audio_home.html'
    context_object_name = 'audio_list'
    paginate_by = 40
    #def get_context_data(self, **kwargs):
     #   return context
   
    def get_queryset(self):
       return Race.objects
