# Secret Document

## Challenge

Pada challange ini diberikan sebuah (file zip)[www.google.com] yang jika diextract terdapat sebuah document. Namun isinya sama sekali kosong.

## Solution

Awalnya saya cuma mencoba-coba dengan menggunakan command `strings` pada terminal sehingga didapatkan :

```{bash}
$ strings secret_doc.docx | grep B2P
word/flag.xmlB2P{3a0e24ffb1f38ee2b55dd3941446f5b1}PK

```

Viola didapatkan flagnya B2P{3a0e24ffb1f38ee2b55dd3941446f5b1}
