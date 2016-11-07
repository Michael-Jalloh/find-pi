from socket import *

client = socket(AF_INET, SOCK_DGRAM)
client.settimeout(1)
print client.gettimeout()

print 'Please enter your network address'
print 'Example:'
print '	192.168.0.1'
ip = raw_input('>>> ')
first,second,third,fourth = ip.split('.')
print ip
ip = first+'.'+second+'.'+third+'.'
print ip
def recv(client):
	try:
		data,addr = client.recvfrom(1024)
		return (data, addr)
	except:
		return (None,None)
i = 1
while i < 255:
	client.sendto('raspberrypi',(ip+`i`,9000))
	print ip+`i`
	i += 1
	data,addr = recv(client)
	if data == 'raspberrypi':
		print 'Raspberry pi @', addr[0]
		fob = open('raspberrypi.txt','w')
		fob.write(addr[0]+'\n')
		fob.close()
		break
if data == 'None':
	print 'No raspberrypi found on your network'

		
	
