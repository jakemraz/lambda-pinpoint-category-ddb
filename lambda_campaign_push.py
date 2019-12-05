import json
import boto3
import jhb_pinpoint as pinpoint
import jhb_ddb as ddb
import dateutil.parser

def lambda_handler(event, context):
    
    params = event
 
    # Query parmeters
    title = params["title"]
    message = params["message"]
    category = params["category"]
    segment = params["segment"]
    icon_url = params["icon"]
    image_url = params["image"]

    # send push message
    segment_id = pinpoint.get_segment_id(segment)
    response = pinpoint.create_campaign(title, message, segment_id, icon_url, image_url)

    # insert category
    campaign_id = response['CampaignResponse']['Id']
    create_date = response['CampaignResponse']['CreationDate']
    create_timestamp = int(dateutil.parser.parse(create_date).timestamp())
    item = {
        "category": category,
        "event_time": create_timestamp,
        "campaign_id": campaign_id
    }
    ddb_response = ddb.put_item(item)
    print(ddb_response)
    
    return {
        'statusCode': 200,
        'body': json.dumps({'result': response}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }