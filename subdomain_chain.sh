#!/usr/bin/bash

target=$1

#Finding subdomains using sublist3r, subfinder and assetfinder

if ! [ $target ]; then
        echo "[!] No target provided like example.com "
        exit 1
fi

sublist3r -d $target -t 5 -o domain
subfinder -d $target -o domain1
assetfinder --subs-only $target >>domain
#cat domain domain1  |sort |uniq >domains
sort -u domain domain1 >domains
rm domain domain1
echo "[!]Found subdomains were saved in domains."
exit 0
