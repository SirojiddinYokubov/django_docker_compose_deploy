import uuid

from django.shortcuts import render, get_object_or_404
from .models import Report
from .tasks import generate_sales_report
from django.http import JsonResponse, FileResponse
from django.utils.encoding import smart_str


def generate_report(request):
    report = Report.objects.create()
    # generate_sales_report.delay(report.id)
    generate_sales_report.apply_async(args=[report.id], queue="sales123_queue")
    return JsonResponse({
        "report_id": report.id,
        "status": report.status
    })


def get_report(request, report_id: uuid.UUID):
    report = get_object_or_404(Report, id=report_id)

    if report.file:
        response = FileResponse(report.file.open('rb'), as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{smart_str(report.file.name.split("/")[-1])}"'
        return response

    if report.status == Report.PROCESSING:
        return JsonResponse({"message": "Report is still processing"}, status=202)
    return JsonResponse({"error": "Report file not found"}, status=404)