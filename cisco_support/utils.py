import requests

def getToken(client_id: str, client_secret: str, verify: bool, proxies: dict) -> str:
        url = 'https://id.cisco.com/oauth2/default/v1/token'

        params = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }

        headers = {
            'Content-Type':'application/x-www-form-urlencoded'
        }

        response = requests.post(url=url, params=params, headers=headers, verify=verify, proxies=proxies)
        
        if response is not None:
           
            try:
               
                return response.json()['access_token']
            
            except Exception:
                print(response.json())
        
        return None