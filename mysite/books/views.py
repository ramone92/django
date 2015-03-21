# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
#from django.utils import timezone
#from django import template
from django.shortcuts import render_to_response
from mysite.books.models import Book
import datetime

def hello(request):
    #return HttpResponse("Hello, World! at %s" % request.path)
    return render_to_response('request.html', {'information': request.META.items()})

def home(request):
    return HttpResponse("Welcome to Home page at %s" % request.path)

def current_datetime(request):
    d = datetime.datetime.now()
    #t = template.loader.get_template('current_date.html')
    #html = t.render(template.Context({'current_date': d})) 
    #return HttpResponse(html)
    return render_to_response('current_date.html', {'current_date': d})

def hours_plus(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    d = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    #html = "<html><body>With %s hour(s) plus time is %s.</body></html>" % (offset, d) 
    #return HttpResponse(html)
    params = {'offset': offset, 'future_date': d}
    return render_to_response('future_date.html', params)

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    message = u''
    errors = []
    #for k, v in request.GET.iteritems():
    #    message += "%s %s\n" % (k, v)
    if 'q' in request.GET:
        q = request.GET['q']
        if len(q) > 20:
            errors.append("Length must be less than 20.")
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'query': q, 'books': books})
    else:
        errors.append("Please enter a term.")
    return render_to_response('search_form.html', {'errors': errors})
