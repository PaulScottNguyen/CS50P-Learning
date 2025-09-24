guest_list = ["An","Trung","Minh","Giang","Thư","Nhung","Linh","Anh","Bảo"] #List of data
def write_letter(receiver, sender): #Function write_letter that takes two variable
    return f""" 
    ==========LETTER==========
    Dear {receiver}!
    You are cordially invited
    to my party at 7 p.m this
    sunday
    Sincerely!
    {sender}!
    ==========================
    """
    # The """ syntax will keep the formatted text as is

for name in range(len(guest_list)): #Loop statement, len is the number of data in the list
    print(write_letter(guest_list[name], "Paulito"))
    #print the return value of the function write_letter by inputting receiver=guest_list[<position>]
    # and sender="Paulito"