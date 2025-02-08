import re

class PasswordValidator:
    def __init__(self):
        self.min_length = 12
        self.special_char = '[~!@#$%^&{()_}.,":<>]'
        self.common_pwd = {
            '123456', 'admin', '12345678', '123456789', '1234', '12345', 'password', '123', 'Aa123456', '1234567890',
            'unknown', '1234567', '123123', '111111', 'password', '12345678910', '000000', 'admin123', '********', 'user',
        }
        
    def password_checker(self, password):
        errs = []
        StrScore = 0
        
        if not re.search(self.special_char, password):
            errs.append('Password must contain at least one special character')
            StrScore -= 2
        else:
            StrScore += 3
        
        if not re.search(r'[A-Z]', password):
            errs.append('Password must contain at least one uppercase letter')
            StrScore -= 2
        else:
            StrScore += 2
        
        if not re.search(r'[a-z]', password):
            errs.append('Password must contain at least one lowercase letter')
            StrScore -= 2
        else:
            StrScore += 2
        
        if not re.search(r'\d', password):
            errs.append('Password must contain at least one number')
            StrScore -= 2
        else:
            StrScore += 2
        
        if len(password) < self.min_length:
            errs.append(f'Password must be at least {self.min_length} characters.')
            StrScore -= 3
        else:
            StrScore += len(password) // 6
        
        if password.lower() in self.common_pwd:
            errs.append('This password too common')
            StrScore = 0
            
        
        strg = "Very Weak"
        if StrScore  > 10:
            strg = "Very Strong"
        elif StrScore > 7:
            strg = "Strong"
        elif StrScore > 5:
            strg = "Moderate"
        elif StrScore > 2:
            strg = "Weak"
            
        return {
            'valid': len(errs) == 0,
            'errors': errs,
            'strength': strg,
            'score': StrScore,
        }

def main():
    validator = PasswordValidator()
    
    print("*+=== Password Strength Tester ===+*")

    # Loop for convenience
    while True:
        try:
            password = input("Enter password [or press q to quit]: ")
            
            if password.lower() == "q":
                print("\n Exiting the program...")
                break
            
            print("\n Analyzing the password...", end='', flush=True)
            rsult = validator.password_checker(password)
            
            if rsult['valid']:
                print("Password Passed all the test, This password is Valid!")
                print(f"Strength: {rsult['strength']}")
            else:
                print("\nPassword didn't pass the test.")
                print("\nIssues Found:")
                for error in rsult['errors']:
                    print(f" {error}")
                    
            print(f"Strength Score: {rsult['score']}")
            
        except KeyboardInterrupt:
            print("\n Exiting the program...")
            break
        except Exception as e:
            print(f"\n An error occurred: {str(e)}")
            
if __name__ == "__main__":
    main()
