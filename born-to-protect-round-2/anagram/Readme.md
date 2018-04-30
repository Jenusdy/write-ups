# Anagram

## Challenge

Pada service tersebut diberikan beberapa list nama-nama kota. Lalu kita diberikan sebuah string acak yang jika disusun merupakan salah satu nama kota pada list terebut (Permainan anagram). Diberikan hanya beberapa detik saja untuk menjawab dari 60 pertanyaan. 

> nc 35.197.134.203 8022 

## Solution

Saya mencoba menjawab beberapa pertanyaan pada service tersebut untuk mengetahui tipe nya. Sehingga saya membuatkan program seperti berikut

```{python}
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
				print "Benar"

	except:
		print r.recvall()
		exit(0)
```

Violaaa ... didapatkan flagnya.. Maaf saya lupa mencapture flag bagian ini. Dan servicenya juga sudah mati.