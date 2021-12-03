class ClassName:
    def __init__(self):
        pass

    def create():
        return """
        CREATE TABLE IF NOT EXISTS 
        table_name 
        (
            id INTEGER PRIMARY KEY AUTO_INCREMENT,            
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        );
        """

    def drop():
        return """
        DROP TABLE IF EXISTS table_name;
        """
