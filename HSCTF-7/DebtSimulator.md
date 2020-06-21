---
title: Debt Simulator
date: 2020-06-06
tags: web
ctf: HSCTF 7
---
## Problem
```
https://debt-simulator.web.hsctf.com/

Author: Madeleine

```

## Solution
The link leads us to a page containing a game. Upon every button press, the user's balance either increases or decreases by a random amount. The game seems to be rigged so that the player eventually loses, barring extreme luck. Viewing the source code, we find some more information about the game:

```
  useEffect(() => {
    if (runningTotal < -1000) {
      setMessage("You lost. You have less than $-1000. Better luck next time.");
      setButtonText("Play Again");
    } else if (runningTotal > 2000) {
      setMessage("You won. You have more than $2000. Try your luck again?");
      setButtonText("Play Again");
    } else if (runningTotal !== 0 && buttonText !== "Next Round") {
      setButtonText("Next Round");
    }
  });
```

The information tells us what happens when we win or lose the game, and it doesn't seem like either of them lead to a flag. What's more interesting is the code that determines what happens when the button is pressed:
```
const onClick = () => {
    const isGetCost = Math.random() > 0.4 ? true : false;
    const func = isGetCost ? 'getCost' : 'getPay';
    const requestOptions = {
      method: 'POST',
      body: 'function=' + func,
      headers: { 'Content-type': 'application/x-www-form-urlencoded' }
    }

    fetch("https://debt-simulator-login-backend.web.hsctf.com/yolo_0000000000001", requestOptions)
    .then(res => res.json())
    .then(data => {
      data = data.response;
      if (buttonText === "Play Again" || buttonText === "Start Game") {
        setButtonText("Next Round");
        setRunningTotal(0);
      }
      setMessage("You have " + (isGetCost ? "paid me " : "received ") + "$" + data + ".");
      setRunningTotal(runningTotal => isGetCost ? runningTotal - data : runningTotal + data);
    });
  }
  ```

A POST request is made to the ```https://debt-simulator-login-backend.web.hsctf.com/yolo_0000000000001``` endpoint upon every button click, calling the ```getPay``` or ```getCost``` function on the server. These functions seemed to return a "random" number, with ```getCost``` generally giving higher values than ```getPay```. There was no flag or any additional information returned in the response for these functions. Knowing the endpoint, I tried to call the ```getFlag``` and ```flag``` function (I like to use Insomnia for API experimentation), and was greeted with this response:

```
{
  "response": "nice try but no"
}
```

We were close, but not quite there. I sent a GET request to the endpoint to see if I could get any more information about the server, and received this response:
```
{
  "functions": [
    "getPay",
    "getCost",
    "getgetgetgetgetgetgetgetgetFlag"
  ]
}
```

Sending a request with the ```getgetgetgetgetgetgetgetgetFlag``` function gave us the flag:
```
{
  "response": "flag{y0u_f0uND_m3333333_123123123555554322221}"
}
```

**Flag:** ```flag{y0u_f0uND_m3333333_123123123555554322221}```