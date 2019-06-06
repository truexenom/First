#!/usr/bin/python
import configparser
import sys,os


def createConfig(path):
    """
    Create a config file
    """
    path = (os.path.dirname(sys.argv[0])+"/config.cfg") 
    config = configparser.ConfigParser()
    config.add_section("FTP")
    config.set("FTP", "ftp_host", "Default")
    config.set("FTP", "ftp_remote", "/")
    config.set("FTP", "ftp_username", "Default")
    config.set("FTP", "ftp_pkey", "Default")
    config.add_section("S3")
    config.set("S3", "s3_bucket", "Default")
    config.set("S3", "s3_local", "/tmp")
    config.set("S3", "s3_remote", "/")
    config.add_section("DB")
    config.set("DB", "db_host", "localhost")
    config.set("DB", "db_user", "root")
    config.set("DB", "db_pass", "root")
    config.add_section("FILE")
    config.set("FILE", "#folder_path", "s3_local+s3_remote")
    config.set("FILE", "data_format", "datetime str int float")
    config.add_section("EMAIL")
    config.set("EMAIL", "email_recipients", "Default")
    config.set("EMAIL", "email_subject", "Default")
    config.set("EMAIL", "email_sender", "Default")
    config.set("EMAIL", "email_body", "Default")
    config.set("EMAIL", "email_logfile", "Default.log")
    config.set("EMAIL", "email_server", "mail.google.com")
    config.set("EMAIL", "email_port", "587")
    
    with open(path, "w") as config_file:
        config.write(config_file)
    print "CFG file created, terminating"
    sys.exit(1)
 
def crudConfig():
    """
    Create, read, update, delete config
    """
    path = (os.path.dirname(sys.argv[0])+"/config.cfg") 
    if not os.path.exists(path):
        createConfig(path)
    
    config = configparser.ConfigParser()
    config.read(path)
  
    ftp_host = config.get("FTP", "ftp_host")
    ftp_remote = config.get("FTP", "ftp_folder")
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
    

    #config.set("Settings", "font_size", "12")
    
    #config.remove_option("Settings", "font_style")
 
    #with open(path, "w") as config_file:
    #   config.write(config_file)
 
 

if __name__ == "__main__": 
    crudConfig()


#-----duplicate for using method
path = (os.path.dirname(sys.argv[0])+"/config.cfg") 
if not os.path.exists(path):
    createConfig(path)

config = configparser.ConfigParser()
config.read(path)


