from django.urls import path
from homepage import views
# bara homepage hér
urlpatterns = [
    # http//localhost:8000
    path('', views.home, name="home")
]