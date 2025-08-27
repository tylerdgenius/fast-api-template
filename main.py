import uvicorn
from config.env import Environment

def main():
    env = Environment()
    host = env.get_env("HOST")
    port = int(env.get_env("PORT"))
    log_level = env.get_env("LOG_LEVEL")

    print(f"Serving app on {host}:{port} with log level {log_level}")
    uvicorn.run("api.main:app", host=host, port=port, log_level=log_level, reload=env.get_env("RELOAD") == "true")

if __name__ == "__main__":
    main()