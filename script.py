import os
import random
from colorama import init, Fore, Back, Style 

init(convert=True)

class RemoteCommand:
	def __init__(self):
		self.nameOfComputer = ""
		self.nameUser = ""

	def validate(self):
		if(len(self.nameOfComputer) <= 3 and len(self.nameUser) <= 3):
			print("Podaj nazwę użytkownika i nazwę komputera dłuższą niż 3 znaki")
			self.inputs()

	def commandInDomain(self, phrase1, phrase2, phrase3):
		data = phrase1 + self.nameOfComputer + phrase2 + phrase3
		os.system(data)
		look = phrase1 + self.nameOfComputer + phrase2
		os.system(look)

	def commandRemoteDesktop(self, phrase1, phrase2):
		data = "psexec \\\\" + self.nameOfComputer + phrase1 + phrase2
		os.system(data)
		look = "psexec \\\\"  + self.nameOfComputer + phrase1
		os.system(look)

	def ipConfig(self):
		data = "psexec \\\\" + self.name + " ipconfig /flushdns > LOGI\\test4.txt"
		os.system(data)	


	def restartPassword(self):
		self.printGreen("Podaj Nowe Hasło: ")
		password = input()
		data = "net user " + self.nameUser + password +" /DOMAIN > LOGI\\POTWIERDZENIE\\potwierdzenieZmianyHasla.txt"
		os.system(data)

	def password(self, i, tab):
		chars = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "H", "h", "I", "i", "J", "j", "K", "k",
		 "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", 
		 "W", "w", "X", "x", "Y", "y", "Z", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "(", ")", "[", "]", 
		 "{", "}", "-", "_", "<", ">"]
		if(i < 30):
			tab.append(random.choice(chars))
			return self.password(i+1, tab)
		print("".join(tab));

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

	def menu2(self):
		self.printRed("-" * 50)
		self.printBackGreen("""
1. Mapuj Dysk T: \n
2. Mapuj Dysk ... \n
3. Mapuj Dysk Osobisty... \n""")
		self.printBackRed("4. Zmień użytkownika/ Komputer") 
		self.printBackRed("5. Wróć do Menu głównego") 
		self.printRed("-" * 50)

		self.printBackYellow("Aktualnie operujesz na komputerze / uzytkowniku: ")
		self.printBackCyan(self.nameOfComputer , " / " , self.nameUser)
		self.printRed("-" * 50)
		self.printYellow("Podaj numer:")
		option = int(input())
		if(option == 1):
			self.commandRemoteDesktop(" net use t: /delete", "")
			self.commandRemoteDesktop(" net use t: \\\\DOMENA\\DyskT /persistent:NO", " > LOGI\\mapujDyskT.txt")
			self.printGreen("Polecenie 1. Mapuj Dysk Sieciowy T: - zostalo wykonane pomyslnie")
		elif(option == 2):
			self.commandRemoteDesktop(" systeminfo", "  > LOGI\\SystemInfo.txt")
			self.printGreen("Polecenie 2.  Mapuj Dysk Sieciowy ...:: - zostalo wykonane pomyslnie")
		elif(option == 3):
			self.commandRemoteDesktop(" route print", " > LOGI\\TablicaRutingow.txt")
			self.printGreen("Polecenie 3.  Mapuj Dysk Sieciowy ...: - zostalo wykonane pomyslnie")

		elif(option == 4):
			self.inputs()
			self.printGreen("Polecenie 4. Zmiana nazwy uzytkownika/komputera - zostalo wykonane pomyslnie")
			self.printRed("Nowa nazwa komputera: ")
			print(self.nameOfComputer)
			self.printRed("Nowa nazwa użytkownika: ")
			print(self.nameUser)
		elif(option == 5):
			self.menu()
		else:
			self.printRed("Podaj inna wartosc \n")
		self.menu2()

	def menu(self):
		self.printRed("-" * 50)
		self.printBackGreen("""
1. Informacje o uzytkowniku \n
2. System Info - Informacje o komputerze \n
3. Tablica Rutingow \n
4. Oczyszczenie DNS, DHCP i aktualizacja rejestru \n
5. Zmiana hasla uzytkownikowi \n
6. Pingowanie \n
7. Generator Hasła\n
8. Mapowanie Dysków sieciowych""")
		self.printBackRed("14. Zmien nazwe komputera i uzytkownik") 
		self.printBackRed("15. Wyjdź")
		self.printRed("-" * 50)

		self.printBackYellow("Aktualnie operujesz na komputerze / uzytkowniku: ")
		self.printBackCyan(self.nameOfComputer , " / " , self.nameUser)
		self.printRed("-" * 50)
		self.printYellow("Podaj numer:")
		option = int(input())
		if(option == 1):
			self.commandInDomain("net user ", " /DOMAIN", " > LOGI\\netUserCommand.txt")
			self.printGreen("Polecenie 1. Informacje o uzytkowniku - zostalo wykonane pomyslnie")
		elif(option == 2):
			self.commandRemoteDesktop(" systeminfo", "  > LOGI\\SystemInfo.txt")
			self.printGreen("Polecenie 2. System Info - Informacje o komputerze - zostalo wykonane pomyslnie")
		elif(option == 3):
			self.commandRemoteDesktop(" route print", " > LOGI\\TablicaRutingow.txt")
			self.printGreen("Polecenie 3. Tablica Rutingow - zostalo wykonane pomyslnie")
		elif(option == 4):
			self.commandRemoteDesktop(" systeminfo", "  > LOGI\\SystemInfo.txt")
			self.printGreen("Polecenie 4. Oczyszczenie DNS, DHCP i aktualizacja rejestru - zostalo wykonane pomyslnie")
		elif(option == 5):
			self.restartPassword()
			self.printGreen("Polecenie 5. Zmiana hasla uzytkownikowi - zostalo wykonane pomyslnie")
		elif(option == 6):
			self.commandInDomain("ping ", " ", " > LOGI\\pingCommand.txt")
			self.printGreen("Polecenie 6. Pingowanie - zostalo wykonane pomyslnie")
		elif(option == 7):
			self.password(0, [])
			self.printGreen("Polecenie 7. Generator hasła - zostalo wykonane pomyslnie")
		elif(option == 8):
			self.menu2()
		elif(option == 14):
			self.inputs()
			self.printGreen("Polecenie 14. Zmiana nazwy uzytkownika/komputera - zostalo wykonane pomyslnie")
			self.printRed("Nowa nazwa komputera: ")
			print(self.nameOfComputer)
			self.printRed("Nowa nazwa użytkownika: ")
			print(self.nameUser)
		elif(option == 15):
			return
		else:
			self.printRed("Podaj inna wartosc \n")
		self.menu()

	def inputs(self):
		self.printGreen("Podaj komputer: ")
		self.nameOfComputer = input()
		self.printGreen("Podaj nick: ")
		self.nameUser = input()
		self.validate()

	def funk(self):
		self.inputs()
		self.menu()


		





remoteCommand = RemoteCommand()
remoteCommand.funk()
