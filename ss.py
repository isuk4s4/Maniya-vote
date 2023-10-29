import requests
# Set the request headers.
headers = {
  "Cookie": "_ga=GA1.1.936671765.1698556372; _ga_8586FJ874T=GS1.1.1698556371.1.1.1698556513.0.0.0",
  "Content-Type": "application/json",
  "Accept": "application/json, text/plain, */*",
  "Origin": "https://letskfc.gamer.lk",
  "Referer": "https://letskfc.gamer.lk/"
}
from faker import Faker

# Create a Faker object
faker = Faker()

# Generate a random email address
email = faker.email()

# Generate a random name
name = faker.name()

# Generate a random phone number
phone_number = faker.phone_number()

payload = {
  "email": email,
  "name": name,
  "phoneNumber": phone_number,
  "vote": "maniya",
  "device": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
}
print(payload)
# Send the request.
response = requests.post("https://letskfc.gamer.lk/1c3485d7/run-vote/submit-vote", headers=headers, json=payload)
data = response.json()['vote']['verificationCode']

print(data)

url = f"https://letskfc.gamer.lk/1c3485d7/run-vote/verify-vote/{data}";

print(url)
headers2 = {
    'Host': 'letskfc.gamer.lk',
    'Cookie': '_ga=GA1.1.936671765.1698556372; _ga_8586FJ874T=GS1.1.1698556371.1.1.1698563438.0.0.0',
    'Sec-Ch-Ua': '(Not(A:Brand";v="8", "Chromium";v="98"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

    
'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9'
}

# Make the request
response2 = requests.get(url, headers=headers)

print(response2)
