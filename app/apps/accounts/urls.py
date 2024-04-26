from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'accounts'
urlpatterns = [
    path('api/v1/accounts/', include(
        ([
            path('sign_up/', views.sign_up, name='sign_up_accounts'),
            path('sign_in/', views.sign_in, name='sign_in_accounts'),
            path('sign_out/', views.sign_out, name='sign_out_accounts'),
        ], 'accounts_api_v1')
    ))
]
