class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
        with open("logs.txt", "a") as f:
            f.write(f"{msg}\n")

try:
    raise CustomException("error")
except CustomException as e:
    print(f"raise {e}")
