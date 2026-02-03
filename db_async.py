import sqlite3
import asyncio

# Asynchronous database helper
async def fetchone(query, params=()):
    loop = asyncio.get_event_loop()
    conn = sqlite3.connect("eventus.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    result = await loop.run_in_executor(None, lambda: cursor.execute(query, params).fetchone())
    conn.close()
    return result

async def fetchall(query, params=()):
    loop = asyncio.get_event_loop()
    conn = sqlite3.connect("eventus.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    result = await loop.run_in_executor(None, lambda: cursor.execute(query, params).fetchall())
    conn.close()
    return result

async def execute(query, params=(), commit=False):
    loop = asyncio.get_event_loop()
    conn = sqlite3.connect("eventus.db")
    cursor = conn.cursor()

    if commit:
        await loop.run_in_executor(None, lambda: cursor.execute(query, params))
        conn.commit()
    else:
        result = await loop.run_in_executor(None, lambda: cursor.execute(query, params).fetchall())
    
    conn.close()
    return result
