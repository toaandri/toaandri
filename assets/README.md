# Profile animations

Six original, looping GIF illustrations used by the profile README. The black and silver palette follows the original profile design. Titles remain readable throughout each loop. Static PNG alternatives are in `stills/`.

These are conceptual illustrations, not recordings of the applications or evidence of training performance. The Stick Balancing loop does not represent a learned policy. Ticket's scan artwork is decorative and contains no valid admission code.

Regenerate from the repository root:

```sh
python -m pip install -r scripts/requirements.txt
python scripts/generate_profile_animations.py
```

The generator looks for Arial/Consolas on Windows and Liberation Sans/DejaVu Sans Mono on Linux. If unavailable, it uses Pillow's bundled font. `PROFILE_FONT_DIR` can point to an additional font folder. No network, credentials or third-party images are needed. Font choice can slightly change lettering across machines.

Each loop contains 48 frames at 100 ms per frame (4.8 seconds), with no flashing or rapid cuts. GitHub's image embedding does not offer an in-image pause control; the profile links to still illustrations.
