from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', kwargs = {'template': 'discount_base.html'}, name = 'discount_show'),
) 
