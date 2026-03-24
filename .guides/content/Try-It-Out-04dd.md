## Try It Out

> 📹 **[VIDEO NOT YET RECORDED — walkthrough of game code and how it works. Script at `.guides/secure/video-script-tryitout.md`]**

In the terminal, type `python3 interface.py` and press Enter.

Play through the game. As the Riot video on the Get Ready page suggests — find the pain points.

**Look at:**
- **Start screen**: Does it tell you what to do? What the game is about?
- **Score display**: Can you read it? Is it in the right place? Think about proximity and contrast.
- **Game over**: Is it clear the game ended? Do you know what to do next?

List at least **3 things** that could be improved.

{Check It!|assessment}(free-text-auto-2573246848)

---

<details><summary>Optional: Make flapping feel more like real Flappy Bird</summary>

Right now, holding SPACE makes the bird fly up continuously. In the real Flappy Bird, each tap gives one flap — you have to keep tapping.

To get that feel, move the flap logic out of `update()` and into `on_key_down()`:

**Remove this from `update()`:**
```python
    if keyboard.space:
        bird.vy = FLAP
```

**Add this to `on_key_down()`:**
```python
    elif state == "playing" and key == keys.SPACE:
        bird.vy = FLAP
```

The video explains why this works differently — `update()` checks every frame, but `on_key_down()` fires once per key press.

</details>
