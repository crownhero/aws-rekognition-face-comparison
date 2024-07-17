#!/bin/bash

# Variables
TEMPLATE_FILE="/Users/mac/downloads/python-rekognition/sam-template.yml"
PACKAGED_TEMPLATE_FILE="packaged-template.yml"
S3_BUCKET="aws-sam-cli-managed-default-samclisourcebucket-sqpvz37f4kqg"
STACK_NAME="sam-face-comparison"

# Build the application
sam build -t $TEMPLATE_FILE

# Package the application
sam package --s3-bucket $S3_BUCKET --output-template-file $PACKAGED_TEMPLATE_FILE

# Deploy the application
sam deploy --template-file $PACKAGED_TEMPLATE_FILE --stack-name $STACK_NAME --capabilities CAPABILITY_IAM
