from django.conf.urls import patterns, include, url
from django.contrib import admin
#from mysite.views import hello, home, current_datetime, hours_plus, search_form
from mysite.books import views
from mysite.contact import views as contact_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    ('^hello/$', views.hello),
    ('^time/$', views.current_datetime),
    (r'^time/hour/(\d{1,2})/$', views.hours_plus),
    (r'^search-form/$', views.search_form),
    (r'^search/$', views.search),
    (r'^contact/$', contact_views.contact),
    ('^$', views.home),
)
