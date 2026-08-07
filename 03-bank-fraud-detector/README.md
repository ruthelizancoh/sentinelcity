# Bank Fraud Detection Simulator

## The Scenario

Banks process millions of transactions every hour, checking for
suspicious behavior before approving them. This program simulates a
simplified version of that early-stage fraud check.

## What It Does

Asks for a transaction amount, the number of failed PIN attempts, and
whether the physical card was present. Based on those answers, it
classifies the transaction as HIGH risk, MEDIUM risk, or SAFE.

## Rules Used

- **HIGH risk:** transaction amount over $5,000, OR 3 or more failed
  PIN attempts (either alone is enough)
- **MEDIUM risk:** the card was not physically present
- **SAFE:** anything not matching either rule above

## How to Run It

​```

python fraud_detector.py

​```

## Concepts Practiced

`or` for combining independently-sufficient warning conditions
(contrast this with Project 1's `and`, which required both facts
together), and choosing `float` vs `int` based on what a value
honestly represents in the real world.