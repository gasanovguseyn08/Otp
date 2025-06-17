
from otp_core.generator import create_token
from otp_core.validator import store_token, is_token_valid

def dispatch_code(user):
    code = create_token()
    store_token(user, code)
    print(f"Code for {user}: {code}")

def validate_code(user, input_code):
    if is_token_valid(user, input_code):
        print("Code confirmed.")
    else:
        print("Invalid or expired code.")

# Example usage
if __name__ == "__main__":
    user_id = "user123"
    dispatch_code(user_id)
    user_input = input("Enter received code: ")
    validate_code(user_id, user_input)
