import db

def add_item(title, description, tags, user_id):
    sql = """INSERT INTO items (title, description, tags, user_id)
            VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, description, tags, user_id])