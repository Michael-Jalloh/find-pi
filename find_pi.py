from socket import *

client = socket(AF_INET, SOCK_DGRAM)
client.settimeout(1)
print(client.gettimeout())

print('Please enter your network address')
print('Example:')
print('	192.168.0.1')
ip = input('>>> ')
ip = ip.split('.')
print(ip)
ip = ip[0]+'.'+ip[1]+'.'+ip[2]+'.'
print(ip)

def recv(client):
	try:
		data,addr = client.recvfrom(1024)
		return (data, addr)
	except KeyboardInterrupt:
		exit()
	except:
		return (None,None)
i = 1
while i < 255:
	client.sendto(b'raspberrypi',(ip + str(i),9000))
	print(ip,str(i))
	i += 1
	data,addr = recv(client)
	if data == 'raspberrypi':
		print('Raspberry pi @', addr[0])
		fob = open('raspberrypi.txt','w')
		fob.write(addr[0]+'\n')
		fob.close()
		break

if data == 'None':
	print('No raspberrypi found on your network')

		
	
