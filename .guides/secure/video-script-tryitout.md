# Try It Out — Video Script

**Goal**: Walk students through the game code so they understand what they're about to modify. Do NOT point out the UI problems — they need to find those themselves. At the end, show the optional on_key_down upgrade.

**Have on screen**: `interface.py` open in the editor, terminal visible.

---

## Opening (~15 sec)

"This is a flappy bird-style game. The code is already written — it runs, it works. Your job isn't to write new code. It's to make the game *feel* good. Let me walk you through how it's set up."

## Setup variables (lines 7–22, ~45 sec)

Highlight lines 7–11.

"At the top we've got our window size, and two global variables you've seen before — `state` and `score`. Same pattern as the last lesson."

Highlight lines 13–16.

"These constants control the game physics. `GRAVITY` pulls the bird down, `FLAP` is how hard it jumps, `GAP` is the space between pipes, and `SPEED` is how fast the pipes move. You don't need to change these — but you can experiment with them later if you want."

Highlight lines 18–22.

"Three Actors — the bird and two pipes. The `anchor` on the pipes just controls which edge lines up with the gap. The bird also has `vy` — that's its vertical velocity. Gravity increases it, flapping resets it."

## reset functions (lines 25–36, ~20 sec)

"`reset_pipes` picks a random gap position and moves both pipes to the right edge. `reset_game` zeroes the score, puts the bird back in the middle, and resets the pipes. Same pattern as last time."

## update (lines 39–59, ~45 sec)

"The `update` function — runs every frame. First line should look familiar: if we're not playing, do nothing."

Highlight lines 44–45.

"Here's the flap. If you're holding SPACE, the bird's velocity gets set to `FLAP`, which is negative — so the bird goes up. This should feel familiar — it's checking a key inside `update()`, same as arrow keys in the chase game."

Highlight lines 47–48.

"Every frame, gravity adds to the velocity, and the bird moves by that amount. So the bird is always falling unless you press SPACE."

Highlight lines 50–53.

"Pipes slide left every frame. When they go off screen, they reset to a new random position and the score goes up."

Highlight lines 55–59.

"Two ways to lose: hit a pipe, or fly off the top or bottom. Same `colliderect` you've used before."

## draw (lines 62–75, ~10 sec)

"The `draw` function — three states, three screens. I'll let you form your own opinions about how these look."

**Don't linger. Don't read the text values. Move on.**

## on_key_down (lines 78–89, ~10 sec)

"`on_key_down` handles SPACE to start and R to restart. Same as before."

## Optional: on_key_down flap upgrade (~45 sec)

"One more thing. Right now, holding SPACE makes the bird fly up continuously. Real Flappy Bird doesn't work that way — each tap gives you one flap.

If you want that feel, there's an optional upgrade on the page. You move the flap check out of `update()` and into `on_key_down()`.

The difference is: `update()` runs every single frame — so if you're holding the key, it fires over and over. `on_key_down()` only fires once, the moment you press the key. One tap, one flap.

It's totally optional. The game works fine either way — it's just a different feel."

## Closing (~10 sec)

"That's the code. Run it, play it, and tell me what you think about the design."

---

**Total time**: ~3.5 minutes
