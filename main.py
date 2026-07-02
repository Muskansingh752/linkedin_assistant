from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from generator import generate_linkedin_draft
from linkedin_api import publish_to_linkedin

load_dotenv(override=True)


app = FastAPI(title='Linkedin AI Assistant')

temporary_database = {
    "latest_draft":None
}


@app.get("/")
def read_root():
    return {"status": "system is online and ready "}

@app.get("/draft-post")
def draft_linkendin_post(topic:str="post you want to generate.."):
    try:
        ai_generated_draft = generate_linkedin_draft(topic)
        temporary_database["latest_draft"]=ai_generated_draft
        return{
            "status":"draft generated",
            "post_content": ai_generated_draft,
            "action_required":"please approve"
    }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/publish-post")
def publish_approved_post():

    draft_to_publish  =temporary_database.get("latest_draft")

    if not draft_to_publish:
        raise HTTPException(status_code=400, detail="no draft found..")
    

    my_access_token = os.getenv("LINKEDIN_ACCESS_TOKEN")
    my_urn = os.getenv("LINKEDIN_URN")

    if not my_access_token or not my_urn:
        raise HTTPException(status_code=500, detail="linkedin credentials missing. ")
    
    try:
        result =publish_to_linkedin(draft_to_publish,my_access_token,my_urn)
        temporary_database["latest_draft"]=None

        return {"status":"success! posted to Linkedin.","Linkedin_response":result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
