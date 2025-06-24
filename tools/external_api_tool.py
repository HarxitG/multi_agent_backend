class ExternalAPI:
    def create_client(self, name, email, phone):
        return {"message": f"Client {name} created."}

    def create_order(self, client, course):
        return {"message": f"Order created for {client} for course {course}"}
