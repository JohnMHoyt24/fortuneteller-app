from django.urls import path
from . import views #'.' refers to the root directory. Then everything from views.py is imported.

urlpatterns = [
  #fortune() comes from the external views.py file.
  path('', views.fortune)
]