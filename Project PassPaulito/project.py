import os   #import cái này để kiếm Database.txt trên máy tính
import csv  #import cái này để tạo file, chỉnh sửa file txt
import pyfiglet #import cái này để làm ascii art
import secrets  #import cái này để làm password generator
import string   #hơi dư nhưng mà import cái này để string đừng có hư
import math
from collections import defaultdict

def main():
    check_database() #function kiểm tra database có mặt hay không, nếu không thì tạo mới
    welcome_message()   #function chào mừng người dùng
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_password_manual() #function tạo mật khẩu manually
        elif choice == "2":
            add_password_auto() #function tạo mật khẩu tự động
        elif choice == "3":
            view_passwords() #function xem database
        elif choice == "4":
            delete_password() #function xóa mật khẩu hiện hành
        elif choice == "5":
            update_password() #function cập nhật mật khẩu
        elif choice == "6":
            print("Exiting program...")
            break   #tắt chương trình
        else:
            print("Invalid option. Try again.")

def check_database():
       if not os.path.exists("Database.txt"):
              with open("Database.txt", "w", newline="") as db: #tạo Database.txt rồi gắn tên db
                     writer=csv.writer(db)
                     writer.writerow(["ID","Website","Username","Password"])    #Hàng đầu tiên
                     print("Database cannot be found, creating a new database")
       else:
              print("Connected to Database successfully")

def welcome_message():
       banner = pyfiglet.figlet_format("Pass Paulito Manager", font="slant")    #Viết tên ascii
       print(banner)
       print("Made by Paul Scott Nguyen")

def show_menu(): #Các options để người dùng chọn
    print("\nOptions:")
    print("1. To add Password manually")
    print("2. To add Password automatically")
    print("3. To see all passwords")
    print("4. To delete a password")
    print("5. To update a password")
    print("6. To exit")

def add_password_manual():  # Option 1
    website = input("Enter Website URL: ").strip().lower()
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()
    
    try:
        with open("Database.txt", "r", newline="") as db:
            reader = csv.reader(db)
            next(reader, None)  # Bỏ hàng đầu tiên (header)
            data = list(reader)
            if data:
                last_id = int(data[-1][0])
            else:
                last_id = 0
    except FileNotFoundError:
        last_id = 0
    
    new_id = last_id + 1
    with open("Database.txt", "a", newline="") as db:  
        writer = csv.writer(db)
        writer.writerow([new_id, website, username, password])
    
    print("Successfully added to database!")

def add_password_auto():  # Option 2
    website = input("Enter Website URL: ").strip().lower()
    username = input("Enter Username: ").strip()
    while True:
         input_length = input("Enter Password Length (int): ").strip()
         if input_length.isdigit():
              password_length=int(input_length)
              if password_length <=0:
                   print("Please enter a positive integer!")
                   continue
              break
         else:
              print("Please enter a valid integer")
                 
    
    characters = string.ascii_letters + string.digits + string.punctuation #password generator
    password = ''.join(secrets.choice(characters) for _ in range(password_length)) #tạo password theo độ dài
    
    try:
        with open("Database.txt", "r", newline="") as db:
            reader = csv.reader(db)
            next(reader, None)  # Bỏ hàng đầu tiên (header)
            data = list(reader)
            if data:
                last_id = int(data[-1][0])
            else:
                last_id = 0
    except FileNotFoundError:
        last_id = 0
    
    new_id = last_id + 1
    with open("Database.txt", "a", newline="") as db:  
        writer = csv.writer(db)
        writer.writerow([new_id, website, username, password])
    
    print("Successfully added to database!")

def view_passwords():
     print("\nView Passwords:")
     print("1. View by ID")
     print("2. View grouped by Website")
     while True:
      choice = input("Choose an option: ").strip()
      if choice == "1":
          view_by_id()
          break
      elif choice =="2":
          view_by_website()
          break
      else:
          print("Invalid option, Please try again!")
          
def view_by_id():
    try:
        with open("Database.txt", "r", newline="") as db:
            reader = csv.reader(db)
            headers = next(reader, None)
            data = list(reader)

            if not data:    #không có data, trừ header
                print("Database is empty.")
                return

            print(f"\n{headers[0]:<4} | {headers[1]:<20} | {headers[2]:<15} | {headers[3]}")
            print("-" * 65)
            for row in data:
                print(f"{row[0]:<4} | {row[1]:<20} | {row[2]:<15} | {row[3]}")
    except FileNotFoundError:
        print("Database file not found.")

def view_by_website():
    try:
        with open("Database.txt", "r", newline="") as db:
            reader = csv.reader(db)
            next(reader, None)
            data = list(reader)

            if not data:
                print("Database is empty.")
                return

            grouped = defaultdict(list) #tạo theo nhóm website, key là website, value là username và password
            for row in data:
                website = row[1]
                grouped[website].append((row[2], row[3]))  # (username, password)

            print()
            for website in sorted(grouped): #định dạng sort alphabet
                print(f"Website: {website}")
                for username, password in grouped[website]:
                    print(f"  - {username}: {password}")
                print()  # Dòng trống giữa các website
    except FileNotFoundError:
        print("Database file not found.")   

def delete_password():
    website = input("Enter Website URL to delete: ").strip().lower()
    username = input("Enter Username: ").strip()

    try:
        with open("Database.txt", "r", newline="") as db:
            reader = csv.reader(db)
            header = next(reader)
            data = list(reader)
    except FileNotFoundError:
        print("Database file not found.")
        return

    # Tìm profile cần xóa
    found = False
    new_data = []

    for row in data:
        if row[1].strip().lower() == website and row[2].strip() == username:
            found = True
            print(f"\nProfile found: {row}")
            confirm = input("Do you want to delete this profile? (Y/N): ").strip().lower()
            if confirm in ["y", "yes"]:
                print("Profile deleted.")
                continue  # Bỏ qua dòng này, không thêm vào new_data
            else:
                print("Deletion cancelled.")
                new_data.append(row)  # Giữ lại dòng này
        else:
            new_data.append(row)

    if not found:
        print("Profile not found.")
        return

    # Ghi lại file với dữ liệu mới (đã xóa nếu cần)
    with open("Database.txt", "w", newline="") as db:
        writer = csv.writer(db)
        writer.writerow(header)  # Ghi lại dòng tiêu đề

    for i, row in enumerate(new_data, start=1):
        writer.writerow([i, row[1], row[2], row[3]])

def update_password():
    website = input("Enter Website URL to update: ").strip().lower()
    username = input("Enter Username: ").strip()

    try:
        with open("Database.txt", "r", newline="") as db:
            reader = csv.reader(db)
            header = next(reader)
            data = list(reader)
    except FileNotFoundError:
        print("Database file not found.")
        return

    found = False
    new_data = []

    for row in data:
        if row[1].strip().lower() == website and row[2].strip() == username:
            found = True
            print(f"\nProfile found: {row}")
            new_password = input("Type your new password: ").strip()
            row[3] = new_password  # Cập nhật cột password
            print("Password updated successfully.")
        new_data.append(row)  # Dù sửa hay không, vẫn append lại

    if not found:
        print("Profile not found.")
        return

    # Ghi lại toàn bộ file và tái đánh số ID
    with open("Database.txt", "w", newline="") as db:
        writer = csv.writer(db)
        writer.writerow(header)
        for i, row in enumerate(new_data, start=1):
            writer.writerow([i, row[1], row[2], row[3]])


if __name__ == "__main__":
    main()


