import random

def generate_otp(length=6):

    lower = 10**(length-1)
    upper = (10**length) - 1
    return random.randint(lower, upper)

def format_otp(otp, format_type):
    if format_type == "decimal":
        return str(otp)
    elif format_type == "hex":
        return hex(otp)
    elif format_type == "binary":
        return bin(otp)
    else:
        return "Invalid format selected."

def main():
    otp = generate_otp()
    print("OTP generated!")

    print("\nChoose display format:")
    print("1. Decimal")
    print("2. Hexadecimal")
    print("3. Binary")

    choice = input("Enter 1/2/3: ").strip()

    if choice == '1':
        formatted = format_otp(otp, "decimal")
    elif choice == '2':
        formatted = format_otp(otp, "hex")
    elif choice == '3':
        formatted = format_otp(otp, "binary")
    else:
        formatted = "Invalid choice."

    print(f"\nFormatted OTP: {formatted}")

if __name__ == "__main__":
    main()
