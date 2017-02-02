from django.conf.urls import include, url

#regular expressions
# the r in r'^cts/index.html$' indicates that what is inside the quotes is a regular expression
# the ^ in r'^cts/index.html$' indicates that we are looking to extend from the root dir from this part of the string
# the $ in r'^cts/index.html$' indicates that we are looking to extend end the mathing part exactly here

print('qed.urls')
#appends to the list of url patterns to check against
urlpatterns = [
	url(r'^', include('splash_app.urls')),
    url(r'^hem/', include('hem_app.urls')),
    #url(r'^hwbi/', include('hwbi_app.urls')),
    #url(r'^cts/', include('cts_app.urls')),
    #url(r'^ubertool/', include('ubertool_app.urls')),
]
