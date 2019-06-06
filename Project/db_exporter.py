#!/usr/bin/python
import fnmatch
import os
import MySQLdb
import sys
import csv

from config_parser import config
db_host = config.get("DB", "db_host")
db_user= config.get("DB", "db_user")
db_pass= config.get("DB", "db_pass")

SUPPORTED_DATATYPES = {'int': 'INT', 'str': 'TEXT', 'float': 'float(53,20)', 'timestamp': 'INT', 'datetime': 'datetime'}
KNOWN_TABLES = []
KNOWN_DBS = []

db = MySQLdb.connect(host=db_host, # The Host
                      user=db_user, # username
                      passwd=db_pass) # password

def create_database_if_not_exist(database):
    """Creating the DB if it's not exist"""
    if not database in KNOWN_DBS:
        cursor = db.cursor()
        query = 'CREATE DATABASE IF NOT EXISTS `{}`'.format(database)
        print "Executing: {}".format(query)
        cursor.execute(query)
        db.commit()
        KNOWN_DBS.append(database)

def create_table_if_not_exist(database, tname, columns, data_format):
    """ Create table if not exist """
    # Do nothing if it's the same table we already created
    if not tname in KNOWN_TABLES:
        cursor = db.cursor()
        query = 'use `{}`'.format(database)
        print 'Executing: {}'.format(query)
        cursor.execute(query)
        query = 'CREATE TABLE IF NOT EXISTS `{0}` (`created_date` datetime NOT NULL'.format(tname)
        for column, type_name in zip(columns, data_format):
            query += ', `{0}` {1}'.format(column, SUPPORTED_DATATYPES[type_name])
        query += ')'
        print "Executing: {0}".format(query)
        cursor.execute(query)
        db.commit()
        KNOWN_TABLES.append(tname)

def get_files_from_folder(folder_path):
    """ Return list of all *_data.csv files """
    files = []
    for f in os.listdir(folder_path):
        if fnmatch.fnmatch(f, '*data.csv'):
            print 'Adding {0} into the list'.format(f)
            files.append(f)
    return files

def split_file_name(fname):
    """Convert file name into customer, datetime and suffix"""
    database, table, datetime, suffix = fname.split('-', 3)
    # convert YY-MM-DD to YYYY-MM-DD HH:MM:SS
    yy,mm,dd = datetime.split('.')
    datetime = '20{0}:{1}:{2} 00:00:00'.format(yy,mm,dd)
    return database, table, datetime, suffix

def get_file_context(fpath):
    """ Get file context """
    f = open(fpath, 'r')
    # Read lines from file
    context = csv.reader(f)
    columns = context.next()
    # Get headers and data
    #columns = context[0].strip().split(',')
    # Strip spaces if any:
    #for i in range(len(columns)):
    #    columns[i] = columns[i].lstrip().rstrip()
    #data = map(float, context[1].strip().split(','))
    data = []
    for row in context:
        data.append(row)
    f.close()
    return data, columns

def insert_data_if_new(database, table, datetime, data):
    """Insert data into DB if not exist"""
    cursor = db.cursor()
    query = 'use `{}`'.format(database)
    print 'Executing: {}'.format(query)
    cursor.execute(query)

    # Check if record exist
    query = "SELECT * FROM `{0}` WHERE `created_date` = '{1}' limit 1".format(table, datetime)
    print "Executing: {0}".format(query)
    cursor.execute(query)
    q_data = cursor.fetchone()
    if q_data:
        print "INFO: Record for date: {0} alreday exists, skipping...".format(datetime)
        return

    # Insert data
    print "INFO: Adding new record for datetime: {0}".format(datetime)
    for record in data:
        insert_query = "INSERT INTO `{0}` VALUES (DATE('{1}')".format(table, datetime)
        for value in record:
            insert_query += ", '{0}'".format(MySQLdb.escape_string(value.lstrip().rstrip()))
        insert_query += ")"
        print "Executing: {0}".format(insert_query)
        cursor.execute(insert_query)
        db.commit()

def validate_format(data_format):
    for item in data_format:
        if item not in SUPPORTED_DATATYPES:
            print "ERROR: Unsupported data type {}.\nUse one of: {}".format(item, SUPPORTED_DATATYPES)
            sys.exit(1)

if __name__ == '__main__':
    #if len(sys.argv) < 3:
    #    print "Usage: test_db_exporter.py <data-folder> <format>"
    #    sys.exit(1)
    folder_path = sys.argv[1]
    data_format = sys.argv[2].split(',')
    validate_format(data_format)

    # Get list of files
    files = get_files_from_folder(folder_path)

    # For each file - get data and insert into db
    for fname in files:
        print "Working with file {0}".format(fname)
        database, table, datetime, suffix = split_file_name(fname)
        create_database_if_not_exist(database)
        data, columns = get_file_context(os.path.join(folder_path, fname))
        #check amount of format specification and data infput
        if len(columns) != len(data_format):
            print "ERROR: The CSV file data columns amount not equal to the format specification. File: {}".format(fname)
            sys.exit(1)
        create_table_if_not_exist(database, table, columns, data_format)
        insert_data_if_new(database, table, datetime, data)
    db.close()
    print "Done"