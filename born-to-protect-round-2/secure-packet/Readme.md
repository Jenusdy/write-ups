# Secure Packet

## Challenge

Pada challange ini diberikan sebuah (file zip)[https://github.com/Jenusdy/write-ups/blob/master/born-to-protect-round-2/secure-packet/crt_001e3e8602b6f05598caab71cc792ba1.zip] yang jika diextract file .pcap yang dapat dibuka dengan menggunakan Wireshark.

## Solution

Awalnya saya cuma mencoba-coba dengan menggunakan command `strings` pada terminal sehingga didapatkan :

```{bash}

$ strings secure_packet_576bit.pcap | grep B2P
B2P{d2b03589a0977959e4198c77efad6dcd}

```

Viola didapatkan flagnya B2P{d2b03589a0977959e4198c77efad6dcd}
