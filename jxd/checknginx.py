import requests
import os
if 200 != requests.get('http://127.0.0.1').status_code:
	os.system("service nginx restart")
