# sms_endpoint
A small service that accepts POST requests and notifies a set of preconfigured phone numbers by sms.

## Configuration checklist
1. create IAM role and configure **write** access to CloudWatch Logs and SNS
1. setup SNS topic and subscribe mobile numbers to it
1. change TopicARN in the script
1. use the wizard to create a Lambda function that is triggered by API Gateway
1. ????
1. PROFIT!!! 

