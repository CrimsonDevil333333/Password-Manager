import kivy, os, sys
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import time
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from modules.face_verification.face import face_verify
from modules.face_verification.face_image_genrator import greyscale_image
from modules.Data.json_file_reader import search_id_pass,admin_pass_retry,reset_password, new_signup,site_configs,normal_data,search_admin
global admin
global total_entries_in_id
total_entries_in_id = 0
global flag
flag = 0 
global point_location_track
point_location_track = 0

kivy.require("1.10.1")


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




def once_time_cache_loop():
    if 1 == 1:
        global flag
        if flag == 0:
            global admin
            global total_entries_in_id
            global point_location_track
            flag = 1
            (n,d,l) = site_configs(admin)
            if n == 0:
                print("not valid admin ")
            elif n == 1:
                print("invalid user!")
            elif n == 2:
                total_entries_in_id = l
                point_location_track = 1
            elif n == 3:
                print("No saved passwords found !",d)



class saved_user_data(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        
        self.logout = Button(text="logOut")
        self.logout.bind(on_press=self.logout_menu)
        self.add_widget(self.logout)

        self.newField = Button(text="Add New Entry")
        self.newField.bind(on_press=self.newfield_page)
        self.add_widget(self.newField)
        once_time_cache_loop()
        global admin
        global total_entries_in_id
        global point_location_track
        
        
# need to add start pieces:-

        D = normal_data(admin)
        
        if total_entries_in_id == 0:
            point_location_track = 0
            l1 = "No data!"
            l2 = "No data!"
            l3 = "No data!"
        else:
            if point_location_track > 0 and point_location_track <= total_entries_in_id+1 :
                line = D[f"{point_location_track}"]
                line = line.split("`;;`")
                l1 = line[0]  # l1 is website !
                l2 = line[1]  # l2 is saved login id !
                l3 = line[2]  # l3 is saved login id password !

        self.add_widget(Label(text= "Website :- "))
        
        self.l1_label = Label(text = f"{l1}")
        self.add_widget(self.l1_label)
        
        self.id_label = Label(text="ID :- ")
        self.add_widget(self.id_label)

        self.l2_label = Label(text = f"{l2}")
        self.add_widget(self.l2_label)

        self.add_widget(Label(text= "Password :- "))
        
        self.l3_label = Label(text = f"{l3}")
        self.add_widget(self.l3_label)
        

        self.prev = Button(text="previous")
        self.prev.bind(on_press=self.prev_menu)
        self.add_widget(self.prev)
        
        self.next = Button(text="next")
        self.next.bind(on_press=self.next_menu)
        self.add_widget(self.next)


    def logout_menu(self, isinstance):
        info = "Logging out now ..... \nPlease wait!"
        o_s.info_page.update_info(info)
        o_s.screen_manager.current = "Info"
        Clock.schedule_once(self.login_button_shift,1.3)

    def newfield_page(self, isinstance):
        pass
    
    def prev_menu(self,isinstance):
        global point_location_track
        global total_entries_in_id

        if point_location_track == 1:
            point_location_track = total_entries_in_id 
        elif point_location_track >= total_entries_in_id + 1 and total_entries_in_id != 0:
            point_location_track = 1
        elif point_location_track == 1 :
            point_location_track == 0
        elif point_location_track > 1:
            point_location_track = point_location_track -1
        
        print(point_location_track)


        D = normal_data(admin)
        if point_location_track != 0:
            if point_location_track > 0 and point_location_track <= total_entries_in_id+1 :
                line = D[f"{point_location_track}"]
                line = line.split("`;;`")
                l1 = line[0]  # l1 is website !
                l2 = line[1]  # l2 is saved login id !
                l3 = line[2]  # l3 is saved login id password !
        self.id_label.text = f"ID ({point_location_track}) :- "
        self.l1_label.text = f"{l1}"
        self.l2_label.text = f"{l2}"
        self.l3_label.text = f"{l3}"

        info = "<---"
        o_s.info_page.update_info(info)
        o_s.screen_manager.current = "Info"
        Clock.schedule_once(self.refresh_page,.3)

    def next_menu(self,isinstance):
        global point_location_track
        global total_entries_in_id

        if point_location_track > total_entries_in_id +1 or point_location_track == total_entries_in_id +1:
            point_location_track = 1
        elif point_location_track < total_entries_in_id :
            point_location_track = point_location_track + 1
        else:
            point_location_track = 1
        
        print(point_location_track,total_entries_in_id)

        D = normal_data(admin)
        if point_location_track != 0:
            if point_location_track > 0 and point_location_track <= total_entries_in_id+1 :
                line = D[f"{point_location_track}"]
                line = line.split("`;;`")
                l1 = line[0]  # l1 is website !
                l2 = line[1]  # l2 is saved login id !
                l3 = line[2]  # l3 is saved login id password !
        self.id_label.text = f"ID ({point_location_track}) :- "
        self.l1_label.text = f"{l1}"
        self.l2_label.text = f"{l2}"
        self.l3_label.text = f"{l3}"

        info = "--->"
        o_s.info_page.update_info(info)
        o_s.screen_manager.current = "Info"
        Clock.schedule_once(self.refresh_page,.3)
    
    def login_button_shift(self, _):
        o_s.connnect_page()
        o_s.screen_manager.current = "Connect"

    def refresh_page(self, _):
        o_s.save_data_show_page()
        o_s.screen_manager.current = "SavedP"

class try_again(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        
        self.add_widget(Label(text= "Re-enter Password:"))
        self.password= TextInput(password = True,text= "" ,multiline=False)
        self.add_widget(self.password)

        self.forget = Button(text="Forget Password")
        self.forget.bind(on_press=self.forget_menu)
        self.add_widget(self.forget)

        self.retry = Button(text="retry")
        self.retry.bind(on_press=self.retry_menu)
        self.add_widget(self.retry)

    def forget_menu(self,isinstance):
        info = f"redirecting to password reset page!"
        o_s.info_page.update_info(info)
        o_s.screen_manager.current = "Info"
        Clock.schedule_once(self.return_reset_menu,1.34)
        
    def retry_menu(self,isinstance):
        
        global admin 
        if admin == 99999:
            info = "not a valid user "
            o_s.info_page.update_info(info)
            o_s.screen_manager.current = "Info"
            Clock.schedule_once(self.return_login,1.3)
        else :
            n = admin_pass_retry(admin,self.password.text)
            if n==2:
                info = "password matched!"
                o_s.info_page.update_info(info)
                o_s.screen_manager.current = "Info"
                Clock.schedule_once(self.pass_matched_right,1.3)

            elif n == 0:
                info = "pass is not right pls retry or else click ok forgot pass !"
                o_s.info_page.update_info(info)
                o_s.screen_manager.current = "Info"
                Clock.schedule_once(self.return_login,1.3)

    def pass_matched_right(self, _):
        o_s.save_data_show_page()
        o_s.screen_manager.current = "SavedP"
    def return_reset_menu(self, _):
        o_s.reset_Pass_Page()
        o_s.screen_manager.current = "resetP"
    def return_login(self, _):
        o_s.try_again_page()
        o_s.screen_manager.current = "tryA"


class reset_password_page(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2 
        
        self.add_widget(Label(text= "Username:"))
        self.adMin= TextInput(text= "" ,multiline=False)
        self.add_widget(self.adMin)

        self.add_widget(Label(text= "Phone No:"))
        self.PhoneNo= TextInput(text= "" ,multiline=False)
        self.add_widget(self.PhoneNo)

        self.add_widget(Label(text= "Password:"))
        self.password= TextInput(password = True,text= "" ,multiline=False)
        self.add_widget(self.password)

        self.add_widget(Label(text= "Re-enter Password:"))
        self.password1= TextInput(password = True,text= "" ,multiline=False)
        self.add_widget(self.password1)

        self.back = Button(text="Back")
        self.back.bind(on_press=self.back_menu)
        self.add_widget(self.back)

        self.save = Button(text="Save Info")
        self.save.bind(on_press=self.save_data)
        self.add_widget(self.save)
    
    def save_data(self,isinstance):
        global admin
        nofinder = self.adMin.text
        admin = search_admin(nofinder)
        repass = self.password1.text
        password = self.password.text
        phoneno = self.PhoneNo.text
        if repass != password:
            info = "Both passwords won't matched !"
            o_s.info_page.update_info(info)
            o_s.screen_manager.current = "Info"
            Clock.schedule_once(self.return_login,1.4)
        else:
        ########################################
            
            if admin == 99999:
                info = "not valid user"
                o_s.info_page.update_info(info)
                o_s.screen_manager.current = "Info"
                Clock.schedule_once(self.return_login,1.4)
            else :
                print("now verifying info with whatsapp no pls wait....")
                n = reset_password(admin,phoneno,password)
                if n == 1:
                    info = "password has been changed"
                    o_s.info_page.update_info(info)
                    o_s.screen_manager.current = "Info"
                    Clock.schedule_once(self.return_login,1.4)
                else :
                    info = "invalid verification no !"
                    o_s.info_page.update_info(info)
                    o_s.screen_manager.current = "Info"
                    Clock.schedule_once(self.return_login,1.4)

        

    def back_menu(self,isinstance):
        info = f"Now going back to login screen."
        o_s.info_page.update_info(info)
        o_s.screen_manager.current = "Info"
        Clock.schedule_once(self.return_login,1)
    

    def return_login(self, _):
        o_s.connnect_page()
        o_s.screen_manager.current = "Connect"

class SignInPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text= "Username:"))
        self.username= TextInput(text= "" ,multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text= "Password:"))
        self.password= TextInput(password = True,text= "" ,multiline=False)
        self.add_widget(self.password)
        
        self.add_widget(Label(text= "Phone No:"))
        self.PhoneNo= TextInput(text= "" ,multiline=False)
        self.add_widget(self.PhoneNo)

        self.back = Button(text="Back")
        self.back.bind(on_press=self.back_menu)
        self.add_widget(self.back)

        self.save = Button(text="Save Info")
        self.save.bind(on_press=self.save_data)
        self.add_widget(self.save)

    # save data and return to login screen ;)

    def save_data(self,isinstance):
        username = self.username.text
        password = self.password.text
        phoneno = self.PhoneNo.text


        n = new_signup(username,password,phoneno)
        if n == 1:
            info = "please use diff username the one choosen allready exixts!"
            o_s.info_page.update_info(info)
            o_s.screen_manager.current = "Info"
            Clock.schedule_once(self.return_login,1.4)
        if n == 2:
            info = f"COngratulation's !  Id has been created sucessfull by this name:-{username}" 
            o_s.info_page.update_info(info)
            o_s.screen_manager.current = "Info"
            Clock.schedule_once(self.return_login,1.4)
       

    def back_menu(self,isinstance):
        info = f"Now going back to login screen."
        o_s.info_page.update_info(info)
        o_s.screen_manager.current = "Info"
        Clock.schedule_once(self.return_login,1)
    

    def return_login(self, _):
        o_s.connnect_page()
        o_s.screen_manager.current = "Connect"
        

