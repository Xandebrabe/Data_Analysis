from django.urls import path

from .views import index, sobrenos, dados

urlpatterns = [
    path('', index, name='index'),
    path('sobrenos', sobrenos, name='sobrenos'),
    path('dados/<str:nome>', dados, name='dados'),
]