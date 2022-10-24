from hashids import Hashids
from dataclasses import dataclass
from dotenv import dotenv_values


@dataclass
class Envs:
    token: str
    sudo_password: str = 'jesus'
    hash_salt: str = 'gzuz'


envs = Envs(**dotenv_values('.env'))
hash_ids = Hashids(salt=envs.hash_salt)


def is_sudo(passwd):
    return envs.sudo_password == passwd


def sudo_hash():
    return hash_ids.encode(envs.sudo_password)
