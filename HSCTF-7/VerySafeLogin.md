---
title: Very Safe Login
date: 2020-06-07
tags: web, beginner
ctf: HSCTF 7
slug: /ctf-writeups/very-safe-login
---
## Problem
```
Bet you can't log in.

https://very-safe-login.web.hsctf.com/very-safe-login

Author: Madeleine
```

## Solution
The link leads us to a login page. Viewing the page source, we find the following script:
```
<script>
    var login = document.login;

    function submit() {
        const username = login.username.value;
        const password = login.password.value;
            
        if(username === "jiminy_cricket" && password === "mushu500") {
            showFlag();
            return false;
        }
        return false;
    }
</script>
```

The login page validates the credentials on the client, allowing us to find the credentials in the source code. Logging in with the credentials brings us to a page with the flag.

**Flag:** ```flag{cl13nt_51de_5uck5_135313531}```