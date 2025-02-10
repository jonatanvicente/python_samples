# Define a simple service class
class Service:
    def perform_action(self):
        return "Service action performed"

# Define a decorator for dependency injection
def inject_service(service_class):
    def decorator(func):
        def wrapper(*args, **kwargs):
            service_instance = service_class()
            return func(service_instance, *args, **kwargs)
        return wrapper
    return decorator

# Use the decorator to inject the Service dependency
@inject_service(Service)
def my_function(service):
    result = service.perform_action()
    print(result)

# Call the function
my_function()