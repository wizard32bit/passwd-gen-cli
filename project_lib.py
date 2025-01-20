#import necessary modules
import random, string
#check the password length
def length():
    while True:
        passwd_len= input("input passwod length (minimum 8): ")
        if passwd_len.isdigit():
            passwd_len= int(passwd_len)
            if passwd_len<8:
                print("the input length is lower than 8")
            else:
                break
        else:
            print("the input is not numeric")
        
    return passwd_len

#genrating password
def generate(mode):
    # Password character sets
    lower_case = list(string.ascii_lowercase)
    upper_case = list(string.ascii_uppercase)
    digits = list(string.digits)
    symbols = list(string.punctuation)

    # Randomize lists
    random.shuffle(lower_case)
    random.shuffle(upper_case)
    random.shuffle(digits)
    random.shuffle(symbols)

    def get_custom_pattern():
        while True:
            pattern = input("Enter the pattern (e.g., (3,5,7,0)): ").strip()
            
            # Validate the pattern
            if not (pattern.startswith('(') and pattern.endswith(')')):
                print("Invalid pattern, please retry. Input should be in the form (l,u,d,p).")
                continue
            
            pattern = pattern[1:-1]  # Remove parentheses
            numbers = pattern.split(',')
            
            if len(numbers) != 4:
                print("Invalid pattern, please enter exactly four numbers.")
                continue
            
            try:
                numbers = [int(num.strip()) for num in numbers]
                if any(num < 0 for num in numbers):
                    print("Numbers cannot be negative.")
                    continue
            except ValueError:
                print("Invalid pattern, please enter valid numbers.")
                continue
            
            passwd_len = sum(numbers)
            if passwd_len < 8:
                print("Password length must be at least 8 characters.")
                continue
            
            return passwd_len, numbers

    output = ""

    if mode == "random":
        passwd_len = length()
        all_chars = lower_case + upper_case + digits + symbols
        output = ''.join(random.choices(all_chars, k=passwd_len))
    
    elif mode == "custom":
        print("===============================================================================================================")
        print("\nCustom Mode:")
        print("You have chosen to generate your password in Custom Mode.")
        print("The input has to be in form of a tuple (e.g., (3,5,7,0)) called `Pattern`.")
        print("the Pattern should be in the form of (lowercase, uppercase, digits, punctuation).")
        print("Unwanted characters: in case you don't want a particular type of characters, make sure to put 0 in the pattern.")
        print("The order matters, make sure to follow it to get the best results.\n")
        print("===============================================================================================================\n")

        passwd_len, numbers = get_custom_pattern()

        l_count, u_count, d_count, s_count = numbers
        counts = {'l': l_count, 'u': u_count, 'd': d_count, 's': s_count}
        
        # Ensure the output contains the exact number of each character type
        chosen_chars = []
        
        chosen_chars.extend(random.choices(lower_case, k=l_count))
        chosen_chars.extend(random.choices(upper_case, k=u_count))
        chosen_chars.extend(random.choices(digits, k=d_count))
        chosen_chars.extend(random.choices(symbols, k=s_count))
        
        # Shuffle the list to ensure randomness
        random.shuffle(chosen_chars)
        
        output = ''.join(chosen_chars)

    return output
