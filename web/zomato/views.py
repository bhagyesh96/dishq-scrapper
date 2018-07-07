from django.shortcuts import render

# Create your views here.
import json
from django.template import loader

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

# Create your views here.
data = []
with open('/Users/bhagyesh/Desktop/dishq/data.json','r+') as d:
    data = json.load(d)
    x = data




def search(request):
    print(x)

    template = loader.get_template('index.html')
    context = {'x': x }
    return HttpResponse(template.render(context, request))
    #return JsonResponse(data, safe=False,content_type="application/html")
    #return render(request, 'demoApp/demo.html', {'d': data}, content_type="application/html")
