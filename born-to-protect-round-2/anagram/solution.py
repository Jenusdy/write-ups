from pwn import *

def is_anagram(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()

    return (list_str1 == list_str2)


r = remote("35.197.134.203",8022)
r.recvline()
r.recvline()
r.recvline()


while True:
	try:
		r.recvline()
		kata = r.recvuntil("']")
		kata = eval(kata.replace('Wordlist: ',''))

		r.recvline()

		dicari = r.recvline()
		dicari = dicari.strip('\n')
		dicari = dicari.replace('Nama kota yang di acak: ','')

		print dicari
		print kata
		for i in kata:	
			if is_anagram(i,dicari):
				r.send(i)
				print "Lewat"

	except:
		print r.recvall()
		exit(0)