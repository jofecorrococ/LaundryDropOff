import datetime

# Global list to store reservations
reservations = []

# ========== LOGIN MENU ==========
def main_menu():
    while True:
        print("\n=== PHINMA COC | Facility Reservation System ===")
        print("[1] Admin Login")
        print("[2] User Login")
        print("[0] Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            login("admin")
        elif choice == "2":
            login("user")
        elif choice == "0":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")

# ========== LOGIN SYSTEM ==========
def login(role):
    print(f"\n=== {role.capitalize()} Login ===")
    username = input("Username: ")
    password = input("Password: ")

    # Predefined credentials
    if role == "admin" and username == "admin" and password == "admin123":
        admin_dashboard()
    elif role == "user" and username == "user" and password == "user123":
        user_dashboard()
    else:
        print("Invalid credentials. Try again.")

# ========== USER MENU ==========
def user_dashboard():
    while True:
        print("\n=== USER MENU ===")
        print("[1] Make a Reservation")
        print("[2] View My Reservations")
        print("[0] Logout")
        choice = input("Enter choice: ")

        if choice == "1":
            make_reservation()
        elif choice == "2":
            view_user_reservations()
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")

# ========== ADMIN MENU ==========
def admin_dashboard():
    while True:
        print("\n=== ADMIN MENU ===")
        print("[1] View All Reservations")
        print("[2] Approve/Reject a Reservation")
        print("[0] Logout")
        choice = input("Enter choice: ")

        if choice == "1":
            view_all_reservations()
        elif choice == "2":
            update_reservation_status()
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")

# ========== USER FUNCTION: MAKE RESERVATION ==========
def make_reservation():
    print("\n=== Make a Reservation ===")
    name = input("Enter your full name: ")
    room = input("Enter room to reserve (e.g. Gym, Lab, Hall): ")
    date_str = input("Enter date (YYYY-MM-DD): ")
    time_str = input("Enter time (HH:MM, 24-hour format): ")

    # --- VALIDATE DATE AND TIME ---
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        time = datetime.datetime.strptime(time_str, "%H:%M").time()

        # Prevent past dates
        if date < datetime.date.today():
            print(" Error: Cannot reserve for a past date.")
            return

        # Save reservation data
        reservation = {
            "name": name,
            "room": room,
            "date": date_str,
            "time": time_str,
            "status": "Pending"
        }
        reservations.append(reservation)
        print("Reservation submitted successfully and is now pending approval.")

    except ValueError:
        print("Invalid date or time format. Please try again.")

# ========== USER FUNCTION: VIEW MY RESERVATIONS ==========
def view_user_reservations():
    print("\n=== My Reservations ===")
    name = input("Enter your name to check your reservations: ")
    found = False
    for r in reservations:
        if r["name"].lower() == name.lower():
            print(f"- Room: {r['room']}, Date: {r['date']}, Time: {r['time']}, Status: {r['status']}")
            found = True
    if not found:
        print("No reservations found.")

# ========== ADMIN FUNCTION: VIEW ALL ==========
def view_all_reservations():    
    print("\n=== All Reservations ===")
    if not reservations:
        print("No reservations yet.")
        return
    for i, r in enumerate(reservations, 1):
        print(f"[{i}] {r['name']} - {r['room']} - {r['date']} {r['time']} - {r['status']}")

# ========== ADMIN FUNCTION: APPROVE/REJECT ==========
def update_reservation_status():
    view_all_reservations()
    if not reservations:
        return

    try:
        index = int(input("\nEnter reservation number to update: ")) - 1
        if 0 <= index < len(reservations):
            print("1 - Approve\n2 - Reject")
            action = input("Choose action: ")
            if action == "1":
                reservations[index]["status"] = "Approved"
                print("Reservation approved.")
            elif action == "2":
                reservations[index]["status"] = "Rejected"
                print("❌ Reservation rejected.")
            else:
                print("Invalid choice.")
        else:
            print("Invalid reservation number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# ========== START PROGRAM ==========
if __name__ == "__main__":
    main_menu()
