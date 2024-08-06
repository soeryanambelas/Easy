import os
	
if __name__ == "__main__":
	try:os.system("git pull")
	except:pass
	try:os.system("mkdir /sdcard/ESBFLIVE")
	except:pass
	try:os.system("mkdir /sdcard/ESBFCHEK")
	except:pass
	__import__("ESBF").menu()
