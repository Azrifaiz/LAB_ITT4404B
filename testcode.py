from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.248.2',  #Your Server IP
    'username': 'azrifaiz19', #your Server Username
    'password': 'Az843172', #your server password
    'port' : 24,
    'secret': 'Prinz Eugen',
}

net_connect = ConnectHandler(**myserver)
output = net_connect.send_command('uname -a')
print(output)
