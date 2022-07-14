from django.urls import path
from .views import MapsView

urlpatterns = [path("maps", MapsView.as_view())]
