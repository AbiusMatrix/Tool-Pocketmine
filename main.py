import os
import time
from configure.FileManager import FileManager

name = input("Enter Plugins Name: ")
api = input("Enter API Plugin: ")
version = input("Enter Version Plugin: ")
main = input("Enter Main Plugin: ")
author = input("Enter Author Plugin: ")

FileManager(name, api, version, main, author)