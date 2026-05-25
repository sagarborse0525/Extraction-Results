import boto3
import os

dynamodb = boto3.resource('dynamodb')


def put_item(item):
    """ Put resume extracted keys and values"""

    table = dynamodb.Table('resume_table')
    response = table.put_item(Item=item)
    return response