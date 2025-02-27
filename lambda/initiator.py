from bs4 import BeautifulSoup
import boto3
from botocore.exceptions import ClientError
#import json


def handle(event, context):
    soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
    print(soup.text)
    print("Hello world!")

    ssm = boto3.client('ssm', region_name='ap-southeast-1')
    response = ssm.get_parameter(
        Name="sg_tickers",
        WithDecryption=True
    )
    
    # Extract the parameter value
    print(response['Parameter']['Value'])
    tickers = response['Parameter']['Value'].split(",")
    for ticker in tickers:
        print(ticker + ".SI")
    

    '''
    # email configurations
    SENDER = "Gangwen <gangwen@yilumi.cn>"
    RECIPIENT = "meigangwen@gmail.com"
    AWS_REGION = "ap-southeast-1"
    SUBJECT = "Amazon SES Test (SDK for Python)"
    BODY_TEXT = ("Amazon SES Test (Python)\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto)."
            )
    BODY_HTML = """<html>
                <head></head>
                    <body>
                    <h1>Amazon SES Test (SDK for Python)</h1>
                    <p>This email was sent with
                        <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
                        <a href='https://aws.amazon.com/sdk-for-python/'>
                        AWS SDK for Python (Boto)</a>.</p>
                    </body>
                </html>"""
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region
    client = boto3.client('ses',region_name=AWS_REGION)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
    '''