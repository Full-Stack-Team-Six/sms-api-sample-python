import requests

phone = "Enter Your Recipient Number"
message = "Enter your message here"
apiKey = "Enter Your API Key Here"

url = 'https://portal.fullstackteamsix.com/api/v1/send/'

x = requests.post(url, data={"key": apiKey, "phone": phone, "message": message}, verify=True)

print(x.text)
