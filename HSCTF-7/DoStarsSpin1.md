---
title: Do Stars Spin? 1
date: 2020-06-06
tags: osint, misc
ctf: HSCTF 7
---
## Problem
```
PMP was walking by earlier, muttering something about "stars". I think he's said something about it before. I also want to know: do stars spin? I'd search for it, but I'm too busy. I think he's mentioned something about stars somewhere…help me out?

Author: JC01010
```

## Solution
The problem mentions the name PMP, searching and stars. Having joined the Discord for the Discord Flag, PMP was the username of one of the organizers. We can search for when PMP mentioned something about stars using the query ```from: PMP#5728 stars``` in Discord's built in search function. This leads to a single message block:
```
does anyone actually use this server

Hello, HSCTF 7!
I'm sure we've all asked the age-old question: Do stars even spin? (No, we haven't. JC put me up to this.)
Hm, I wonder… dostarsevenspin? Time to ask reddit
```

With this, we get the keywords of ```dostarsevenspin``` and ```reddit```. Checking the [profile of dostarsevenspin](https://old.reddit.com/user/dostarsevenspin) on Reddit, we find a post:

```
Somebody hacked my account and deleted all my posts... help!
```

To find the flag, we need to recover his post history. Checking ```ceddit``` and ```removeddit``` yielded no results, as both rely on the PushShift API and the posts were likely deleted prior to PushShift recording them. There are a few other archive websites to check, such as Wayback Machine (archive.org). Wayback Machine had a [snapshot](https://web.archive.org/web/20200527041338/https://www.reddit.com/user/dostarsevenspin/) of /u/dostarsevenspin's posts, which contained the bee movie script, and the flag.

**Flag:** ```flag{7t3rE_i5_n0_wAy_a_be3_sh0u1d_BEE_ab13_t0_f1Y_89a89fe1}```