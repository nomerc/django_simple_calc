from api.views import main
from django.urls import path
from .views import CalcView, main

urlpatterns = [
    path('', main),
    path('calc', CalcView.as_view()),
]