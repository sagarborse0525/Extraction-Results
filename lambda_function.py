import json
import urllib.parse
import logging
import os
import base64
import boto3
from resume_schema import ResumeParser
from llm_model import model
from prompts import system_prompt
from put_items import put_item
from pdf_extract import extract_resume_text
from langchain.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()


# Configure logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    local_file_path = f"/tmp/{os.path.basename(key)}"
    # print(f" Bucket Name: {bucket}")
    # print(f"Key name: {key}")
    # print(f"Path name: {local_file_path}")

    s3 = boto3.client('s3')

    s3.download_file(bucket, key, local_file_path)
    
    resume_context = extract_resume_text(local_file_path)

    
    llm = model()

    structured_output = llm.with_structured_output(ResumeParser)

    result = structured_output.invoke(
        [
            SystemMessage(content=system_prompt),
            HumanMessage(content=resume_context)
        ]
    )
    res = put_item(result.model_dump())
    
    return res


