from django.conf.urls import url, include
from addresses import views
from django.urls import path
from django.contrib import admin


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('^$', views.login_page),
    path('addresses/', views.address_list),
    path('addresses/<int:pk>/', views.address),
    path('login/', views.login),
    path('admin/', admin.site.urls),
    path('app_login/', views.app_login),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
