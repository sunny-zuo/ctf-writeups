---
title: Do Stars Spin? 3
date: 2020-06-06
tags: osint, misc
ctf: HSCTF 7
---
## Problem
```
[Do Stars Spin? 2 continued]

Author: JC01010
```

## Solution
With no additional info from the challenge description, we can continue where we left off with [Do Stars Spin? 2](./DoStarsSpin2.md). The twitter profile had this tweet:

```
smh, imagine getting banned on one of the tfes forums, at least im not banned on the 2nd one
```

The [Wikipedia account](https://en.wikipedia.org/wiki/Special:Contributions/Dostarsspin) also made revisions to the *[Conspiracy theory](https://en.wikipedia.org/w/index.php?title=Conspiracy_theory&diff=prev&oldid=960548597)* and *[Modern flat Earth societies](https://en.wikipedia.org/w/index.php?title=Modern_flat_Earth_societies&diff=prev&oldid=960548445)* articles, adding a few links to the article:

```	
*[https://www.youtube.com/watch?v=I2vKd6FbXd8 Behind the Curve Trailer]
*[https://www.dreamlandresort.com/ Area 51]
*[https://archive-it.org/collections/3610 UFO Sighting Forums]
*[https://thescienceforum.org/ Science Forums]
*[https://forum.tfes.org/index.php TFES]
*[https://theflatearthsociety.org/forum/ The Flat Earth Society]
*[https://www.scienceforums.net/ Science Forums]
*[http://www.scienceforums.com/ Science Forums]
```

We now have two TFES forums (tfes.org and theflatearthsociety.org) to look through. We can use Google to search for anything about "Do Stars Spin?" in the two forums with two queries:

* ```do stars spin? site:https://forum.tfes.org/index.php```
* ```do stars spin? site:https://theflatearthsociety.org/forum```

We can filter the search for information from the past month. The first search yielded no results, so it's likely the forum that the user was banned in. The second search didn't yield any exact links, but did link to the [Flat Earth General board](https://www.theflatearthsociety.org/forum/index.php?board=20.0). With a quick look through the threads on the first page of the board, there is a thread titled *[Do stars spin?](https://www.theflatearthsociety.org/forum/index.php?topic=86057.0)* by user [starsspinning](https://www.theflatearthsociety.org/forum/index.php?action=profile;u=1510927). The thread did not seem to contain any useful infomration. Looking through the user's [post history](https://www.theflatearthsociety.org/forum/index.php?action=profile;area=showposts;u=1510927), we find a [more interesting post](https://www.theflatearthsociety.org/forum/index.php?topic=86066.msg2254895#msg2254895):

```
How do sunspots appear on the sun?

Also, do stars spin?

Email me at starsspinning123@gmail.com! 
```

A quick search for the email didn't yield any results, so I figured I'd send an email. I received an autoreply:

```
Not available through email right now! Shoot me a message on hangouts though, I'll reply from there!

https://hangouts.google.com/group/nbZkwLjPyNZuZt6g6
(use a throwaway if you dont want to be doxxed)
```

Joining the hangouts group leads us to the flag, with the group being titled ```flag{fuuuhhhh1Illlla@gggg}```.

**Flag:** ```flag{fuuuhhhh1Illlla@gggg}```