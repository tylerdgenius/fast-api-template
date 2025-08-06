from os import environ

class Environment:
    def __init__(self):
        self.envs_keys = list(environ.keys())
        self.env = []

    def __validate_envs(self, env_list: list[str] = []):
        for key in env_list:
            if key not in self.env_keys:
                raise ValueError(f"Environment variable '{key}' is not set.")
            
    def get_env(self, key: str, default: str = None) -> str:
        self.__validate_envs(env_list=[key])
        if key in self.env_keys:
            return self.envs_keys[key]
        else:
            raise KeyError(f"Environment variable '{key}' not found.")
            

