from django.urls import path
from recipes.views import home
#pra exemplo de adicionar uma view simples

    

urlpatterns = [
    path('', home),


]
