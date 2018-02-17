from django.urls import path

import users.views

urlpatterns = [
    path('me/', users.views.me, name='me'),
    path('login/', users.views.login_view, name="login"),
    path('logout/', users.views.logout_view, name="logout"),
    path('return_from_ulb/', users.views.return_from_ulb, name="return_from_ulb"),
]
