from django.urls import path
from .views import applicationListView, applicationDetailView

urlpatterns = [
    path('', applicationListView.as_view(), name = 'application_list'),
    path('<int:pk>', applicationDetailView.as_view(), name = 'application_detail'),
]