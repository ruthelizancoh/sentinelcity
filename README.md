# SentinelCity

A portfolio of five small, complete Python programs, each simulating a
real decision-making system used by a real kind of organization — a
cybersecurity team, an airport, a bank, an antivirus company, and an
account security team.

Every project in this repository uses only comparison operators
(`==`, `!=`, `>`, `<`, `>=`, `<=`), `if` / `elif` / `else` chains, and
boolean logic (`and`, `or`, `not`) — no loops, functions, or data
structures yet. Each project deliberately practices identifying whether
a real-world rule is genuinely an `and` situation (both facts must be
true together) or an `or` situation (either fact alone is enough).

## Projects

| # | Project | Folder | Decides |
|---|---|---|---|
| 1 | Cyber Threat Monitoring Console | [`01-cyber-threat-monitor`](./01-cyber-threat-monitor) | Login risk: Low, Medium, or High |
| 2 | Airport Immigration Checkpoint | [`02-airport-immigration-checkpoint`](./02-airport-immigration-checkpoint) | Whether to approve entry |
| 3 | Bank Fraud Detection Simulator | [`03-bank-fraud-detector`](./03-bank-fraud-detector) | Transaction risk: Safe, Medium, or High |
| 4 | Malware Detection Scanner | [`04-malware-scanner`](./04-malware-scanner) | File status: Safe, Suspicious, or Dangerous |
| 5 | Password Security Auditor | [`05-password-security-auditor`](./05-password-security-auditor) | Whether a password is accepted |

Each folder above contains its own detailed README (explaining that
specific project's scenario, rules, and how to run it) and its own
complete, runnable Python file.

## How to Run Any Project

1. Make sure Python is installed on your machine.
2. Open a terminal inside this repository.
3. Move into whichever project folder you want to run, for example:

​```

cd 01-cyber-threat-monitor
python threat_monitor.py

​```

4. Answer each prompt when asked.

## Why I Built This

*This is my fourth Git and GitHub project, and my first repository
containing multiple related sub-projects rather than a single
standalone program. It was built while learning conditional logic
(`if` / `elif` / `else`, comparison operators, and boolean logic) in
Week 2, Day 8 of the 3IXL Elite Python Programming Foundations course.
Each of the five projects simulates a different real-world security or
verification system, chosen specifically to practice recognizing when
a real rule requires `and` versus `or` logic.*

## About Me

An aspiring software engineer focused to archieve a safe and comfortable digital environment.Enjoy.