#!/usr/bin/python
#/usr/bin/env python
import os
import sys
from contextlib import closing

from paramiko import SSHConfig, SSHClient

from config_parser import config
ftp_host = config.get("FTP", "ftp_host")
ftp_remote = config.get("FTP", "ftp_remote")
ftp_username = config.get("FTP", "ftp_username")
ftp_pkey = config.get("FTP", "ftp_pkey")

config = SSHConfig()
with open(os.path.expanduser('~/.ssh/config')) as config_file:
    config.parse(config_file)
d = config.lookup(ftp_host)

# connect
with closing(SSHClient()) as ssh:
    ssh.load_system_host_keys() #NOTE: no AutoAddPolicy() 
    #import pdb; pdb.set_trace()
    #ssh.connect(d['asa-proc.phx.llnw.net'], username=d.get('msulym@llnw.com'))
    ssh.connect(ftp_host, username=ftp_username, key_filename=key_filename)
    with closing(ssh.open_sftp()) as sftp:
        # cd into remote directory
        sftp.chdir(remote)
        # cd to local destination directory
        os.chdir(destdir)
        # download all files in it to destdir directory
        for filename in sftp.listdir():
            sftp.get(filename, filename)