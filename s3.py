import boto3

vsvv = boto3.client('s3', region_name="us-east-1")
response = vsvv.create_bucket(
Bucket='1q2w3e4r5t6y',
    )
