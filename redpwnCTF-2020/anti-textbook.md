---
title: anti-textbook
date: 2020-06-24
tags: web, crypto
ctf: redpwnCTF 2020
---
## Problem
```
It's important for public keys to be transparent.

Hint: certificate-transparency.org
```

## Solution
This was a very interesting web challenge, since no website was given. We did get a data.txt file, containing an ```n``` and ```e``` value, indicating that it is for an RSA public key:

```
e: 65537
n: 23476345782117384360316464293694572348021858182972446102249052345232474617239084674995381439171455360619476964156250057548035539297034987528920054538760455425802275559282848838042795385223623239088627583122814519864252794995648742053597744613214146425693685364507684602090559028534555976544379804753832469034312177224373112610128420211922617372377101405991494199975508780694545263130816110474679504768973743009441005450839746644168233367636158687594826435608022717302508912914016439961300625816187681031915377565087756094989820015507950937541001438985964760705493680314579323085217869884649720526665543105616470022561
```

Reading about certificate transparency, we learn that it is essentially logs of all issued SSL certificates. We'll likely need to find a site who's SSL certificate matches the RSA public key (indirectly) given.

To search through certificate transparency logs, we found a site called [crt.sh](https://crt.sh/) that allows us to search using a variety of options, including SubjectPublicKeyInfo which we can get from just the public key.

First, we should construct the public key from the given n and n values. We can write a quick python script to do this, using PyCryptodome:

```py
from Crypto.PublicKey import RSA
n = 23476345782117384360316464293694572348021858182972446102249052345232474617239084674995381439171455360619476964156250057548035539297034987528920054538760455425802275559282848838042795385223623239088627583122814519864252794995648742053597744613214146425693685364507684602090559028534555976544379804753832469034312177224373112610128420211922617372377101405991494199975508780694545263130816110474679504768973743009441005450839746644168233367636158687594826435608022717302508912914016439961300625816187681031915377565087756094989820015507950937541001438985964760705493680314579323085217869884649720526665543105616470022561
e = 65537

key = RSA.construct((n, e))
pem = key.exportKey("PEM")

f = open("publickey.pem", "wb")
f.write(pem)
f.close()
```

We get this output:

```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuffuWhYrpTW8cdcAWUwe
T8oZYCp/8pKPYj4eZ3pd7mhYoCkSSeqZ5e+L33O38SoMANogM1NBayYlumOcPxC/
C9PHMF6AlaLDH+yX/Fg+a055m0O7+5pJNUVuRn9z7aYhhubnRyjk2cVTHLmOHqK9
FPM1QBBdouddMgZYE6plaBdBIMwQ8txuZQs6t862zJfA0/cgT47TtiTNkouHkAuT
VXBPcbM5pXIu7MoflJrUjQ0ljuOIFgXQ7wCFusXrIpvuVpqLzRvTD69GA7Cj0Dt9
ij7KPrBFM2jFyR8vnm5w+T6sGafXgJEEj0sLmbIReWcNeyHC2Tl9OniyMEqPeLsZ
oQIDAQAB
-----END PUBLIC KEY-----
```

However, this is only a public key, so we need to convert it to a certificate. We can use ```openssl``` for this:

```
openssl pkey -pubin -outform der -in publickey.pem -out publickey.der
```

Lastly, we get the sha256 checksum of the file of the newly created ```publickey.der``` file, which we need to search on [crt.sh](https://crt.sh/):

```
sha256sum publickey.der
```

This outputs ```9db105389dd81cfb4b59ff1a4c0670c630b1800e542323111d5c5cb9af72031f```. Searching for the checksum on [crt.sh](https://crt.sh/) (and specifiying that we're searching for the SHA-256 SubjectPublicKeyInfo), we find a [precertificate](https://crt.sh/?id=1998063179) and a [leaf certificate](https://crt.sh/?id=2001057066) for the website oa4gio7glypwggb9iu3rh8mrc87tnjbs.flag.ga.

Visting this site, we find the flag!

**Flag:** ```flag{c3rTific4t3_7r4n5pArAncY_fTw} ```