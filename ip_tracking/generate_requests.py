import requests

# Change this to your Django server address
url = "http://127.0.0.1:8000/login/"
num_requests = 120  # More than 100 to trigger anomaly

for i in range(num_requests):
    response = requests.get(url)
    print(f"Request {i+1}: Status {response.status_code}")
