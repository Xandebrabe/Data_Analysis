from django.urls import path

from .views import index, sobrenos

urlpatterns = [
    path('', index, name='index'),
    path('sobrenos', sobrenos, name='sobrenos')
]