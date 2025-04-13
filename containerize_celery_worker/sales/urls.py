from django.urls import path
from .views import generate_report, get_report

urlpatterns = [
    path('report/', generate_report),
    path('report/<uuid:report_id>/', get_report)
]
