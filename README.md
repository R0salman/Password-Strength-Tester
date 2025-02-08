# Password-Strength-Tester
### A simple Cybersecurity project
A Python script to validate password strength and check against common passwords. It enforces complexity rules and provides a strength score.

# Flowchart
<div style="width: 100%; overflow-x: auto;">
  
```mermaid
flowchart TD;
    A[Start] --> B[Initialize PasswordValidator]
    B --> C[Prompt user for password]
    
    C -->|User enters 'q'| D[Exit Program]
    C -->|User enters password| E[Analyze password]
    
    E --> F[Check for special character]
    F -->|Missing| F1[Add error: 'Password must contain at least one special character'\nDecrease score by 2]
    F -->|Present| F2[Increase score by 3]
    
    F2 --> G[Check for uppercase letter]
    F1 --> G
    G -->|Missing| G1[Add error: 'Password must contain at least one uppercase letter'\nDecrease score by 2]
    G -->|Present| G2[Increase score by 2]
    
    G2 --> H[Check for lowercase letter]
    G1 --> H
    H -->|Missing| H1[Add error: 'Password must contain at least one lowercase letter'\nDecrease score by 2]
    H -->|Present| H2[Increase score by 2]
    
    H2 --> I[Check for number]
    H1 --> I
    I -->|Missing| I1[Add error: 'Password must contain at least one number'\nDecrease score by 2]
    I -->|Present| I2[Increase score by 2]
    
    I2 --> J[Check password length]
    I1 --> J
    J -->|Too short| J1[Add error: 'Password must be at least 12 characters'\nDecrease score by 3]
    J -->|Long enough| J2[Increase score based on length]
    
    J2 --> K[Check if password is too common]
    J1 --> K
    K -->|Common Password| K1[Add error: 'This password is too common'\nSet score to 0]
    K -->|Not common| L[Evaluate Strength]
    
    K1 --> L
    L -->|Score > 10| L1[Set Strength: 'Very Strong']
    L -->|Score > 7| L2[Set Strength: 'Strong']
    L -->|Score > 5| L3[Set Strength: 'Moderate']
    L -->|Score > 2| L4[Set Strength: 'Weak']
    L -->|Score ≤ 2| L5[Set Strength: 'Very Weak']
    
    L1 --> M[Display Results]
    L2 --> M
    L3 --> M
    L4 --> M
    L5 --> M

    M --> |Valid Password| N[Print: 'Password Passed all tests!']
    M --> |Invalid Password| O[Print: 'Password failed, show errors']

    N --> P[Display Strength and Score]
    O --> P

    P --> C[Prompt for another password]

    D[Exit Program] --> Z[End]
```
</div>
# Features:
Validates minimum password length (12 characters).

Requires uppercase, lowercase, numbers, and special characters.

Blocks common passwords (e.g., "password", "admin123")

Generates a strength score and feedback.

## Requirements
Python3
## Password Rules
Minimum length: 12 characters

Uppercase letter: At least 1 (A-Z)

Lowercase letter: At least 1 (a-z)

Number: At least 1 (0-9)

Special character: At least 1 from ~!@#$%^&{()_}.,":<>

Common passwords: Blocked (e.g., "123456", "password")
