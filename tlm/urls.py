"""
TLM URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from tlm.apps.core import views


urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^$', views.index, name='index'),

    # Include apps API urls without prefix so that we can preserve the
    # patterns for django "{app_namespace}/" and DRF "api/v1/{app_namespace}"
    url(r'', include('tlm.apps.users.urls', namespace='users')),
]


if settings.DEBUG:  # pragma: no cover
    import debug_toolbar

    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
