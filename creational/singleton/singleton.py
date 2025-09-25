class Database:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance
    
    def connect(self):
        print("Connecting to database")
        
    def disconnect(self):
        print("Disconnecting from database")
        