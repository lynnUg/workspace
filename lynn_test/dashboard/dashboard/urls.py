from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.views.generic import (TemplateView,ListView)
from django.conf import settings
from registration.views import (RegistrationView,ActivationView)
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import viewsets, routers
from webapp import views

urlpatterns = patterns('',

	 url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^',  include('registration.backends.default.urls')),
    url(r'^login$', 'django.contrib.auth.views.login'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user_list') ,
    url(r'^users/$', views.UserList.as_view(), name='the_list') ,

    # Examples:
    # url(r'^$', 'dashboard.views.home', name='home'),
    # url(r'^dashboard/', include('dashboard.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'profile_images/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )
