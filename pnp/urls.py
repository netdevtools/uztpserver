from django.urls import path
from .views import work_request, work_response

urlpatterns = [
    path('WORK-REQUEST', work_request),
    path('WORK-RESPONSE', work_response),
]
