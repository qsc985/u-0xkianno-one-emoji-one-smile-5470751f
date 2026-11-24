#!/usr/bin/env python3
"""One Emoji, One Smile — writes exactly one emoji to /output/entry.txt.

The emoji is the one most likely to make a stranger smile: 🌻 the
sunflower. Weighing the judge's criteria against the candidates:

- 🙂 the default slight smile: warm enough, but it is the first smiley
  that comes to mind, so it loses on "chosen rather than default".
- 🥰 the smiling face with hearts: warm, but it reads as affectionate
  and intimate — odd coming from a stranger.
- 😀 the big grin: friendly, but it is the stock smiley face, the
  most generic pick of all, and it loses to anything more considered.
- 🌻 the sunflower: bright and cheerful at a glance, kind without
  words, understood the same way by any age or background, no irony
  and no in-joke, and it feels deliberately picked rather than the
  default face. A flower is a gift anyone can accept from a stranger.

The sunflower wins on warmth, universality, and being chosen.
"""

import os

EMOJI = "🌻"


def main() -> None:
    emoji = EMOJI.strip()
    # Gate: 1-8 UTF-8 characters, not only whitespace, exactly one emoji.
    # The gate counts characters, so a single code point is safely inside it;
    # the file must contain nothing else — no newline, no caption.
    assert 1 <= len(emoji) <= 8, f"emoji is {len(emoji)} characters"
    assert emoji.strip(), "emoji must not be only whitespace"
    assert len(emoji) == 1, "entry must be exactly one emoji"
    assert not emoji.isspace(), "emoji must not be whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(emoji)


if __name__ == "__main__":
    main()
