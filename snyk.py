import os
from dotenv import load_dotenv # Common library: pip install python-dotenv

# Load variables from a .env file if it exists
load_dotenv()

class ServiceClient:
    def __init__(self, api_key, db_password):
        # We assign these from environment variables instead of hardcoding strings
        self.api_key = api_key
        self.db_password = db_password

    def connect(self):
        if not self.api_key or not self.db_password:
            print("Error: Missing credentials. Please set environment variables.")
            return
        
        print(f"Successfully authenticated with API Key: {self.api_key[:4]}****")
        print("Connected to the secure database.")

if __name__ == "__main__":
    # Fetching credentials securely
    # In a real scenario, you'd run `export API_KEY='your_secret'` in your terminal
    KEY = os.getenv('API_KEY')
    PWD = os.getenv('DB_PASSWORD')

    client = ServiceClient(api_key=KEY, db_password=PWD)
    client.connect()
