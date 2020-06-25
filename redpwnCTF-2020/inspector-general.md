---
title: Inspector General
date: 2020-06-22
tags: web, beginner
ctf: redpwnCTF 2020
---
## Problem
```
My friend made a new webpage, can you [find a flag?](https://redpwn.net/)
```

## Solution
This challenge was a simple inspect element challenge. Looking at the page source, we find this in the head:

```html
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="redpwnctf2020" content="flag{1nspector_g3n3ral_at_w0rk}">
    <title>Home | redpwn</title>
```

**Flag:** ```flag{1nspector_g3n3ral_at_w0rk}```