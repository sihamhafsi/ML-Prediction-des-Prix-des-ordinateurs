from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name="home"), 
    path('predict', views.predict, name="predict"), 
    path('Gradient_Descent', views.Gradient_Descent, name="Gradient_Descent"), 
    path('Gradient_Stochaqtiue', views.Gradient_Stochaqtiue, name="Gradient_Stochaqtiue"), 
] 