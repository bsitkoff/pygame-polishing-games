## Try It Out


<iframe width="720" height="600"
  src="https://app.screencastify.com/watch/RHi8u1Gvx8kW3Sv5CSqT/embed"
  title="Codio - Extension: Polishing Games-1 - Screencastify - March 24, 2026 9:11 PM"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen
></iframe>
  

In the terminal, type `python3 interface.py` and press Enter.

Play through the game. As the Riot video on the Get Ready page suggests — find the pain points.

**Look at:**
- **Start screen**: Does it tell you what to do? What the game is about?
- **Score display**: Can you read it? Is it in the right place? Think about proximity and contrast.
- **Game over**: Is it clear the game ended? Do you know what to do next?

{Check It!|assessment}(free-text-auto-2573246848)

---

<details><summary>Optional: Make flapping feel more like real Flappy Bird</summary>

Right now, holding SPACE makes the bird fly up continuously. In the real Flappy Bird, each tap gives one flap — you have to keep tapping.

To get that feel, **remove** the flap check from `update()`:
```python
    if keyboard.space:
        bird.vy = FLAP
```

And **add a new function** called `on_key_down()` that handles it instead:
```python
def on_key_down(key):
    if state == "playing" and key == keys.SPACE:
        bird.vy = FLAP
```

Why does this work differently? `keyboard.space` in `update()` checks every frame — so if you're holding the key, it fires over and over. `on_key_down()` is a special PyGame Zero function that only fires once, the moment you press the key. One tap, one flap.

</details>