# main login screen 
class connectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.rows = 3
        if os.path.isfile("database/cache.txt"):
            with open("database/cache.txt", "r") as f:
                d = f.read().split(",")
                prev_username = d[0]
                prev_pass = d[1]       
        else:
            prev_pass = ""
            prev_username = ""

        self.add_widget(Label(text= "username: "))
        self.username= TextInput(text= prev_username ,multiline=False)
        self.add_widget(self.username)

    
        self.add_widget(Label(text= "password: "))
        self.password= TextInput(password=True,text = prev_pass ,multiline=False)
        self.add_widget(self.password)

        self.signup = Button(text="signup")
        self.signup.bind(on_press=self.signup_button)
        self.add_widget(self.signup)

        self.login = Button(text="login")
        self.login.bind(on_press=self.login_button)
        self.add_widget(self.login)

        
        
        
    # checking login button and check data  
    def login_button(self, isinstance):
        password = self.password.text
        username = self.username.text
        with open("database/cache.txt", "w") as f:
            f.write(f"{username},{password}")
        print("done")

        info = f"Logging in as {username}"
        o_s.info_page.update_info(info)
        o_s.screen_manager.current = "Info"

        Clock.schedule_once(self.test_data, 0.9)
    # connected to ogin button to verify login data in database
    def test_data(self, _):

