import paramiko

ip="x.x.x.x"
username="archidote"
ssh = paramiko.SSHClient()
ssh.connect(ip, username=username)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("echo 123 > /tmp/test.txt")
