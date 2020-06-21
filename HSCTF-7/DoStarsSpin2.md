---
title: Do Stars Spin? 2
date: 2020-06-06
tags: osint, misc
ctf: HSCTF 7
slug: /ctf-writeups/do-stars-spin-2
---
## Problem
```
PMP was walking by earlier, muttering something about "stars". I think he's said something about it before. I also want to know: do stars spin? I'd search for it, but I'm too busy. I think he's mentioned something about stars somewhere…help me out? [continued]

Author: JC01010
```

## Solution
With no additional info from the challenge description, we can continue where we left off with [Do Stars Spin? 1](./DoStarsSpin1.md). Another [deleted post](https://web.archive.org/web/20200527041338/https://www.reddit.com/user/dostarsevenspin/) contained information about his Instagram:

```
Hey, I need help on my instagram profile

How do I delete posts? Here is my handle: @ dostarsevenspin
```

Checking the [Instagram profile](https://www.instagram.com/dostarsevenspin/), we find a biography:
```
Twitter: starsdonotspin
Reddit: dostarsevenspin
Sc: starsspinn't
Follow me for free flag (dm too)
^imagine falling for that
flag{no}
```

There are also a few memes posted. I checked the Instagram account to see if I could find any other info (for example, through the [GraphQL API](https://www.instagram.com/dostarsevenspin/?__a=1)) and checked Wayback Machine just in case the "deleted" posts were also archived, with no success.

The biography links to the user's Twitter and Snapchat. The snapchat didn't seem to exist, so the [Twitter profile](https://twitter.com/starsdonotspin) was our only lead. Two of his tweets stood out: ([tweet 1](https://twitter.com/starsdonotspin/status/1268209028414484481), [tweet 2](https://twitter.com/starsdonotspin/status/1266119748737290242))

```
smh, imagine getting banned on one of the tfes forums, at least im not banned on the 2nd one
```

```
en.wikipedia.org/wiki/Spin_Star
https://en.wikipedia.org/wiki/Star

EVEN WIKIPEDIA SAID SO!
```

The first tweet led to the flag for [Do Stars Spin? 3](./DoStarsSpin3.md). The second tweet linked to two Wikipedia articles. Checking the revision history of both articles, I noticed that Wikipedia user Dostarsspin made an edit on the [Spin Star article](https://en.wikipedia.org/w/index.php?title=Spin_Star&action=history). The user Dostarsspin had a [few other 'contributions'](https://en.wikipedia.org/wiki/Special:Contributions/Dostarsspin), including an edit on the Wikipedia page for flags. The [revision on the Flag page](https://en.wikipedia.org/w/index.php?title=Flag&diff=prev&oldid=959455544) contains our flag.

**Flag:** ```flag{te3_6ov3rnM3n7_i5_h1d1ng_1nf0!}```