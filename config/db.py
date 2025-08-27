import os
from sqlalchemy import create_engine, text
from config.env import Environment
from sqlalchemy.engine import URL
from typing import Any, Mapping, Optional

class Database(Environment):
    def __init__(self):
        super().__init__()
        self.user = self.get_env("PG_USER")
        self.host = self.get_env("PG_HOST")
        self.password = self.get_env("PG_PASSWORD")
        self.db = self.get_env("PG_DB")
        self.port = self.get_env("PG_PORT")
        sslmode = self.get_env("PG_SSLMODE").strip()

        # query = {"application_name": self.get_env("APP_NAME")}

        # if sslmode:
        #     query["sslmode"] = sslmode

        url = URL.create(
                    drivername="postgresql+psycopg",
                    username=self.user,
                    password=self.password,
                    host=self.host,
                    port=self.port,
                    database=self.db,
                    # query=query,
                )
        
        print(url)

        self.engine = create_engine(
            url, 
            pool_size=10, 
            max_overflow=20, 
            pool_pre_ping=True, 
            pool_recycle=1800,
            pool_use_lifo=True,
        )

    def ping(self, query: str = "SELECT 1", params: Optional[Mapping[str, Any]] = None) -> bool:
        try:
            with self.engine.begin() as conn:
                res = conn.execute(text(query), params or {})
                print(f"Ping result: {res.scalar()}")
                return bool(res.scalar())
        except Exception:
            return False

    def connect(self):
        return self.engine.connect()