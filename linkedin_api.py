import requests

def publish_to_linkedin(approved_text, access_token, user_urn):
    url = "https://api.linkedin.com/rest/posts"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "LinkedIn-Version": "202603", # Standard stable version
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }
    
    payload = {
        "author": f"urn:li:person:{user_urn}",
        "commentary": approved_text, 
        "visibility": "PUBLIC",      
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": []
        },
        "lifecycleState": "PUBLISHED"
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    # Return the response so FastAPI knows if it succeeded or failed
    if response.status_code == 201:
        return {"status": "success", "message": "Post published to LinkedIn!"}
    else:
        return {"status": "error", "details": response.text}