from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.248.4',  #Your Server IP
    'username': 'azrifaiz19', #your Server Username
    'password': 'Az843172', #your server password
    'port' : 22,
    'secret': '',
}

net_connect = ConnectHandler(**myserver)
output = net_connect.send_command('uname -a')
print(output)


