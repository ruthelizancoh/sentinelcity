# Cyber Threat Monitoring Console

## The Scenario

You've just joined a cybersecurity company as a Junior Security Analyst.
A Security Operations Center (SOC) monitors employee login attempts
around the clock, checking whether each one looks suspicious. This
program simulates a simplified version of that triage tool.

## What It Does

Asks for a username, number of failed login attempts, whether a VPN was
used, and the hour of the login attempt (0-23). Based on those answers,
it classifies the login as **HIGH**, **MEDIUM**, or **LOW** risk, and
prints a recommended action.

## Rules Used

- **HIGH risk:** 5 or more failed attempts, AND no VPN used
- **MEDIUM risk:** 3-4 failed attempts, OR a login between 10 PM and 5 AM
- **LOW risk:** anything not matching the above

## How to Run It

​```
python threat_monitor.py
​```

Answer each prompt when asked.

## Concepts Practiced

Comparison operators, `if` / `elif` / `else`, `and` / `or`, `.lower()`
for case-insensitive comparison, and careful ordering of conditions
from most to least severe.
