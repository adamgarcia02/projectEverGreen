#!/usr/bin/python3

from ftplib import FTP

def fileUpload_temp(filename, SERVER, USERNAME, PASSWORD):
    # connection to server
    ftp = FTP(SERVER)
    # server login credentials
    ftp.login(USERNAME, PASSWORD)
    # change directory
    ftp.cwd('temperature')
    # open file and store on server
    with open(filename, 'rb') as t:
        ftp.storlines('STOR %s' % filename, t)
    # quit
    ftp.quit()

def fileUpload_humidity(filename, SERVER, USERNAME, PASSWORD):
    # connection to server
    ftp = FTP(SERVER)
    # server login credentials
    ftp.login(USERNAME, PASSWORD)
    # change directory
    ftp.cwd('humidity')
    # open file and store on server
    with open(filename, 'rb') as t:
        ftp.storlines('STOR %s' % filename, t)
    # quit
    ftp.quit()

def fileUpload_pressure(filename, SERVER, USERNAME, PASSWORD):
    # connection to server
    ftp = FTP(SERVER)
    # server login credentials
    ftp.login(USERNAME, PASSWORD)
    # change directory
    ftp.cwd('pressure')
    # open file and store on server
    with open(filename, 'rb') as t:
        ftp.storlines('STOR %s' % filename, t)
    # quit
    ftp.quit()



