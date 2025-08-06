from os import environ, stat

class Environment:
    def __init__(self, env_file: str = '.env'):
        self.__load_env(env_file)

    def __validate_envs(self, env_list: list[str] = []):
        for key in env_list:
            if key not in environ.keys():
                raise ValueError(f"Environment variable '{key}' is not set.")
            
    def read_env_file(self, env_file: str):
        if not env_file:
            raise ValueError("Environment file path cannot be empty.")
        if not stat(env_file):
            raise FileNotFoundError(f"Environment file '{env_file}' does not exist.")
        
        with open(env_file) as file:
            for line in file:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split("=", 1)
                    environ[key] = value

    def __load_env(self, env_file):
        self.read_env_file(env_file=env_file)
        self.__validate_envs(env_list=['HOST', 'PORT', 'LOG_LEVEL'])

    def get_env(self, key: str) -> str:
        return environ.get(key, f"Environment variable '{key}' not found.")