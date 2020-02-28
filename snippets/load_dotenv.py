from dotenv import load_dotenv
import os

load_dotenv()
database = os.getenv('DATABASE')
print(database)


# .env file
DATABASE=Sanple_connection_string
