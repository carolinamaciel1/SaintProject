from django.urls import path

from . import views
from .views import ListSaintsView

urlpatterns = [
    path('saints/', ListSaintsView.as_view(), name="all_saints"),
    # url(r'/<int:pk>/', views.detail_saints, name="detail_saint"),
]