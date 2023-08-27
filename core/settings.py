from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: int
    feedback_id: int
    payment_id: str


@dataclass()
class Settings:
    bots: Bots


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("BOT_TOKEN"),
            admin_id=env.int("ADMIN_ID"),
            feedback_id=env.int("FEEDBACK_ID"),
            payment_id=env.str("PAYMENT_TOKEN")
        )
    )


settings = get_settings('input')
