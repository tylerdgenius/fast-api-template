from fastapi import FastAPI
from uvicorn import run
from config.env import Environment

class Api:
    def __init__(self):
        env = Environment()
        self.host = env.get_env("HOST")
        self.port = env.get_env("PORT")
        self.log_level = env.get_env("LOG_LEVEL")

        self.app = FastAPI(title='FastAPI Template', 
                           description='A template for FastAPI applications',
                           version='1.0.0')
        print("Initializing API...")

    def serve_app(self):
        run(self.app, host=self.host, port=int(self.port), log_level=self.log_level)
        print(f"Serving app on {self.host}:{self.port} with log level {self.log_level}")