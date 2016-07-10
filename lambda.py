from __future__ import print_function

import boto3

def lambda_handler(event, context):
    '''forward all incoming requests to SNS
    '''
    print(str(event))
    boto3.client('sns').publish(
        TopicArn='arn:aws:sns:REGION:ACCOUNT_ID:pingonMe',
        Message='Check pingon.me!\n\n%s'.format(str(event))
    )
