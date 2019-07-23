import os

class RemoteCommand:
	def __init__(self, name, nameUser):
		self.name = name
		self.nameUser = nameUser

	def funkInfo(self):
		data = "net user " + self.nameUser + " /DOMAIN > LOGI\\test1.txt"
		os.system(data)

	def systemInfo(self):
		data = "psexec \\\\" + self.name + " systeminfo > LOGI\\test2.txt"
		os.system(data)

	def funkRoute(self):
		data = "psexec \\\\" + self.name + " route print > LOGI\\test3.txt"
		os.system(data)


	def funk(self):
		self.funkInfo()
		self.systemInfo()
		self.funkRoute()

		

print("Podaj komputer: ")
name = input()
print("Podaj nick: ")
nameUser = input()

remoteCommand = RemoteCommand(name, nameUser)
remoteCommand.funk()