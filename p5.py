import paramiko 
#ip address and ssh port of my xiaomi cleaner
host = '192.168.0.156'
port = 22
#user and passwd
user = 'cleaner'
secret = 'cleaner'
#create instance of ssh client
client = paramiko.SSHClient()
#will allow fetch missing keys in auto mode
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#connect to cleaner
client.connect(hostname=host, username=user, password=secret, port=port)
#exec command - service dnsmasq status, to get status of dnsmasq
stdin, stdout, stderr = client.exec_command('service dnsmasq status')
#readout output buffers
data = stdout.read() + stderr.read()
#close connection
client.close()
print(data)