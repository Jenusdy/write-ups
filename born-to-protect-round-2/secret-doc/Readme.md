# Secret Document

## Challenge

Pada challange ini diberikan sebuah (file zip)[https://github.com/Jenusdy/write-ups/blob/master/born-to-protect-round-2/secret-doc/secret_doc_7ebbb414ab345363f06fb94e636a50d1.zip] yang jika diextract terdapat sebuah document. Namun isinya sama sekali kosong.

## Solution

Awalnya saya cuma mencoba-coba dengan menggunakan command `strings` pada terminal sehingga didapatkan :

```{bash}
$ strings secret_doc.docx | grep B2P
word/flag.xmlB2P{3a0e24ffb1f38ee2b55dd3941446f5b1}PK

```

Viola didapatkan flagnya B2P{3a0e24ffb1f38ee2b55dd3941446f5b1}
