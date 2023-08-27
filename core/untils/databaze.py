import sqlite3 as sq

global db, cur
db = sq.connect('databaze.db')
cur = db.cursor()


async def add_user(user_id):
    user = cur.execute("SELECT * FROM users WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO users (tg_id) VALUES ({key})".format(key=user_id))
        db.commit()


async def set_active(user_id, active):
    return cur.execute("UPDATE users SET active = ? WHERE tg_id = ?", (active, user_id,))


async def get_users():
    return cur.execute("SELECT tg_id, active FROM users").fetchall()
