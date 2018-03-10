import ntplib
from time import ctime

def print_time():
	ntp_client = ntplib.NTPClient()
	response = ntp_client.request('1.us.pool.ntp.org')
	print (ctime(respsonse.tx_time))

if __name__ == '__main__':
    print_time()
