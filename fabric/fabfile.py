from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd
from fabric.contrib.console import confirm
from ssh import SSHClient

def connect_me():
	user = 'ec2-user'
	hosts = 'ec2-50-19-150-120.compute-1.amazonaws.com'
	pkey = '/home/darthlukan/.ssh/testserver.pem'
	s = SSHClient()
	s.connect(hosts, user, pkey)	
	view_remote_dir()
	
def view_remote_dir():
	run('pwd')

def main():
	connect_me()