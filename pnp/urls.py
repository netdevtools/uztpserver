from django.urls import path
from .views import work_request

urlpatterns = [
    path('WORK-REQUEST', work_request),
]
