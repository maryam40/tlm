from django.conf.urls import include, url

app_name = 'users'

# Add django views urls here
urlpatterns = [
]

# Add API urls here
urlpatterns += [
    # url(r'^api/', include('tlm.apps.users.api.urls', namespace='api')),
]
