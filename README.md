# Multi-Agent Backend for Fitness Center

This project implements a backend system using FastAPI and MongoDB. It simulates two intelligent agents to handle user support and business analytics for a fitness center.

## Overview

### Support Agent

Handles:

- Client queries (e.g., available classes)
- Order status checks
- Simulated order creation

### Dashboard Agent

Handles:

- Revenue reporting
- Attendance percentage metrics

## Folder Structure

AgentsBackend/
│
├── agents/ # Agent logic
│ ├── support_agent.py
│ └── dashboard_agent.py
│
├── tools/ # Database/API tools
│ ├── mongodb_tool.py
│ └── external_api_tool.py
│
├── api/ # FastAPI routing
│ ├── handlers.py
│ └── schemas.py
│
├── database/ # MongoDB connection & data seeding
│ ├── connection.py
│ └── sample_data.py
│
├── main.py # FastAPI app entry point
├── requirements.txt # Project dependencies
└── README.md # Project overview and instructions

## Setup Instructions

### 1. Clone the Repository and Set Up Virtual Environment

```bash
git clone <your-repo-url>
cd multi_agent_backend
python -m venv venv
```

2. Activate the Environment
   Windows:

```bash
.\venv\Scripts\Activate.ps1
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Start MongoDB
   Ensure MongoDB is running locally at mongodb://localhost:27017. You can also update the URI in database/connection.py if using MongoDB Atlas.

5. Seed Sample Data
   In a Python shell:

```python
from database.connection import get_db
db = get_db()
db.payments.drop()
db.attendance.drop()

from database.sample_data import seed_data
seed_data()
```

6. Run the Application

```bash
python main.py
```

Open in browser: http://127.0.0.1:8000/docs

API Endpoints
Endpoint Query Example Description
/support What classes are available this week? Returns upcoming class schedule
/support Has order #12345 been paid? Returns payment status
/support Create an order for Yoga Beginner for client Priya Sharma Simulates order creation
/dashboard How much revenue did we generate this month? Returns total revenue
/dashboard What is the attendance percentage for Yoga Beginner? Returns attendance percentage

# Tech Stack

Python

FastAPI

MongoDB

PyMongo

Uvicorn
