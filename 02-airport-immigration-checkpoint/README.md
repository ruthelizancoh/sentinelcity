# Airport Immigration Checkpoint

## The Scenario

Immigration officers inspect arriving passengers, verifying documents
and eligibility before allowing entry into a country. This program
simulates a simplified version of that checkpoint decision.

## What It Does

Asks whether the traveller has a valid passport, has a visa, their age,
and whether they're a returning citizen. Based on those answers, it
decides whether entry is approved or denied.

## Rules Used

- **Returning citizens** are approved if their passport is valid.
- **Foreign visitors** are approved only if they have BOTH a valid
  passport AND a visa.
- Anyone not meeting either path above is denied entry.

## How to Run It

​```
python immigration_checkpoint.py

​```

## Concepts Practiced

`if` / `elif` / `else` with two separate valid approval paths,`and`
for combining required conditions, and deliberately modeling a
real-world rule as two clear, separate checks rather than one
tangled condition.