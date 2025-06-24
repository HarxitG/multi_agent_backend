from .connection import get_db

def seed_data():
    db = get_db()
    
    db.clients.insert_one({"name": "Priya Sharma", "email": "priya@example.com", "phone": "1234567890"})
    db.courses.insert_one({"title": "Yoga Beginner", "instructor": "Anjali", "status": "upcoming"})
    db.classes.insert_one({"course": "Yoga Beginner", "date": "2025-06-25", "instructor": "Anjali", "status": "upcoming"})
    db.orders.insert_one({"client": "Priya Sharma", "course": "Yoga Beginner", "status": "pending", "order_id": "12345"})
    
    # Changed status from "unpaid" to "paid" here
    db.payments.insert_one({"order_id": "12345", "amount": 300, "status": "paid"})
    
    db.attendance.insert_one({"class": "Yoga Beginner", "attended": 8, "total": 10})

    print("✅ Sample data inserted!")
