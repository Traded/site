from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'traded_io.views.home', name='home'),
    url(r'^login$', 'traded_io.views.login', name='login'),
    # url(r'^traded_io/', include('traded_io.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'api/', include('api.urls', namespace='api')),
    url(r'social/', include('social.apps.django_app.urls', namespace='social')),
)
