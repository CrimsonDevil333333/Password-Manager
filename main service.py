from modules.face_verification.face import face_verify
from modules.face_verification.face_image_genrator import greyscale_image
from modules.Data.json_file_reader import search_id_pass,admin_pass_retry,reset_password, new_signup,site_configs,normal_data
global admin
global total_entries_in_id
total_entries_in_id = 0
# Face reader for facial rec to log into account 
def login_encoding():
    n = face_verify()
   
    if n == 1:
        print("Welcome Sir! How may i help you ")
    else:
        if n == 0:
            print("No target found")

# to register a face 
def register_face():
    print("now scanning face so don't move")
    greyscale_image()
    print("face scanned!")

# login with id and password from the dataBase 
def login(id_name,passwords):
    global admin
    (n , m) = search_id_pass(id_name,passwords)
    if m == 99999:
        print("Invalid login info pls enter correct info and try again !")
        admin =  m
    else:
        if n == 1 :
            print("welcome sir! ")
            admin = m
        elif n==2 :
            print("enter pass and try again")
            admin = m
        elif n == 3:
            print("wrong pass")
            admin = m
        else:
            print("some error accured ")
# retry password function
def retryPass(passwords):
    global admin 
    if admin == 99999:
        print("not a valid user ")
    else :
        n = admin_pass_retry(admin,passwords)
        if n==1:
            print("pass matched ")
        elif n == 0:
            print("pass is not right pls retry or else click ok forgot pass !")

# forgot pass enter whatsappno and new password
def forget_pass(whatsappNo,new_pass):
    global admin
    if admin == 99999:
        print("not valid user")
    else :
        print("now verifying info with whatsapp no pls wait....")
        n = reset_password(admin,whatsappNo,new_pass)
        if n == 1:
            print("new pass is now ",new_pass)
        else :
            print("invalid verification no !")

# new user
def new_user_signup(name,password,whatsapp):
    n = new_signup(name,password,whatsapp)
    if n == 1:
        print("please use diff username the one choosen allready exixts!")
    if n == 2:
        print(f"COngratulation's !  Id has been created sucessfull by this name:-{name}")            

# retreving saved ids and passwords in the account !
def retreve_old_data():
    global admin
    global total_entries_in_id
    (n,d,l) = site_configs(admin)
    if n == 0:
        print("not valid admin ")
    elif n == 1:
        print("invalid user!")
    elif n == 2:
        total_entries_in_id = l
    elif n == 3:
        print("No saved passwords found !")


# total entries split data count for gui 
def split_data():
    global total_entries_in_id
    global admin
    n = normal_data(admin)
    if total_entries_in_id == 0:
        print("no entry in cache!")
    else:
        for i in range(1,total_entries_in_id+1,1):
            line = n[f"{i}"]
            line = line.split("`;;`")
            l1 = line[0]  # l1 is website !
            l2 = line[1]  # l2 is saved login id !
            l3 = line[2]  # l3 is saved login id password !
            split_line_transfer(l1,l2,l3)

# to transfer splited data and print it !
def split_line_transfer(a,b,c):
    print(a,b,c)

# main loop for testing and stuff!
if __name__ == "__main__":
    login("adarsh","1234")
    forget_pass("123","4321")
    