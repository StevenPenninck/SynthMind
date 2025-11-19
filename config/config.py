from environs import Env # https://pypi.org/project/environs/

env = Env()
env.read_env()  # leest .env als aanwezig

db_database = env.str("DB_DATABASE")
db_path = env.str("DATABASE_PATH")