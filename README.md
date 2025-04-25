# Django va FastAPI loyihalarini Docker Compose bilan boshqarish  

Ushbu video seriya orqali Django va FastAPI loyihalarini Docker Compose yordamida konteynerlash, deploy qilish va avtomatlashtirishni o‘rganamiz. Har bir dars real loyihalarda ishlatiladigan eng yaxshi amaliyotlarga asoslangan.  

## 📌 Darslar ro‘yxati  

✅ **1. Konteynerlash asoslari**  
   - Docker va Docker Compose tushunchalari  
   - Django loyihalarini konteynerlash  
   - Dockerfile va docker-compose.yml yaratish  

✅ **2. Ko‘p muhitli (multi-environment: dev, qa, prod) sozlash**
   - .env fayllar yordamida konfiguratsiya  
   - Docker Compose orqali turli muhitlarni sozlash  
   - Postgresql va Redis xizmatlarini qo‘shish 

       
   [Ushbu dars agendasi](./2.%20Ko'p%20muhitli%20(multi-environment%3A%20dev%2C%20qa%2C%20prod)%20sozlash/README.md)
   
✅ **3. Celeryda asynchronous (asinxron) va background task yaratish**
   - celeryni sozlash  
   - Asinxron task yaratish
   - Redisni broker sifatida sozlash

       
   [Ushbu dars agendasi](./3.%20Celeryda%20asynchronous%20(asinxron)%20va%20background%20task%20yaratish/README.md)
   
✅ **4. Celery workerni docker compose konteynerga olish**
  - Celery workerni Docker konteynerga olish  
  - Docker Compose orqali Celery workerni ishga tushirish
  - Docker compose multiple projectlar bilan ishlash
  - Celery worker uchun healthcheck yozish
       
  
   [Ushbu dars agendasi](./4.%20Celery%20workerni%20docker%20compose%20konteynerga%20olish/README.md)

✅ **5. RabbitMQni Celery uchun message broker sifatida sozlash**  
   - RabbitMQ va Erlangni Ubuntu tizimiga o‘rnatish  
   - RabbitMQ’ni Celery uchun message broker sifatida sozlash  
   - RabbitMQ’da foydalanuvchi va vhost yaratish  
   - RabbitMQ foydalanuvchisiga ruxsat berish  
   - RabbitMQ HTTP API’ni yoqish  
   - RabbitMQ Management UI orqali navbat va almashinuvni kuzatish

🔲 **6. Django va FastAPI projectlarini real serverda Docker Compose orqali deploy qilish**  
   - Server tayyorlash  
   - Docker Compose yordamida loyihani deploy qilish  
   - Xizmatlarni boshqarish  

🔲 **7. Project xavfsizligini ta'minlash (Throttling, Rate Limiting, CORS)**  
   - Django va FastAPI-da throttling va rate limiting  
   - CORS sozlamalarini to‘g‘ri yo‘lga qo‘yish  
   - Xavfsizlikni mustahkamlash  

🔲 **8. Nginxni sozlash va domen uchun bepul SSL olish**  
   - Nginx orqali trafikni yo‘naltirish  
   - Let's Encrypt bilan bepul SSL olish  
   - HTTPS’ga o‘tish va xavfsiz bog‘lanishni ta’minlash  

🔲 **9. GitHub Actions | Continuous Integration (CI)**  
   - CI/CD tushunchasi  
   - GitHub Actions yordamida avtomatik test va linting  

🔲 **10. GitHub Actions | Continuous Deployment (CD)**  
   - Avtomatik deploy qilish  
   - GitHub Actions va Docker Compose integratsiyasi

🚀 **Yangi videolar qo‘shilgan sari ushbu ro‘yxat yangilanadi. Har bir mavzuda amaliy misollar va kodlar keltiriladi!**  
