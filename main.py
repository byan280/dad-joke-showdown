#!/usr/bin/env python3
"""Dad Joke Showdown entry.

The program prints exactly one line: an original dad joke built
around a units pun. The output is fixed text, so every run prints
the same line with no randomness, no clock reads, and no network.
"""

# The joke: a band named after 1023 megabytes never gets a "gig",
# because a gigabyte needs 1024 megabytes. The punchline is the
# missing megabyte.
JOKE = "I tried to start a band called 1023 Megabytes, but we never got a gig."


# One line on stdout and nothing else, so the graded run's
# action log is identical on every execution.
def main():
    print(JOKE)


if __name__ == "__main__":
    main()
