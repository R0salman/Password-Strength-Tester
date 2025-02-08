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
*For Mobile Users📱* -[ViewDigram](https://kroki.io/mermaid/svg/eNqVld1um0AQhe_7FNMr3zRSTBJVaqVIiX8A_yRWnaZSqS82sDEoeNfdXeK64gX6Hn2yPkmHWRwDIY7iC8tjzjkz38KyS8XWMdz0P78D_FwEc8OUWcDR0TlcBr5ITMLS5DeHGdN6I1V0i2XEjFQLMlySshfMlFytDWSaK7iXCtal3Kroq1dI86-FggvDlYbOz04O_WDwKzGAAUvFVosXpLu8HAbBhWDpFkdq6TGgcYZBL-bhAw2i1zxEBAhjpliIWVY9pA7TROtELHMYdoOLKAKulFSfoLODhVWmDYRSGJYIYAZSzvAPKfjz3M4P0eehQgFeDKXicLcFp9ptprhGHOzm4Mo2pScVjKFDHG6FI1uvuQoLR8rNHqNrhVS4dSb3zUzNHoeQ3DqS24bkVJBci-RVkFK5aUFyLZJHhVdH8t6M1OxxCMmrI3mvIXkWya8giWx1twPxLIhPhV8H8d8MYpMPje_Xx_dfG9-344_K8Xe7CXuKpYnLTMswomJEDW6kBB1LhS1Ghyju-B6g6-z3iW5lKJ9-22IixRI3vsyWMTZ5zoE_I1yU2qTWbpHGJVJyv6dKNBicPJSrlRRlMws3pmJMnXt0-elll8O4jngTJ_qFTMSac1OOaCQcLyq5V9KUshwmweCRpRkzHOZGNRHGdqgJFRMyzynyHLrHaO4GRZedEUe65Wpb1LhmnUWL6yOanKbpgP4M9SdN_VRGXOHErQ4HHadNxzfOHlrU__78Jf1ZK0bFZJ12MaZBP9HrlG3hC9dZanSZa-_21BYn1eK0WpyVBVVTKnI6xir3-QpPsESY6lNc_MDnjKUpGK6Nfl9OVib44rGRcf08454lKY8-FBtmYx8ijSkUc0Uxsye03VoAExHQYtl211ZnTbP6cVu8cpiQJubVE5eUjWOVfN-DgYgW_wGFU2-a)
</div>

# Features:
Validates minimum password length (12 characters).

Requires uppercase, lowercase, numbers, and special characters.

Blocks common passwords (e.g., "password", "admin123")

Generates a strength score and feedback.

# Requirements
Python3
## Password Rules
Minimum length: 12 characters

Uppercase letter: At least 1 (A-Z)

Lowercase letter: At least 1 (a-z)

Number: At least 1 (0-9)

Special character: At least 1 from ~!@#$%^&{()_}.,":<>

Common passwords: Blocked (e.g., "123456", "password")
