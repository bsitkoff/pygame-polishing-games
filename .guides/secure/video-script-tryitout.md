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

"These constants control the game physics. `GRAVITY` pulls the bird down every frame. `FLAP` is how hard it jumps — it's negative because up is negative in PyGame Zero. `GAP` is the space between the top and bottom pipes. And `SPEED` is how fast the pipes move toward you.

These three values — `GRAVITY`, `FLAP`, and `GAP` — work together. If the game feels too hard, you can make `GRAVITY` smaller so you fall slower, make `FLAP` more negative so you jump higher, or make `GAP` bigger so there's more room between the pipes. If it's too easy, do the opposite. Tuning these is how real game designers adjust difficulty — small changes make a big difference. Try it."

Highlight lines 18–22.

"Three Actors — the bird and two pipes. The `anchor` on the pipes just controls which edge lines up with the gap. The bird also has `vy` — that's its vertical velocity. Gravity increases it, flapping resets it."

## reset functions (lines 25–36, ~20 sec)

"`reset_pipes` picks a random gap position and moves both pipes to the right edge. `reset_game` zeroes the score, puts the bird back in the middle, and resets the pipes. Same pattern as last time."

## update (lines 39–71, ~45 sec)

"The `update` function — runs every frame."

Highlight lines 42–49.

"First, it checks if you're on the start screen or game over screen. If you press SPACE on the start screen, it starts the game. If you press R on game over, it goes back to start. Same `keyboard.` pattern you've been using."

Highlight lines 51–52.

"If we're not in any of those states and we're not playing, do nothing."

Highlight lines 54–55.

"Here's the flap. If you're holding SPACE, the bird's velocity gets set to `FLAP`, which is negative — so the bird goes up. Same pattern as arrow keys in the chase game."

Highlight lines 57–58.

"Every frame, gravity adds to the velocity, and the bird moves by that amount. So the bird is always falling unless you press SPACE."

Highlight lines 60–65.

"Pipes slide left every frame. When they go off screen, they reset to a new random position and the score goes up."

Highlight lines 67–71.

"Two ways to lose: hit a pipe, or fly off the top or bottom. Same `colliderect` you've used before."

## draw (lines 74–87, ~10 sec)

"The `draw` function — three states, three screens. I'll let you form your own opinions about how these look."

**Don't linger. Don't read the text values. Move on.**

## Optional: on_key_down flap upgrade (~45 sec)

"One more thing. Right now, holding SPACE makes the bird fly up continuously. Real Flappy Bird doesn't work that way — each tap gives you one flap.

There's an optional upgrade on the page. You take the flap check out of `update()` and put it in a new function called `on_key_down()`. PyGame Zero calls that function once the moment a key is pressed — not every frame. So instead of holding SPACE to fly, you have to tap it each time. One tap, one flap.

It's totally optional. The game works fine either way — it's just a different feel."

## Closing (~10 sec)

"That's the code. Run it, play it, and tell me what you think about the design."

---

**Total time**: ~4 minutes
