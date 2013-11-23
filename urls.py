from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # (r'^yoursite/', include('yoursite.foo.urls')),

	# (r'^admin/doc/', include('django.contrib.admindocs.urls')), 
	# And add 'django.contrib.admindocs' to INSTALLED_APPS
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    )