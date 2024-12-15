import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


def pegar_conexao():
    
    user = os.getenv('user')
    password = os.getenv('password')
    host = os.getenv('host')
    port = os.getenv('port')
    database = os.getenv('database')

    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

    return engine
