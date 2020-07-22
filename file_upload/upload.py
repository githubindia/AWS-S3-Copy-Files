import boto3 as boto
import os.path
import botocore

s3 = boto.resource('s3')

source_bucket = 'personal-photos-v1'
file_to_upload = 'data.json'

if os.path.exists(file_to_upload):
    try:
        # upload_file(file_path, file_name_for_s3)
        s3.Bucket(source_bucket).upload_file(file_to_upload, 'dat.json')
        print("file \"{0}\" is uploaded successfully to S3 bucket".format(file_to_upload))

    except botocore.exceptions.ClientError as e:
        print(e)
else:
    print("File does not exists!")