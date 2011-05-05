from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('django.contrib.auth.views',
	(r'^login/$',  'login', {'template_name' : 'login.html'}),
	(r'^logout/$', 'logout_then_login'),
)

urlpatterns += patterns('browner.dispatcher.views',
	(r'^$',     'main'),
	(r'^pop/$', 'pop' ),
	(r'^add/$', 'add' ),
)

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
)

