import time
import sys

def type_lyric(line, char_delay=0.065):
    for char in line:
        print(char, end="", flush=True)
        time.sleep(char_delay)
    print()

def print_lyrics():
    lyrics = [
        "Tu hai toh dil dhadakta hai",
        "Tu hai toh saa'ns aati hai",
        "Tu na toh ghar ghar nahi lagta",
        "Tu hai to darr nahi lagta",
        "Tu hai toh gham na aate hai",
        "Tu hai toh muskurate hai",
        "Ke tere bin so nahi sakte",
        "Kisi ke ho nahi sakte",
        "Tu hai toh...",
        "Tu hai toh...",
    ]
    delays = [2.0, 2.0, 2.5, 2.5, 3.0, 2.5, 2.5, 2.5, 2.5, 2.0]

    print("— Now Playing: \n Now Playing: “Tu hai toh” — Mr and Mrs Mahi\n")
    time.sleep(1.0)

    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])

if __name__ == "__main__":
    print_lyrics()