from database.connection import get_db
from bson import ObjectId

def bson_to_dict(doc):
    """
    Converts BSON document to JSON-serializable dict
    by converting ObjectId to str.
    """
    if not doc:
        return doc
    doc = dict(doc)
    if "_id" in doc and isinstance(doc["_id"], ObjectId):
        doc["_id"] = str(doc["_id"])
    return doc

class MongoDBTool:
    def __init__(self):
        self.db = get_db()

    def find_client(self, keyword):
        result = self.db.clients.find_one({
            "$or": [
                {"name": keyword},
                {"email": keyword},
                {"phone": keyword}
            ]
        })
        return bson_to_dict(result)

    def get_order_status(self, order_id):
        query = {
            "$or": [
                {"order_id": order_id},
                {"order_id": int(order_id)} if order_id.isdigit() else {}
            ]
        }
        result = self.db.orders.find_one(query)
        return bson_to_dict(result)

    def get_class_schedule(self):
        classes = self.db.classes.find({"status": "upcoming"})
        return [bson_to_dict(cls) for cls in classes]

    def get_revenue(self):
        payments = self.db.payments.find({"status": "paid"})
        return sum(p.get("amount", 0) for p in payments)

    def get_attendance_stats(self, course_name):
        record = self.db.attendance.find_one({"class": course_name})
        if not record:
            return None
        return (record['attended'] / record['total']) * 100
