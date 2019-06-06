#!/usr/bin/python
import boto3
import os
#def retreave(client, resource, dist, s3_local, s3_bucket):
#def retreave(client, resource):
def retreave():
    client = boto3.client('s3')
    resource = boto3.resource('s3')
    from config_parser import config
    s3_bucket = config.get("S3", "s3_bucket")
    s3_local= config.get("S3", "s3_local")
    s3_remote= config.get("S3", "s3_remote")
    paginator = client.get_paginator('list_objects')
    for result in paginator.paginate(Bucket=s3_bucket, Delimiter='/', Prefix=s3_remote):
        if result.get('CommonPrefixes') is not None:
            for subdir in result.get('CommonPrefixes'):
                retreave(client, resource, subdir.get('Prefix'), s3_local, s3_bucket)
        for file in result.get('Contents', []):
            try:
                print("Working with file \n {0}".format(file))
                dest_pathname = os.path.join(s3_local, file.get('Key'))
                if not os.path.exists(os.path.dirname(dest_pathname)):
                    os.makedirs(os.path.dirname(dest_pathname))
                if not file.get('Key').endswith('/'):
                    resource.meta.client.download_file(s3_bucket, file.get('Key'), dest_pathname)
            except KeyboardInterrupt:
                print("Stopping the upload of current file")
