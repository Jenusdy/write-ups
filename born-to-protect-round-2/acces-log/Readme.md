# Access log

## Challenge

Diberikan sebuah (file zip)[www.google.com] yang jika di extact akan memberikan sebuah file access.log.

## Solution

Saya mencoba mencari dengan Ctrl+F kata yang berawalan `flag` atau `B2P` namun tidak ditemukan apa-apa. Sehingga saya mencoba menelaah lagi tiap baris hingga menemukan baris yang saya curigai adalah flagnya

```
192.168.32.1 - - [23/Apr/2018:03:37:34 -0400] "GET %2Fmutillidae%2Findex.php%3Fpage%3Duser-info.php%26username%3D%27+union+all+select+1%2CString.fromCharCode%28102%2C+108%2C+97%2C+103%2C+32%2C+105%2C+115%2C+32%2C+66%2C+50%2C+80%2C+123%2C+53%2C+48%2C+102%2C+49%2C+101%2C+97%2C+55%2C+99%2C+102%2C+49%2C+53%2C+52%2C+52%2C+49%2C+48%2C+54%2C+101%2C+51%2C+53%2C+53%2C+53%2C+99%2C+52%2C+99%2C+99%2C+50%2C+99%2C+102%2C+52%2C+48%2C+56%2C+55%2C+125%29%2C3+--%2B%26password%3D%26user-info-php-submit-button%3DView+Account+Details HTTP/1.1" 200 9582 "http://192.168.32.134/mutillidae/index.php?page=user-info.php&username=something&password=&user-info-php-submit-button=View+Account+Details" "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
```

Pada bagian ini saya coba ubah 

```
String.fromCharCode%28102%2C+108%2C+97%2C+103%2C+32%2C+105%2C+115%2C+32%2C+66%2C+50%2C+80%2C+123%2C+53%2C+48%2C+102%2C+49%2C+101%2C+97%2C+55%2C+99%2C+102%2C+49%2C+53%2C+52%2C+52%2C+49%2C+48%2C+54%2C+101%2C+51%2C+53%2C+53%2C+53%2C+99%2C+52%2C+99%2C+99%2C+50%2C+99%2C+102%2C+52%2C+48%2C+56%2C+55%2C+125%29

Didecode ke utf-8

String.fromCharCode(102,+108,+97,+103,+32,+105,+115,+32,+66,+50,+80,+123,+53,+48,+102,+49,+101,+97,+55,+99,+102,+49,+53,+52,+52,+49,+48,+54,+101,+51,+53,+53,+53,+99,+52,+99,+99,+50,+99,+102,+52,+48,+56,+55,+125)

Hapus semua tanda + nya 

String.fromCharCode(102,108,97,103,32,105,115,32,66,50,80,123,53,48,102,49,101,97,55,99,102,49,53,52,52,49,48,54,101,51,53,53,53,99,52,99,99,50,99,102,52,48,56,55,125)


Pada console web browser kita coba paste kan lalu Viola... 

"flag is B2P{50f1ea7cf1544106e3555c4cc2cf4087}"
```

