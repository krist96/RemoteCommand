import os
from colorama import init, Fore, Back, Style 

init(convert=True)

class RemoteCommand:
	def __init__(self):
		self.name = ""
		self.nameUser = ""

	def funkInfo(self):
		data = "net user " + self.nameUser + " /DOMAIN > LOGI\\InformacjeOUzytkowniku.txt"
		os.system(data)

	def systemInfo(self):
		data = "psexec \\\\" + self.name + " systeminfo > LOGI\\SystemInfo.txt"
		print(data)
		os.system(data)
		#text = open('LOGI\\test2.txt', 'rb').read()

	def funkRoute(self):
		data = "psexec \\\\" + self.name + " route print > LOGI\\TablicaRutingow.txt"
		print(str(data))
		os.system(data)

	def ipConfig(self):
		data = "psexec \\\\" + self.name + " ipconfig /flushdns > LOGI\\test4.txt"
		os.system(data)	

	def refresh(self):
		data = "psexec \\\\" + self.name + " GPUPDATE /force > LOGI\\POTWIERDZENIE\\potwierdzenieUpdateForce.txt"
		os.system(data)
		data2 = "psexec \\\\" + self.name + " ipconfig /flushdns > LOGI\\POTWIERDZENIE\\potwierdzenieFlushDNS.txt"
		os.system(data2)	
		data3 = "psexec \\\\" + self.name + " ipconfig /registerdns > LOGI\\POTWIERDZENIE\\potwierdzenieRegisterDNS.txt"
		os.system(data3)
		data4 = "psexec \\\\" + self.name + " ipconfig /release > LOGI\\POTWIERDZENIE\\potwierdzenieIpconfigRelease.txt"
		os.system(data4)	
		data5 = "psexec \\\\" + self.name + " ipconfig /renew > LOGI\\POTWIERDZENIE\\potwierdzenieIpconfigReNew.txt"
		os.system(data5)
	
	def ping(self):
		data = "ping " + self.nameUser + " > LOGI\\InformacjeOUzytkowniku.txt"
		os.system(data)
		look = "ping " + self.nameUser 
		os.system(look)


	def restartPassword(self):
		self.printGreen("Podaj Nowe Hasło: ")
		password = input()
		data = "net user " + self.nameUser + password +" /DOMAIN > LOGI\\POTWIERDZENIE\\potwierdzenieZmianyHasla.txt"
		os.system(data)

###  Style tekstow  ###
	def printGreen(self, text):
		print(Fore.GREEN + text)
		print(Style.RESET_ALL)

	def printYellow(self, text):
		print(Fore.YELLOW + text)
		print(Style.RESET_ALL)

	def printRed(self, text):
		print(Fore.RED + text)
		print(Style.RESET_ALL)

	def printBackGreen(self, text):
		print(Back.GREEN + text)
		print(Style.RESET_ALL)

	def printBackRed(self, text):
		print(Back.RED + text)
		print(Style.RESET_ALL)

	def printBackYellow(self, text):
		print(Back.YELLOW + text)
		print(Style.RESET_ALL)

	def printBackCyan(self, text, text2, text3):
		print(Fore.RED + Back.CYAN + text + text2 + text3)
		print(Style.RESET_ALL)

	def printBlue(self, text,):
		print(Fore.BLUE + text)
		print(Style.RESET_ALL)

	def menu(self):
		self.printRed("-" * 50)
		self.printBackGreen("""
1. Informacje o uzytkowniku \n
2. System Info - Informacje o komputerze \n
3. Tablica Rutingow \n
4. Oczyszczenie DNS, DHCP i aktualizacja rejestru \n
5. Zmiana hasla uzytkownikowi
6. Pingowanie""")
		self.printBackRed("8. Zmien nazwe komputera i uzytkownik") 
		self.printBackRed("9. Wyjdź")
		self.printRed("-" * 50)

		self.printBackYellow("Aktualnie operujesz na komputerze / uzytkowniku: ")
		self.printBackCyan(self.name , " / " , self.nameUser)
		self.printRed("-" * 50)
		self.printYellow("Podaj numer:")
		option = int(input())
		if(option == 1):
			self.funkInfo()
			self.printGreen("Polecenie 1. Informacje o uzytkowniku - zostalo wykonane pomyslnie")
		elif(option == 2):
			self.systemInfo()
			self.printGreen("Polecenie 2. System Info - Informacje o komputerze - zostalo wykonane pomyslnie")
		elif(option == 3):
			self.funkRoute()
			self.printGreen("Polecenie 3. Tablica Rutingow - zostalo wykonane pomyslnie")
		elif(option == 4):
			self.refresh()
			self.printGreen("Polecenie 4. Oczyszczenie DNS, DHCP i aktualizacja rejestru - zostalo wykonane pomyslnie")
		elif(option == 5):
			self.restartPassword()
			self.printGreen("Polecenie 5. Zmiana hasla uzytkownikowi - zostalo wykonane pomyslnie")
		elif(option == 6):
			self.ping()
			self.printGreen("Polecenie 6. Pingowanie - zostalo wykonane pomyslnie")
		elif(option == 8):
			self.inputs()
			self.printGreen("Polecenie 8. Zmiana nazwy uzytkownika/komputera - zostalo wykonane pomyslnie")
			self.printRed("Nowa nazwa komputera: ")
			print(self.name)
			self.printRed("Nowa nazwa użytkownika: ")
			print(self.nameUser)
		elif(option == 9):
			return
		else:
			self.printRed("Podaj inna wartosc \n")
		self.menu()

	def inputs(self):
		self.printGreen("Podaj komputer: ")
		self.name = input()
		self.printGreen("Podaj nick: ")
		self.nameUser = input()

	def funk(self):
		self.inputs()
		self.menu()


		





remoteCommand = RemoteCommand()
remoteCommand.funk()
