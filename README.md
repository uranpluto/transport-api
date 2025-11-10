## Transport Management API Assignment (DRF)

Django REST API for a transport management system focusing on clean architecture, proper API design, and intelligent vehicle assignment.

---

## Overview

This project provides RESTful API endpoints for:

- Managing **Drivers**
- Managing **Vehicles**
- Managing **Orders**
- **Smart Vehicle Assignment**:
  Automatically assigns the most suitable vehicle to an order based on:
  - Vehicle capacity
  - Vehicle and driver availability
  - 2D distance between vehicle and pickup location

---

## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/uranpluto/transport-api.git  
cd transport-api


### 2. VENV

python3.14 -m venv .venv  
source .venv/bin/activate

### 3. Start Django

pip install -r requirements.txt  
python manage.py migrate  
python manage.py loaddata logistics/fixtures/sample_data.json  
python manage.py runserver  

### 4. Check endpoints:

POST/GET http://127.0.0.1:8000/api/drivers/  
POST/GET http://127.0.0.1:8000/api/vehicles/  
POST/GET http://127.0.0.1:8000/api/orders/  
POST     http://127.0.0.1:8000/api/orders/{order_id}/assign-optimal-vehicle/  


### 5. Check doc:  

http://127.0.0.1:8000/api/schema/  
http://127.0.0.1:8000/api/docs/swagger/  
http://127.0.0.1:8000/api/docs/redoc/  
