from dotenv import load_dotenv
import os
load_dotenv()

class Setting:
    origin = os.getenv("ORIGIN")
    secret_key = os.getenv("SECRT_KEY")
    db_url = os.getenv("DB_URL")

setting = Setting()