# login with id and password from the dataBase 
        global admin
        (n , m) = search_id_pass(self.username.text,self.password.text)
        if m == 99999:
            admin =  m
            info = f"Sorry sir no user availabe with {self.username.text}. \nTry Sign-up if your are new here "
            o_s.info_page.update_info(info)
            o_s.screen_manager.current = "Info"
            Clock.schedule_once(self.signup_button,1.2)
        else:
            if n == 1 :
                admin = m
                info = f"Welcome {self.username.text}"
                o_s.info_page.update_info(info)
                o_s.screen_manager.current = "Info"
                Clock.schedule_once(self.main_data_button,1.2)
    
            elif n==2 :
                info = "enter pass and try again"
                admin = m
                o_s.info_page.update_info(info)
                o_s.screen_manager.current = "Info"
                Clock.schedule_once(self.retry_button,1.2)

            elif n == 3:
                info = "wrong pass"
                admin = m
                o_s.info_page.update_info(info)
                o_s.screen_manager.current = "Info"
                Clock.schedule_once(self.retry_button,1.2)

            else:
                info = "some error accured Pls close the window"
                o_s.info_page.update_info(info)
                o_s.screen_manager.current = "Info"
            

#
#
#          retry pass class needed
#         
#   
    def retry_button(self, _):
        o_s.try_again_page()
        o_s.screen_manager.current = "tryA"
    # signup page button       
    def signup_button(self, _):
        o_s.Wrong_Login_info_page()
        o_s.screen_manager.current = "SignIn"
    
    def main_data_button(self, _):
        o_s.save_data_show_page()
        o_s.screen_manager.current = "SavedP"


