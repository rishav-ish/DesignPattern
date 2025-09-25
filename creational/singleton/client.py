from singleton import Database

def main() -> None:
    database = Database()
    database.connect()
    database.disconnect()
    
    database2 = Database()
    database2.connect()
    database2.disconnect()
    
    print(database is database2)
    
if __name__ == "__main__":
    main() 