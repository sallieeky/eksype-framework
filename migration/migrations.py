class Migrations:
    def __init__(self):
        pass

    def create():
        return """
        CREATE TABLE IF NOT EXISTS 
        migrations 
        (
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL,
            alamat VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        );
        """

    def drop():
        return """
        DROP TABLE IF EXISTS migrations;
        """
