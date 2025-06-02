#!/bin/env python3

import argparse
import random
import math
import decimal

# Set precision for decimal arithmetic
decimal.getcontext().prec = 128 # Adjust this value based on your precision needs

def simulate_player(rounds, loss, gain):
    tails = 0
    heads = 0
    for _ in range(rounds):
        if random.random() < 0.5:
            heads += 1
        else:
            tails += 1

    # Convert to Decimal for arbitrary precision arithmetic
    loss_dec = decimal.Decimal(str(loss))
    gain_dec = decimal.Decimal(str(gain))
    return loss_dec ** heads * gain_dec ** tails


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Toss a coin")
    parser.add_argument("--rounds", type=int, default=100, help="Number of rounds")
    parser.add_argument("--players", type=int, default=100, help="Number of players")
    parser.add_argument("--loss", type=float, default=0.6, help="Loss rate")
    parser.add_argument("--gain", type=float, default=1.5, help="Gain rate")
    args = parser.parse_args()

    results = []

    for player in range(args.players):
        results.append(simulate_player(args.rounds, args.loss, args.gain))

    results.sort()
    
    print("Top 5 results:")
    for i, result in enumerate(reversed(results[-5:]), 1):
        print(f"  {i}. {result}")

    print("Bottom 5 results:")
    for i, result in enumerate(results[:5], 1):
        print(f"  {i}. {result}")

    total = sum(results)
    average = total / len(results)
    print(f"Total sum:      {total}")
    print(f"Average result: {average}")

    for i in range(len(results)):
        if results[i] >= 1:
            print(f"Top {len(results) - i + 1} players have won")
            break
    

    


