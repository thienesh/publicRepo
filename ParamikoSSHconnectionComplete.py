import paramiko


def ssh(cmd):
    ip = "192.168.1.104"
    user = "guest"
    passwd = "Jayathi$"

    try:
        custom_SSH_Client = paramiko.SSHClient()
        custom_SSH_Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        custom_SSH_Client.connect(hostname=ip, username=user, password=passwd)
        stdin, stdout, stderr = custom_SSH_Client.exec_command(cmd)

        output = stdout.read().decode()  # Convert output to string
        print(output)

        custom_SSH_Client.close()
    except paramiko.AuthenticationException:
        print("Authentication failed. Please check the credentials.")
    except paramiko.SSHException as ssh_exception:
        print("Unable to establish SSH connection:", str(ssh_exception))
    except paramiko.Exception as exception:
        print("An error occurred:", str(exception))


if __name__ == '__main__':
    ssh("ls -l")
