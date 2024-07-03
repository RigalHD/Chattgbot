import asyncpg
import os

class DataBase:
    def __init__(self) -> None:
        pass
    
    async def connect(self):
        connection = await asyncpg.connect(
            host="localhost",
            database="chat_tg_bot_db",
            user="postgres",
            password=os.getenv("database_password"),
            port=5432,
        )
        return connection
    

class UsersTable(DataBase):
    def __init__(self) -> None:
        super().__init__()
    
    async def create_table(self):
        connection: asyncpg.Connection = await self.connect()
        await connection.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                telegram_id BIGINT,
                username TEXT DEFAULT NULL,
                first_name TEXT DEFAULT NULL,
                last_name TEXT DEFAULT NULL,
                phone_number TEXT,
                permissions_level INTEGER DEFAULT 0,
                registation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            )
        await connection.close()

    async def register_user(
            self, 
            telegram_id: int,
            phone_number: str,
            username: str = "", 
            first_name: str = "", 
            last_name: str = "",
            ):
        try:
            connection: asyncpg.Connection = await self.connect()
            await self.create_table()
            await connection.execute(
                """
                INSERT INTO users (telegram_id, phone_number, username, first_name, last_name) 
                VALUES ($1, $2, $3, $4, $5)
                """, telegram_id, phone_number, username, first_name, last_name
            )
        except Exception as e:
            print(e)

        finally:
            await connection.close()

    async def check_user(self, telegram_id: int):
        try:
            connection: asyncpg.Connection = await self.connect()
            exists = await connection.fetchval(
                """
                SELECT EXISTS(SELECT 1 FROM users WHERE telegram_id = $1)
                """, telegram_id
             )
            return bool(exists)
        except Exception as e:
            print(e)
        finally:
            await connection.close()

