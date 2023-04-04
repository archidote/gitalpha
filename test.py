import paramiko

ip="192.168.5.3"
username="archidote"
password="123+aze"
api_token="dsgfsg546ds4gf65fds4g5fd4s5dgdgf51fdg545q"
path="/var/www/html"
test = "test"
ssh = paramiko.SSHClient()
ssh.connect(ip, username=username)
# ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("echo 'hello world' > /tmp/hello-world.txt")
