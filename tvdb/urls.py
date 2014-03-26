from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', 'tvdb.views.default', name='default'),

    url(r'^accounts/login/$', 'tvdb.views.user_login', name='login'),
    url(r'^accounts/login/welcome/$', TemplateView.as_view(template_name='tvdb/welcome.html'), name='welcome'),

    url(r'^accounts/logout/$', 'tvdb.views.user_logout', name='logout'),
    url(r'^accounts/logout/goodbye/$', TemplateView.as_view(template_name='tvdb/goodbye.html'), name='goodbye'),
)
