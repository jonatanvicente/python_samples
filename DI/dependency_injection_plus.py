# Define service classes
class DatabaseService:
    def connect(self):
        return "Database connected"

class EmailService:
    def send_email(self, recipient, message):
        return f"Email sent to {recipient} with message: {message}"

# Define a decorator for dependency injection
def inject_services(*service_classes):
    def decorator(cls):
        def wrapper(*args, **kwargs):
            services = {service_class.__name__: service_class() for service_class in service_classes}
            instance = cls(*args, **kwargs)
            for service_name, service_instance in services.items():
                setattr(instance, service_name.lower(), service_instance)
            return instance
        return wrapper
    return decorator

# Use the decorator to inject the services into a class
@inject_services(DatabaseService, EmailService)
class MyApplication:
    def run(self):
        db_result = self.databaseservice.connect() # lower in the decorator
        email_result = self.emailservice.send_email("user@example.com", "Hello, World!")
        print(db_result)
        print(email_result)

# Create an instance of the class and run the application
app = MyApplication()
app.run()