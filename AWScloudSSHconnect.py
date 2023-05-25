import paramiko


def ssh(cmd):
    ip = "15.206.123.180"
    user = "ec2-user"

    aws_ssh_client = paramiko.SSHClient()
    #aws_ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    aws_ssh_client.load_host_keys(r"c:\Users\Admin\.ssh\known_hosts")
    aws_ssh_client.connect(hostname=ip, username=user, key_filename= r"c:\Users\Admin\OneDrive\Desktop\RHEL_9.pem")
    stdin, stdout, stderr = aws_ssh_client.exec_command(cmd)

    result = stdout.read().decode()
    print(result)
    aws_ssh_client.close()


ssh("ls")