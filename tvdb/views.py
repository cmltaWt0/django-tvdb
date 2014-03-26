# -*- coding: utf-8 -*-
from django.contrib.auth import views
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


def user_login(request):
    """
    Login func
    """
    if request.user.is_authenticated():
        return TemplateResponse(request, 'tvdb/already_logged.html')
    else:
        return views.login(request, template_name='tvdb/login.html')


def user_logout(request):
    """
    Logout func
    """
    if request.user.is_authenticated():
        return views.logout(request, next_page=reverse('tvdb:goodbye'))
    else:
        return TemplateResponse(request, 'tvdb/not_logged.html')


@login_required(login_url='/tvdb/accounts/login/')
def default(request):
    """
    Show default page tvdb's app.
    """
    return TemplateResponse(request, 'tvdb/default_tvdb.html', locals())

