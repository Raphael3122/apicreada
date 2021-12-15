from django.urls import path
from .views import Registroview

urlpatterns=[
    path('register/',Registroview.as_view(),name='register_list'),
    path('register/<str:correo>&<contrasena>',Registroview.as_view(),name='register_process'),
]