from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns =[

url(r'^$', views.index, name='index'),
url(r'^user$', views.show),
url(r'^reg$', views.reg),
url(r'^siti$', views.reg),
url(r'^zakaz$', views.zaksz1),
#url(r'^new_user$', views.create),
    #url(r'^search-form/$', views.search_form),
]