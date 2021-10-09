import sys
import pprint
from collections import defaultdict

# Note: text should be a short phrase for bars to fit in IDLE window
text = 'Like the castle in its corner in a medieval game, I foresee terrible \
trouble and I stay here just the same.'

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

mapped = defaultdict(list)
for character in text:
    # 小文字に統一
    character = character.lower()
    if character in ALPHABET:
        mapped[character].append((character))
        # print(mapped)

print("\nYou may need to strech console window if text wrapping occurs.\n")
print("text = ", end="")
print("{}\n".format(text), file=sys.stderr)
pprint.pprint(mapped, width=110)
