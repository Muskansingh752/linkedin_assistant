import requests
import os 
from dotenv import load_dotenv

load_dotenv(override=True)
token = os.getenv("LINKEDIN_ACCESS_TOKEN")

print(f"\nChecking token starting with: {token[:15]}...")

url = "https://api.linkedin.com/v2/userinfo"
headers = {"Authorization": f"Bearer {token}",
           "LinkedIn-Version": "202401" }

response = requests.get(url,headers=headers)

if response.status_code==200:
    user_data = response.json()
    print("\nSUCCESS! your account is connected.")
    print("your urn id is the value next to 'sub': ")
    print(f"  {user_data.get('sub')}  ")

else:
    print("error:" , response.text)

