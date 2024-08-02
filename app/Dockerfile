# Use the official AWS Lambda Python base image
FROM --platform=linux/amd64 public.ecr.aws/lambda/python:3.8

COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "main.handler" ]