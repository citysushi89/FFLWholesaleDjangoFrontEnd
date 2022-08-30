from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from .models import Data
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

# Create your views here.

def home (request):
    context = {
        'data': Data.objects.all()
    }
    return render(request, 'PPSapp/home.html', context)

def about(request):
    return render(request, 'PPSapp/about.html', )

@login_required
def report(request):
    return render(request, 'PPSapp/report.html', )


# Paginating and displaying the table
class TableListView(ListView):
    model = Data
    template_name = 'PPSapp/home.html'
    context_object_name = 'data'
    paginate_by = 15
