import json
global path_of_json
path_of_json = "demo.json"
global entry_count
entry_count = 0

with open(path_of_json, "r") as read_file:
    data = json.load(read_file)

def normal_data(admin = None):
    if admin == None or admin == 99999:
        return None
    else :
        return data[f"{admin}"]

def site_configs(admin = None):
    if admin == None:
        return (0,0,0)
    elif admin == 99999:
        return (1,0,0)
    else:
        try:
            entry_count_by_uid(admin)
            return (2,data[f"{admin}"],entry_count)
        except:
            return (3,0,0)

def entry_count_by_uid(uid = None):
    global entry_count
    if uid == None:
        print("No uid !!!!!!!!!!")
    else:
        countss = 0
        try:
            for i in range(1,50,1):
                if data[f"{uid}"][f"{i}"] != None:
                    countss = countss + 1
                elif data[f"{uid}"][f"{i}"] == None:
                    print("BadIndex!")
        except:
            entry_count = countss
            print("Total entries are ! ",countss)


def admin_pass_retry(name=None,password = None ):
    count = 0
    if data[f'{name}']["password"] == password:
        count = 2
        return (count)
    else:
        return (count)
    
def new_signup(name = None,password=None,wtsappNo = None):
    countss = 1
    try:
        for i in range(1,100,1):
            

            if data[f'{i}'] != None :
                countss = countss + 1

            
            else:
                
                print("error")
                    

    except:
        for i in range(1,countss,1):
            if data[f'{i}']['name'] == name:
                return 1
            
        data[f'{countss}'] = {'name':f'{name}' ,'password':f'{password}' ,'wtsno':wtsappNo }
        
        dump_json_instant()

        print(i,data[f'{i}'])
        return (2) #Sucessfull signup !

def search_id_pass(name=None,password=None):
    count = 0
    try:
        for i in range(1,100,1):
            if data[f'{i}']['name'] == name :
                if data[f'{i}']["password"] == password :
                    count = 1
                    return (count,i)
                elif password == None or password == "":
                    count = 2
                    return (count,i)
                else :
                    count = 3
                    return (count,i)
                
    except:
        print("entered login info is not valid !")
        i = 99999
        return (count,i)   

def search_admin(name = None):
    try:
        for i in range(1,100,1):
            if data[f'{i}']['name'] == name :
                return i
                
    except:
        print("entered login info is not valid !")
        i = 99999
        return i   

def dump_json_instant():
    global path_of_json
    with open(path_of_json, "w") as write_file:
        json.dump(data, write_file, indent=2)
        print(" dump done")

def reset_password(name = None , wtsappNo=None, newPasswords=None ):
    if data[f"{name}"]["wtsno"] == wtsappNo and newPasswords != None:
        data[f"{name}"]["password"] = newPasswords
        
        dump_json_instant()

        print("password changed")

        return 1
    else :
        return 0
