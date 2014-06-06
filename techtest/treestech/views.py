from django.shortcuts import render
from .models import Genre

def tree1(request):
    data = {}
    template = 'treestech/tree1.html'
    data['nodes']=Genre.objects.all()
    return render(request, template, data)





