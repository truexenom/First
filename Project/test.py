#!/usr/bin/python
from config_parser import config
data_format= (config.get("FILE", "data_format")).split()
print(data_format)