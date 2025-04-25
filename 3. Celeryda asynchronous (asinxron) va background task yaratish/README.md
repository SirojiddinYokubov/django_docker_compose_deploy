# 📊 Generating Reports in Django using Celery and Pandas

This project demonstrates how to generate reports asynchronously using **Django, Celery, Redis and Pandas**. Reports are processed in the background and stored in Django's **FileField**.

## 🚀 Agenda
- [x] **Create Report model** to store report files
- [x] **Generate reports** using Pandas
- [x] Create POST API to **trigger report generation**
- [x] Create GET API to **fetch report file** as an attachment
- [x] **Setup Celery** in Django
- [x] **Redis as Celery broker** for task management  
- [x] **Create asynchronous report generation task** using Celery
- [x] **Monitor Celery tasks** using Django Admin
