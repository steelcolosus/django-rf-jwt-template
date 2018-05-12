from django.conf.urls import url, include
from rest_framework import routers
from project.api_auth import views
from rest_framework.urlpatterns import format_suffix_patterns


from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import  TokenRefreshView

urlpatterns = [
    url(r'^$', get_schema_view()),
    url(r'^auth/', include(
        'rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/token$', views.MyTokenObtainPairView.as_view()),
    url(r'^auth/token/refresh$', TokenRefreshView.as_view()), 
 
    url(r'^signup$', views.Signup.as_view(), name='account-create'),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),
]
