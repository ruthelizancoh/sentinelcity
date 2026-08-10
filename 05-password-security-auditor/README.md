# Password Security Auditor

## The Scenario

Whenever you create an account online, the system checks whether your
password is strong enough and correctly confirmed. This program
simulates a simplified version of that basic check.

## What It Does

Asks for a password and a confirmation of that password. It checks
whether they match, and if they do, whether the password is at least
8 characters long.

## Rules Used

- If the two entries don't match: reject immediately, before checking
  anything else.
- If they match and the password is 8+ characters: Strong password.
- If they match but the password is under 8 characters: Weak password.

## How to Run It

​​```
python password_auditor.py
​```

## Important Note

This project is a simplified simulation for practicing conditional
logic. It is **not** an example of real, secure password handling :
real systems never display or compare raw passwords the way this
simple learning exercise does, and use proper encryption, which is
well beyond this stage of the course.

## Concepts Practiced

`!=` for detecting a mismatch before any other check runs, and `len()`
for a simple, readable length requirement.