# transition page button
class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign="center", valign="middle",font_size= 25)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)
    def update_info(self,message):
        self.message.text = message
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width*.9,None)
    
# main loop
class MainApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.connect_page = connectPage()
        screen = Screen(name= "Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)
        self.info_page = InfoPage()
        screen = Screen(name ="Info")
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)
        return self.screen_manager

    def connnect_page(self):
        self.connect_page = connectPage()
        screen = Screen(name= "Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)
        return self.screen_manager

    def Wrong_Login_info_page(self):
        self.signin_page = SignInPage()
        screen = Screen(name="SignIn")
        screen.add_widget(self.signin_page)
        self.screen_manager.add_widget(screen)
        return self.screen_manager
    
    def reset_Pass_Page(self):
        self.reset_page = reset_password_page()
        screen = Screen(name="resetP")
        screen.add_widget(self.reset_page)
        self.screen_manager.add_widget(screen)
        return self.screen_manager
    
    def try_again_page(self):
        self.try_page = try_again()
        screen = Screen(name="tryA")
        screen.add_widget(self.try_page)
        self.screen_manager.add_widget(screen)
        return self.screen_manager

    def save_data_show_page(self):
        self.show_page = saved_user_data()
        screen = Screen(name="SavedP")
        screen.add_widget(self.show_page)
        self.screen_manager.add_widget(screen)
        return self.screen_manager

if __name__ =="__main__":
    o_s = MainApp()
    o_s.run()
