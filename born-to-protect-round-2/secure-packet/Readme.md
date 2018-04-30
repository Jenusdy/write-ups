# Secure Packet

## Challenge

Pada challange ini diberikan sebuah (file zip)[www.google.com] yang jika diextract file .pcap yang dapat dibuka dengan menggunakan Wireshark.

## Solution

Awalnya saya cuma mencoba-coba dengan menggunakan command `strings` pada terminal sehingga didapatkan :

```{bash}

$ strings secure_packet_576bit.pcap | grep B2P
B2P{d2b03589a0977959e4198c77efad6dcd}

```

Viola didapatkan flagnya B2P{d2b03589a0977959e4198c77efad6dcd}
