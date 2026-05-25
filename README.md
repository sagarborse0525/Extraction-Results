# 📄 AWS Resume Processing Pipeline

> Automatically extract structured data from PDF resumes using AWS Lambda, LangChain, and Ollama LLM — serverless, scalable, and fully event-driven.

![Architecture](Resume_drawio.png)

---

## 🏗️ Architecture Overview

```
User (PDF) → S3 Bucket → [S3 Event: ObjectCreated] → AWS Lambda
                                                          ├── LangChain Framework
                                                          ├── Ollama LLM Model
                                                          └── Extract Resume Fields
                                                               └──→ Amazon DynamoDB
```

### Services Used

| Service | Role |
|---|---|
| **Amazon S3** | Stores uploaded PDF resumes; triggers Lambda on upload |
| **AWS Lambda** | Serverless compute; runs LangChain + Ollama to process resumes |
| **LangChain** | Framework for document loading, chunking, and LLM chaining |
| **Ollama LLM** | Local LLM model for extracting structured resume fields |
| **Amazon DynamoDB** | NoSQL database storing extracted resume data |
| **Lambda Layer** | Packages LangChain, Ollama client, and dependencies |
| **IAM Role / Policy** | Grants Lambda permissions to access S3 and DynamoDB |

---

## 🚀 Features

- **Event-driven**: S3 `ObjectCreated` trigger automatically invokes Lambda on every upload
- **Serverless**: No servers to manage — Lambda scales automatically
- **LLM-powered extraction**: Uses Ollama LLM via LangChain to extract structured fields
- **Structured storage**: Extracted data stored as items in DynamoDB for easy querying
- **Modular**: Lambda Layer keeps dependencies separate and reusable

---

## 📁 Project Structure

```
resume-pipeline/
├── lambda_function.py
├── llm_model.py
├── pdf_extract.py
├── prompts.py
├── put_items.py
├── requirements.txt
└── resume_schema.py
```
![Screenshot](images/file_structure.png)

---

## ⚙️ Setup & Deployment

### Prerequisites

- AWS Account
- AWS Lambda
- AWS Bucket
- AWS DynamoDB
- Lambda Role with S3 and DynamoDB access
- Ollama api key(https://ollama.com/settings/keys)

### 1. Create the S3 Bucket
![Screenshot](images/create_bkt.png)

### 2. Build the Lambda Layer

```bash
mkdir python
pip install -r requirements.txt -t python/
zip -r my_layer.zip python
Upload my_layer.zip
```
![Screenshot](images/upload_pkg.png)
```
Create Layer
```
![Screenshot](images/create_layer.png)

### 3. IAM Role
![Screenshot](images/role1.png)

### 4. IAM Policy
![Screenshot](images/role2.png)

### 5. Deploy the Lambda Function

![Screenshot](images/lambda.png)

### 6. Add S3 Trigger

![Screenshot](images/trigger.png)

### 7. Add Layer

![Screenshot](images/layer.png)

### 8. Create DynamoDB Table
![Screenshot](images/table.png)

### 9. Upload python file into lambda function
![Screenshot](images/file.png)
---


---

## 🔐 IAM Policy

Attach this policy to the Lambda execution role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject"],
      "Resource": "arn:aws:s3:::resume-upload-bucket/*"
    },
    {
      "Effect": "Allow",
      "Action": ["dynamodb:PutItem", "dynamodb:GetItem"],
      "Resource": "arn:aws:dynamodb:*:*:table/ResumeData"
    },
    {
      "Effect": "Allow",
      "Action": ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
      "Resource": "*"
    }
  ]
}
```

---

## 🌍 Environment Variables

Set these on your Lambda function:

| Variable | Value |
|---|---|
| `OLLAMA_API_KEY` | `your ollama key` |
| `OLLAMA_BASE_URL` | `https://api.ollama.com` |

![Screenshot](images/env_var.png)

---
