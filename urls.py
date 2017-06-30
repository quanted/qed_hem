from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

#regular expressions
# the r in r'^cts/index.html$' indicates that what is inside the quotes is a regular expression
# the ^ in r'^cts/index.html$' indicates that we are looking to extend from the root dir from this part of the string
# the $ in r'^cts/index.html$' indicates that we are looking to extend end the matching part exactly here

#appends to the list of url patterns to check against
urlpatterns = [
	url(r'^', include('splash_app.urls')),
    url(r'^hem/', include('hem_app.urls')),
    #url(r'^hwbi/', include('hwbi_app.urls')),
    #url(r'^cts/', include('cts_app.urls')),
    #url(r'^ubertool/', include('ubertool_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		url(r'^__debug__/', include(debug_toolbar.urls)),
	] + urlpatterns


