#!/usr/bin/python
#----------config parser#
import configparser
import sys,os

from config_parser import createConfig
print("--->Reading config file")
"""
Create, read, update, delete config
"""
path = (os.path.dirname(sys.argv[0])+"/config.cfg") 
if not os.path.exists(path):
    createConfig(path)

config = configparser.ConfigParser()
config.read(path)

ftp_host = config.get("FTP", "ftp_host")
ftp_remote = config.get("FTP", "ftp_remote")
ftp_username = config.get("FTP", "ftp_username")
ftp_pkey = config.get("FTP", "ftp_pkey")
s3_bucket = config.get("S3", "s3_bucket")
s3_local= config.get("S3", "s3_local")
s3_remote= config.get("S3", "s3_remote")
db_host = config.get("DB", "db_host")
db_user= config.get("DB", "db_user")
db_pass= config.get("DB", "db_pass")
folder_path= (s3_local+"/"+s3_remote)
data_format= (config.get("FILE", "data_format")).split()
email_recipients= config.get("EMAIL", "email_recipients")
email_logfile= config.get("EMAIL", "email_logfile")
email_subject= config.get("EMAIL", "email_subject")
email_sender= config.get("EMAIL", "email_sender")
email_body= config.get("EMAIL", "email_body")
email_attachment = (os.path.dirname(sys.argv[0])+"/"+email_logfile)
email_server= config.get("EMAIL", "email_server")
email_port= int(config.get("EMAIL", "email_port"))
print("Done")
#---end of config parser

#---start of s3
from s3_sync import *
print("--->Downloading files from the s3")
retreave()
print("Done")
#---end of s3


#----start of database exporter
from db_exporter import *
#db_exporter(db_host, db_user, db_pass, folder_path, data_format)
print("--->Uploding files to the Database")

#folder_path = "/tmp/s3/data/"
#data_format = ['datetime', 'str', 'str', 'str', 'int', 'float', 'float', 'float', 'str']

validate_format(data_format)

# Get list of files
files = get_files_from_folder(folder_path)

# For each file - get data and insert into db
for fname in files:
    print "Working with file \n {0}".format(fname)
    database, table, datetime, suffix = split_file_name(fname)
    create_database_if_not_exist(database)
    data, columns = get_file_context(os.path.join(folder_path, fname))
    #check amount of format specification and data infput
    if len(columns) != len(data_format):
        print "ERROR: The CSV file data columns amount not equal to the format specification. File: {}".format(fname)
        sys.exit(1)
    create_table_if_not_exist(database, table, columns, data_format)
    try:
        insert_data_if_new(database, table, datetime, data)
    except KeyboardInterrupt:
        print("Stopping the upload of current file")
db.close()
print "Done"
#----end of DB exporter

#---start of email
print("---->Sending an email")
from send_email import *
#email(email_recipients, email_subject, email_sender, email_body, email_attachment, email_server, email_port)
email()
print("done")
#----end of email