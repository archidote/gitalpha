import paramiko

ip="x.x.x.x"
username="archidote"
password="123+aze"
test = "test"
ssh = paramiko.SSHClient()
ssh.connect(ip, username=username)
# ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("echo 'hello world' > /tmp/hello-world.txt")
