# import paramiko
# ip = "192.168.21.135"
# user = "saleem"
# passwd = "12345"
#
# custom_SSH_client = paramiko.SSHClient()      # creating SSh client
# custom_SSH_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())           # for not getting error secure connection
# custom_SSH_client.connect(hostname=ip,username=user,password=passwd)        # for connecting
#
# stdin,stdout,stderr= custom_SSH_client.exec_command("uptime")             # command executing  i,e uptime
#
# print(f"output of command: {stdout.read().decode()}")         # to print the executing command
#
# custom_SSH_client.close()                    # for closing SSH client


import paramiko


def ssh(cmd):
    ip = "192.168.1.104"
    user = "guest"
    passwd = "Jayathi$"

    custom_SSH_Client = paramiko.SSHClient()
    custom_SSH_Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    custom_SSH_Client.connect(hostname=ip, username=user, password=passwd)
    stdin, stdout, stderr = custom_SSH_Client.exec_command(cmd)

    print(f"{stdout.read().decode()}")
    custom_SSH_Client.close()


ssh("ls -l")
