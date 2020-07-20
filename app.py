import boto3 as boto
import botocore

s3 = boto.resource('s3')

source_bucket = 'personal-photos-v1'
destination_bucket = 'personal-photos-v2'
file_to_copy = 'teams.png'
destination_file_name = 'teams.png'

# Check if file exists
try:
    s3.Object(source_bucket, file_to_copy).load()
    copy_source = {
        'Bucket': source_bucket,
        'Key': file_to_copy
    }
    bucket = s3.Bucket(destination_bucket)
    bucket.copy(copy_source, destination_file_name)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        # The object does not exist.
        print("file does not exist in {0}".format(source_bucket))
    else:
        # Something else has gone wrong.
        print(e.response)