from time import sleep, time
CURRENT_USER = {}
# User Roles
HR_ROLE = "hr"
ADMIN_ROLE = "admin"
SALES_ROLE = "sales"
# Users Data Structure
users = {
    "admin_u": {"username": "admin_u", "password": "Hamza234", "role": ADMIN_ROLE},
    "hr_u": {"username": "hr_u", "password": "abc", "role": HR_ROLE},
    "sales_u_a": {"username": "sales_u_a", "password": "Nadiya09", "role": SALES_ROLE},
    "guest_a": {"username": "guest_a", "password": "def", "role": "guest"},
} 
# -------------------------------------------------------------
def login():
    global CURRENT_USER
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print("Verifying credentials...")
    sleep(1)
    found_user = users.get(username) # ইউজারনেমকে key হিসেবে ধরে searching সহজ করা হলো
    
    if found_user and found_user['password'] == password:
        CURRENT_USER = found_user
        print(f"\n✅ Access granted! Welcome, {CURRENT_USER['username']}.")
    else:
        print("\n❌ Access denied! Invalid credentials.")
        CURRENT_USER = {}
# Role Checker decorator
# -------------------------------------------------------------
def role_chucker(allowed_roles):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if CURRENT_USER.get('role') in allowed_roles:
                t1 = time()
                res = func(*args, **kwargs)
                t2 = time()
                
                if func.__name__.endswith("heavy_operation"):
                    print(f"\n✅ Function '{func.__name__}' executed. ⏱️ Time: {round(t2 - t1, 4)}s.")
                elif res is not None:
                    print(f"\n✅ Function '{func.__name__}' execution allowed.")
                
                return res
            else:
                print(f"\n❌ Access denied for '{CURRENT_USER.get('username')}' ({CURRENT_USER.get('role')}).")
                print(f"⚠️ Not authorised for operation '{func.__name__}'.")
                return None
        return wrapper
    return decorator

# Protected Functions
@role_chucker([ADMIN_ROLE, HR_ROLE])
def sum_calculator(a: int, b: int) -> int:
    """Calculates the sum of two integers."""
    return a + b
@role_chucker([ADMIN_ROLE])
def multiplication_operation(a: int, b: int) -> int:
    """Calculates the multiplication of two integers."""
    return a * b

@role_chucker([ADMIN_ROLE, SALES_ROLE])
def database_update_operation():
    """Simulates a database update."""
    sleep(1) 
    return "Database updated"

@role_chucker([HR_ROLE])
def generate_report_heavy_operation():
    """Simulates a heavy report generation process."""
    sleep(2) 
    return "Report Data"
# Main Program Execution
if __name__ == '__main__':
    print("--- User Authentication System ---")
    # 1. Login attempt (যেমন: admin_u, 123)
    login()

    print("\n--- Testing Role-Based Access & Operations ---")

    res_sum = sum_calculator(10, 20)
    res_mul = multiplication_operation(5, 8)
    res_db = database_update_operation()
    res_report = generate_report_heavy_operation()
    print(f"Sum result: {res_sum}")
    print(f"Multiplication result: {res_mul}")
    print(f"Database update status: {res_db}")
    print(f"Report status: {res_report}")
