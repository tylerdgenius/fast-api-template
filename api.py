from fastapi import FastAPI
from uvicorn import run
from config.env import Environment

app = FastAPI()

class Api:
    def __init__(self):
        env = Environment()
        self.host = env.get_env("HOST")
        self.port = env.get_env("PORT")
        self.log_level = env.get_env("LOG_LEVEL")

    def serve_app(self):
        run(app, self.host, self.port, log_level=self.log_level)