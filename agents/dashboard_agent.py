from tools.mongodb_tool import MongoDBTool
import string  # <-- new import for punctuation stripping

class DashboardAgent:
    def __init__(self):
        self.db_tool = MongoDBTool()

    def handle_query(self, prompt: str):
        # Remove trailing punctuation (like '?' or '.')
        prompt = prompt.strip().rstrip(string.punctuation)
        
        if "revenue" in prompt:
            return {"total_revenue": self.db_tool.get_revenue()}
        elif "attendance" in prompt:
            # Extract course name after 'for ', safely without trailing punctuation
            course = prompt.split("for ")[-1].strip()
            percentage = self.db_tool.get_attendance_stats(course)
            return {"attendance": f"{percentage:.2f}%"} if percentage else "No data"
        else:
            return "Query not supported"
