from tools.mongodb_tool import MongoDBTool
from tools.external_api_tool import ExternalAPI

class SupportAgent:
    def __init__(self):
        self.db_tool = MongoDBTool()
        self.api_tool = ExternalAPI()

    def handle_query(self, prompt: str):
        if "class" in prompt and "available" in prompt:
            return self.db_tool.get_class_schedule()
        
        elif "order" in prompt and "paid" in prompt:
            order_id = prompt.split("#")[-1].strip()
            status = self.db_tool.get_order_status(order_id)
            return status or f"No order found with ID {order_id}"
        
        elif "create an order" in prompt.lower():
            client = prompt.split("for client ")[-1]
            course = prompt.split("for ")[1].split(" for")[0]
            return self.api_tool.create_order(client, course)
        
        else:
            return "Query not recognized."
