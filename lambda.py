import json

def lambda_handler(event, context):
    #print(event)
    bot_message = 'Application under development. Search functionality will be implemented in Assignment 2'
    return {
        "messages":[{"type":"unstructured","unstructured":{"text":"Application under development. Search functionality will be implemented in Assignment 2"}}]}
