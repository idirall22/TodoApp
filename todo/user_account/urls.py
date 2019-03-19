from django.urls import path, re_path, include

urlpatterns = [
    path('api/', include('user_account.api.urls')),
    re_path(r'^auth/', include('rest_auth.urls'))
]
