from django.conf.urls import include,patterns, url
from app.home.views import index
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$',index),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    # url('', include('social.apps.django_app.urls', namespace='social')),
    # url('', include('django.contrib.auth.urls', namespace='auth')),
    # url(r'^accounts/', include('app.accounts.urls')),
    # url(r'^home/', include('app.home.urls')),

)
