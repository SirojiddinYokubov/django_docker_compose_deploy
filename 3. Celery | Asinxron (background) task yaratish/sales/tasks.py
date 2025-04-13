import logging

from celery import shared_task
import pandas as pd
import time
import io
from django.core.files.base import ContentFile
from .models import Report

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@shared_task
def generate_sales_report(report_id):
    logger.info("Generating report %s started", report_id)
    report = Report.objects.get(id=report_id)
    report.status = Report.PROCESSING
    report.save()

    try:
        time.sleep(60)

        logger.info("Step 1: Fetching data from database")
        data = {
            "Order ID": [1, 2, 3, 4, 5],
            "Customer": ["Alice", "Bob", "Charlie", "Alice", "Eve"],
            "Total ($)": [120, 250, 180, 300, 150],
        }

        logger.info("Step 2: Creating DataFrame")
        df = pd.DataFrame(data)

        logger.info("Step 3: Saving DataFrame to CSV")
        buffer = io.StringIO()
        df.to_csv(buffer, index=False)
        buffer.seek(0)

        logger.info("Step 4: Saving CSV to file")
        file_name = f"sales_report_{report_id}.csv"
        report.file.save(file_name, ContentFile(buffer.getvalue()))

        logger.info("Step 5: Saving report status")
        report.status = Report.COMPLETED
        report.save()
        logger.info("Generated report %s completed", report_id)

        return f"Generated report {report_id} completed"
    except Exception as exc:
        report.status = Report.FAILED
        report.save()
        logger.error("Failed to generate report %s: %s", report_id, exc, exc_info=True)

        return f"Failed to generate report {report_id}: {exc}"