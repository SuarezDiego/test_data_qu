from django.views.generic import TemplateView, View, FormView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
import urllib.request, json 
#forms
from .forms import *

# dashboard
class Dashboard(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = [
            {'name': 'Dashboard', 'url': None}
        ]
        context['dashboard'] = True
        return context

    def get_template_names(self):
        template = "app/dashboard/administrador.html"
        return [template]
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        host = request.get_host()
        with urllib.request.urlopen("http://" + host + "/data_statistics") as url:
            data = json.loads(url.read().decode())
        context['data'] = data
        return self.render_to_response(context)
