import requests
import shutil

r = requests.get('https://static.pexels.com/photos/126407/pexels-photo-126407.jpeg', stream=True)
print(r.status_code)
if r.status_code == 200:
    with open("img.jpeg", 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
