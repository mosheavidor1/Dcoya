class ErrorHandling:
    @staticmethod
    def handle_exception(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Exception occurred: {e}")

        return wrapper
