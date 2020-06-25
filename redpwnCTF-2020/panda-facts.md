---
title: panda-facts
date: 2020-06-23
tags: web, json
ctf: redpwnCTF 2020
---
## Problem
```
I just found a hate group targeting my favorite animal. Can you try and find their secrets? We gotta take them down!

Site: panda-facts.2020.redpwnc.tf
```

## Solution

The site brings us to a webpage where we 'login' with a username, and then are presented with panda facts. There's a button present to show a member only fact (presumably the flag), which tells us that we are not a member upon pressing. The site leaves a cookie, but the cookie appears to be encrypted. The [source code of the challenge](./files/pandafacts1.js) was provided, so we can start by taking a look there.

We can find how the cookie is generated:
```js
async function generateToken(username) {
    const algorithm = 'aes-192-cbc'; 
    const key = Buffer.from(process.env.KEY, 'hex'); 
    // Predictable IV doesn't matter here
    const iv = Buffer.alloc(16, 0);

    const cipher = crypto.createCipheriv(algorithm, key, iv);
    const token = `{"integrity":"${INTEGRITY}","member":0,"username":"${username}"}`

    let encrypted = '';
    encrypted += cipher.update(token, 'utf8', 'base64');
    encrypted += cipher.final('base64');
    return encrypted;
}
```

The code builds a JSON token using template literals for user input as a string. We also note that ```member``` is set to 0, so we need to change it to 1 in order to become a member and get the flag. Since the JSON is built as a string, we can use JSON injection to become a member by setting this as our username:

```
user", "member":"1
```

As a result, the server would create the following JSON:

```json
{
    "integrity": "12370cc0f387730fb3f273e4d46a94e5",
    "member": 0,
    "username": "user",
    "member": "1"
}
```

When a JSON object contains duplicate keys (```member``` appears twice), it will take the last key of that name. Thus, when the server checks, they will see that the key ```member``` is equal to ```1```. With this, we can see the exclusive member fact, which is the flag.

**Flag:** ```flag{1_c4nt_f1nd_4_g00d_p4nd4_pun}```