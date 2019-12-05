import json
import boto3
import os
import datetime
from botocore.exceptions import ClientError
 

# Pinpoint Project Id
application_id = "6dd52750e1b54397ad258c8827ee7a00"
#region = os.environ['AWS_REGION']
region = 'us-west-2'
client = boto3.client('pinpoint',region_name=region)

def get_segment_id(segment_name):
    try:
        response = client.get_segments(
            ApplicationId=application_id
        )
        segments = response['SegmentsResponse']['Item']
        for segment in segments:
            if segment['Name'] == segment_name:
                segment_id = segment['Id']
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print(segment_id)
        # print(json.dumps(response))
    return segment_id
 
def create_campaign(title, message, segment_id, icon_url, image_url):
    print(segment_id)
    try:
        response = client.create_campaign(
            ApplicationId=application_id,
            WriteCampaignRequest={
                'MessageConfiguration': {
                    'DefaultMessage': {
                        'Action': 'OPEN_APP',
                        'Body': message,
                        'Title': title,
                        'ImageIconUrl': icon_url,
                        'ImageUrl': image_url
                        # 'ImageUrl': 'http://www.earlyadopter.co.kr/wp-content/uploads/2019/11/apple-airpods-pro-early-adopter-review-1.jpg'
                        # 'MediaUrl': 'https://m.media-amazon.com/images/G/01/kindle/merch/2019/ONTHEGO/19951312/PUGE0013_Amazon_Puget_US_REV_2019_45_HD-forDP.mp4?_=1'
                    },
                },
                'Name': title,
                'Description': "Campaign Message", #Can use 'Description' for Category
                'SegmentId': segment_id,
                'Schedule': {
                    'StartTime': "IMMEDIATE"
                    # 'Frequency': 'ONCE',
                    # 'StartTime': datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
                }
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print (json.dumps(response))

        return response
