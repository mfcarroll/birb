import argparse
import random

# Emojis are defined as a list of strings to prevent multi-character
# emojis (like the phoenix 🐦‍🔥) from being split apart.
BIRBS = [
    "🐦", "🐤", "🐧", "🐔", "🐣", "🐥", "🦉", "🕊️", "🦅", "🐦‍🔥",
    "🦜", "🐦‍⬛", "🦃", "🪿", "🦩", "🐓", "🦆", "🦢", "🦤", "🦚",
    "🪶", "🪽"
];

def main():
    """Prints a number of random bird emojis to the console."""
    parser = argparse.ArgumentParser(description="Print some random bird emojis.")
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        default=1,
        help="the number of bird emojis to print (default: 1)",
    )
    args = parser.parse_args()

    for _ in range(args.number):
        print(random.choice(BIRBS), end="")
    print()


if __name__ == "__main__":
    main()
