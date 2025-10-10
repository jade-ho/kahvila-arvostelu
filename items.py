import db

def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)

    return classes

def add_item(title, description, tags, user_id, classes):
    sql = """INSERT INTO items (title, description, tags, user_id)
            VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, description, tags, user_id])

    item_id = db.last_insert_id()

    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql,[item_id, title, value])

def get_classes(item_id):
    sql = "SELECT title, value FROM item_classes WHERE item_id = ?"
    return db.query(sql, [item_id])

def get_items():
    sql = "SELECT id, title FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.id,
                    items.title,
                    items.description,
                    items.tags,
                    users.id user_id,
                    users.username
            FROM items, users
            WHERE items.user_id = users.id AND
                    items.id = ?"""
    return db.query(sql, [item_id])[0]

def update_item(item_id, title, description, tags):
    sql = """UPDATE items SET title = ?,
                            description = ?,
                            tags = ?
                        WHERE id = ?"""
    db.execute(sql, [title, description, tags, item_id])

def remove_item(item_id):
    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])

def find_items(query):
    sql = """SELECT id, title, tags
            FROM items
            WHERE title LIKE ? OR description LIKE ? OR tags LIKE ?
            ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like, like])