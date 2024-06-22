import requests

# Replace with your own access token and endpoint
access_token = 'IGQWRPbWc4M3NGbnVOV19QQTJwUDRRWDNjWjByNjNESzJKVXJtaEU1NHhpU3hBakUtY0ZAROEljVXk3dGthOVBvdGlyLWtWWjFwQjdacGNVX1hnSlJmUHBpcVlZANDFPV0xFWWttTlFqaVEwVW5yQVMza21aRnVMSncZD'
endpoint = 'https://graph.instagram.com/me/media'

# Send GET request
params = {
    'access_token': access_token
}
response = requests.get(endpoint, params=params)

# Check response status
if response.status_code == 200:
    data = response.json()
    # Process fetched data
    print(data)
else:
    print(f'Error fetching data: {response.status_code}')
