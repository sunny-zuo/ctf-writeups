---
title: login
date: 2020-06-22
tags: web, sql, beginner
ctf: redpwnCTF 2020
---
## Problem
```
I made a cool login page. I bet you can't get in!

Site: login.2020.redpwnc.tf
```

## Solution
The website brings us to a simple login page that appears to send a request to the server to authenticate. The [source code](./files/login.js) of the challenge was provided, so we can look through that to see if any vulernabilities exist. We immediately notice that the server utilizes a SQL database:

```js
const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const path = require('path');
const db = require('better-sqlite3')('db.sqlite3');
```

This is likely a SQL injection challenge. Looking further through the code, we find how the server checks credentials:

```js
let result;
    try {
        result = db.prepare(`SELECT * FROM users 
            WHERE username = '${username}'
            AND password = '${password}';`).get();
    } catch (error) {
        res.json({ success: false, error: "There was a problem." });
        res.end();
        return;
    }
```

The code makes a SQL query, and does not sanitize user input. The normal query would be checking for something like this:

```SELECT * FROM users WHERE username = 'example' AND password = 'example';```

Since the code directly takes our user input, we can modify the query so that it returns true. By putting ```' OR 1=1--``` as our password, the query becomes this:

```SELECT * FROM users WHERE username = 'example' AND password = '' OR 1=1--';```

We close the password string and make an alternative check of 1=1, which is true. The use of ```--``` allows us to comment out the remainder of the query so that it remains valid.

Using the above password gives us the flag!


**Flag:** ```flag{0bl1g4t0ry_5ql1}```