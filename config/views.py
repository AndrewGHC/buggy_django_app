# -*- coding: utf-8 -*-
from django.views.generic import RedirectView

def redirect(request, redirectLocation):
    print(type(redirectLocation))
    print('hi')
    return RedirectView.as_view(url=redirectLocation)(request)
