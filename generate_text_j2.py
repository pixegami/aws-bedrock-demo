import boto3
import json

prompt_data = """
Write a one-liner 90s style B-movie horror/comedy pitch about 
a giant man-eating Python, with a hilarious and surprising twist.
"""

bedrock = boto3.client(service_name="bedrock-runtime")
payload = {
    "prompt": prompt_data,
    "maxTokens": 512,
    "temperature": 0.8,
    "topP": 0.8,
}

body = json.dumps(payload)
model_id = "ai21.j2-mid-v1"
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json",
)

response_body = json.loads(response.get("body").read())
response_text = response_body.get("completions")[0].get("data").get("text")
print(response_text)
