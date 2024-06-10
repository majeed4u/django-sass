from django.shortcuts import render
import pathlib

# this_dir = pathlib.Path(__file__).parent.resolve()
from visits.models import PageVisit

def home(request, *args, **kwargs):
    queryset = PageVisit.objects.filter(path=request.path)
    
    my_context = {
        'page_visit_count':queryset.count()
    }
    
    PageVisit.objects.create(path=request.path)
    
    return render(request, 'home.html', my_context)
    