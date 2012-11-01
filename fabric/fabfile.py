from fabric.api import local

def hello(name='World'):
	print("Hello %s!" % name)

def view_dir():
	local('ls -all')

def main(name=''):
	hello(name)
	view_dir()
