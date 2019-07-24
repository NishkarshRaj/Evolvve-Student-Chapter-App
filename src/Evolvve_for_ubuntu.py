''' Importing necessary modules and packages '''
import sqlite3
from random import randint
from os import system,name
from time import sleep

''' Creation of Connection Object in sqllite for Ubuntu '''
con = sqlite3.connect("pro.db") #Connection IP
cur = con.cursor()

''' Function for clearing Python Shell '''
def clear():
    if name=='posix':
        _=system('clear') 
''' Class that uses multiple important functions that are not related in true sense of student chapter '''

''' User Defined Exception Raiser '''
class exception_raiser(Exception):
        def __init__(self,msg):
            self.msg = msg
        def print_exception(self):
            print(self.msg)

class extra:
    ''' Function to generate Student Chapter ID '''
    def studentID(self,stu_id):
        s = int(stu_id)
        flag = 0
        random_value = randint(10000,2000+s)
        try:
            file = open("chapterid.txt","r",1)
        except:
            print("The File cannot be opened!!!!")
            exit()
        for lines in file:
            lines = lines.strip()
            x = int(lines)
            if x == random_value:
                flag = 1
            elif x == None:
                break
            else:
                continue
        file.close()
        if flag == 1:
            studentID(s)
        elif flag == 0:
            try:
                file1 = open("chapterid.txt","a",1)
                string = str(random_value)+"\n"
                file1.write(string)
                file1.close()
            except:
                print("File error due to writing in elif block!!!")
            else:
                return random_value
    ''' Loading Function '''
    def loading(self):
        for i in range (0,31):
            if i <10:
                print("Connecting To the Database")
            elif i>=10 and i<21:
                if i==10:
                    sleep(3)
                    clear()
                else:
                    print("Inserting Details in The Database")
            else:
                if i==21:
                    sleep(3)
                    clear()
                else:
                    print("Generating Student Chapted ID")
    ''' Function for fee calculation '''
    def fee(self,name):
        sleep(3)
        clear()
        print("Hello",name,"To the Fee insertion page")
        x = name
        print("Following Packages are available!!!")
        print("1) Premium Membership for 500 Rupees - 1 Year")
        print("2) Gold Membership for 1000 Ruppes - 2 Years")
        print("3) Platinum Membership for 2000 Rupees - 4 Years + Tech Magazines")
        inp = int(raw_input("Enter your Choice [1/2/3] :"))
        if inp == 1:
            print("Returning the Value entered")
            return 500
        elif inp == 2:
            print("Returning the Value entered")
            return 1000
        elif inp == 3:
            print("Returning the Value entered")
            return 2000
        else:
            print("Wrong Choice!! Try Again")
            self.fee(x)
    ''' Password Checker '''
    def checkpass(self,password):
        count_small = 0
        count_capital = 0
        count_number = 0
        count_special = 0
        ''' Password must contain 1 small 1 capital letter 1 digit and 1 special character '''
        for ch in password:
            if ord(ch) in range(97,123):
                count_small += 1 #Ascii for small letter 97-122
            elif ord(ch) in range(65,91):
                count_capital += 1 #Ascii for capital letter 65-90
            elif ord(ch) in range(48,58):
                count_number += 1 #Ascii for number 48-57
            else:
                count_special += 1
        #print(count_small)
        #print(count_capital)
        #print(count_special)
        #print(count_number)
        if count_small >= 1 and count_capital >= 1 and count_special >= 1 and count_number >= 1:
            return 1 #If 1 == True Correct pass
        else:
            return 0 #If 2 == False incorrect pass
    ''' About Evolvve Function using File Handling '''
    def about(self):
        sleep(3)
        clear()
        file = open("About.txt","r",1)
        print(file.read())
        ans = raw_input("Print y/Y to redirect to homepage else Application will close")
        if ans == 'y' or ans == 'Y':
            homepage()
        else:
            quit()

class login_pages:
    ''' Forgot password code '''
    ''' When Username exists in Membersignup page but user does not remember his/her password '''
    def forgotpass(self,sap_id):
        sleep(3)
        clear()
        print("Enter your Registration Number for verification!!!")
        reg_num = raw_input("Enter your registration number: ")
        cur.execute("select registration_num from membersignup where sapid = :sap",{"sap":sap_id,})
        d_rn = cur.fetchall()
        data_rn = list(d_rn[0])
        database_rn = str(data_rn[0])
        if database_rn == None:
            print("\nRegistration Number does not exist in our Database!!! Access Denied!!!")
            quit()
        elif database_rn == reg_num:
            print("\n\nDatabase Result Match Success!!!")
            cur.execute("select password from membersignup where sapid = :sap",{"sap":sap_id})
            passwo = cur.fetchall()
            passw = list(passwo[0])
            password = str(passw[0])
            print("Your Password is =>",password)
            ans1 = raw_input("\nEnter y/Y to redirect to login page! Else application redirects to homepage!!! \n")
            if ans1 == 'y' or ans1 == 'Y':
                print("\nRedirecting to login page.....")
                self.login()
            else:
                print("\nRedirecting to homepage....")
                homepage()
        else:
            print("\nWrong Registration Number Entered!!! Retry")
            inp1=raw_input("\nEnter y/Y to retry : ")
            if inp1=='y' or inp1=='Y':
                self.forgotpass(sap_id)
            else:
                print("Redirecting to homepage!!")
                homepage()
    ''' Login Page '''
    def login(self):
        try:
            sleep(3)
            clear()
            print("\n\n")
            print("\t\t\t\t\t\t\tEvolvve: Student Chapter Application\n\n\n")
            print("\t\t\t\t\t\t\t\tLogin Page!!!\n\n")
            sapid = raw_input("Enter SAP ID: ")
            cur.execute("select password from membersignup where sapid = :sap",{"sap":sapid,})
            var1 = cur.fetchall()
            if not var1:
                raise exception_raiser("Sap ID is not registered!!  Please Sign Up")
                
            else:
                pass_db=var1
                pass_data = list(pass_db[0])
                pass_database = str(pass_data[0])
            if pass_database == None:
                print("User does not exist in Database!!!") #Case 1) User does not exists
                homepage()
            else:
                password = raw_input("Enter Password: ")
                if password == pass_database:
                    m123 = menu_pages()
                    m123.menu()
                elif pass_database==None:
                    print("Cannot Access password from the database!!!")
                else:
                    print("\n\n")
                    print("Incorrect Password! ")
                    print("1) Retry Login")
                    print("2) Forgot Password?")
                    inp = int(input("Enter your choice [1/2]: "))
                    if inp == 1:
                        self.login() #Case 3: User Exists but types incorrect password!!!
                    elif inp == 2:
                        self.forgotpass(sapid) #Case 4: Users exists but needs to ask password
                    else:
                        print("\nAccess Denied! Too much faults!! Redirecting to homepage!")
                        homepage()
        except sqlite3.DatabaseError as e:
            print("Database Error:",e)
            self.login()
        except exception_raiser as e1:
            e1.print_exception()
            print("Runtime error encountered!!!")
            self.login()
    
    ''' Login Page '''
    def adminlogin(self):
        try:
            sleep(3)
            clear()
            print("\n\n")
            print("\t\t\t\t\t\t\tEvolvve: Student Chapter Application\n\n\n")
            print("\t\t\t\t\t\t\t\tAdmin Login Page\n\n")
            sapid = raw_input("Enter SAP ID: ")
            pass_db=cur.execute("select password from membersignup where sapid = :sap",{"sap":sapid,})
            pass_db = cur.fetchall()
            pass_data=list(pass_db[0])
            pass_database=str(pass_data[0])
            if pass_database == None:
                print("User does not exist in Database!!!") #Case 1) User does not exists
                homepage()
            else:
                password = raw_input("Enter Password: ")
                if password == pass_database:
                    print("Successful") # Case 2: Correct SAP id and password: Grant Access!!! will create menu function later!!!
                    #Different code from normal login()
                    ad_pass = "Evolvve@1"
                    admin_pass = raw_input("Enter Admin Password: ")
                    if ad_pass == admin_pass:
                        m321 = menu_pages()
                        m321.admin_menu()
                    else:
                        print("Wrong Admin Password!!")
                        adminlogin()
                elif pass_database==None:
                    print("Cannot Access password from the database!!!")
                else:
                    print("Incorrect Password! ")
                    print("1) Retry Login")
                    print("2) Forgot Password?")
                    inp = int(input("Enter your choice [1/2]: "))
                    if inp == 1:
                        login() #Case 3: User Exists but types incorrect password!!!
                    elif inp == 2:
                        self.forgotpass(sapid) #Case 4: Users exists but needs to ask password
                    else:
                        print("Access Denied! Too much faults!! Redirecting to homepage!")
                        homepage()
        except sqlite3.DatabaseError as e:
            print("Database Error:",e)
        except:
            print("Runtime error encountered!!!")

class menu_pages:
    ''' Menu Page for Normal Login '''
    def menu(self):
        sleep(3)
        clear()
        print("\t\t\t\t\t\t\tMain Menu Page\n\n")
        print("1) Upcoming Evolvve Events")
        print("2) Recent News and Trends")
        print("3) Give Feedback for Evolvve")
        print("4) Change Password for login")
        print("5) Visit Homepage\n\n")
        inp = int(raw_input("Enter your choice: "))
        if inp == 1:
            print("\n\n\n")
            print("Upcoming Evolvve Events!!!\n") #Till Now neither table nor files written!!!
            #cur.execute("select * from events")
            #for row in cur:
                #print(row)
            file3 = open("Event_list.txt","r",1)
            print(file3.read())
            print("\nEnter Any event name you want to know more about!!!")
            print("Press 1) To redirect to menu")
            inp1 = raw_input("Enter your choice: ")
            file3.close()
            if inp1 == '1':
                self.menu()
            else:
                try:
                    print("\n\n")
                    filename = "Event_" + inp1 + ".txt" #Event files should be stored as Event_filename.txt
                    file = open(filename,"r",1)
                except:
                    print("File does not exists")
                else:
                    print(file.read())
                finally:
                    sleep(4)
                    self.menu()
                filename = "Event_" + inp1 + ".txt"
                file5 = open("filename","r",1)
                if file5.read() == None:
                    print("File does not exists")
                else:
                    print(file5.read())
                    self.menu()
        elif inp == 2:
            print("\n\n\n")
            print("Recent News and Trends!!!") #No tables required!! Files already written!!!
            file_recent = open("recent_trend.txt","r",1)
            print(file_recent.read())
            file_recent.close()
            file_trend = open("flag_trend.txt","r",1)
            flag_trend = int(file_trend.read())
            file_trend.close()
            inp2 = int(raw_input("Enter your choice in integer: "))
            if inp2 >= 1 and inp2 <= flag_trend:
                try:
                    file7 = str(inp2) + ".txt"
                    file = open(file7,"r",1)
                except:
                    print("Sorry! Unable to open file!!!")
                else:
                    print(file.read())
                finally:
                    k=raw_input("\n\n Press enter to redirect to menu : ")
                    k=32
                    if k==32:
                        self.menu()
            else:
                print(" Wrong Choice!!! Redirecting to Main Menu!!!")
                self.menu()
        elif inp == 3:
            print("Writing Feedback!!!")
            filename = raw_input("Enter file name you want to keep for your feedback: ")
            file1 = "Support_" + filename + ".txt" #Support files must be stored as Support_filename.txt
            file = open(file1,"w",1)
            input1 = raw_input("Enter Feedback:\n")
            file.write(input1)
            file.close()
            print("Feedback successfully sent!!!")
        elif inp == 4:
            try:
                sapid = raw_input("Enter SAP-ID: ")
                if len(sapid)!=9:
                    raise exception_raiser("SAP ID is always of length 9 characters. Please Retry..")
                for k in sapid:
                    if ord(k) >= 48 and ord(k) <=57:
                        pass
                    else:
                        raise exception_raiser("Invalid Character in SAP ID")
                pass_current = raw_input("Enter Correct Password: ")
                cur.execute("select password from membersignup where sapid = :s",{"s":sapid})
                p = cur.fetchall()
                p1 = list(p[0])
                p2 = str(p1[0])
                if p2 == None:
                    raise exception_raiser("Either member is not enrolled or password does not exist")
                if p2 == pass_current:
                    pass_new = raw_input("Enter new password: ")
                    flag_41 = 0
                    e41 = extra()
                    flag_41 = e41.checkpass(pass_new)
                    if flag_41 == 0:
                        raise exception_raiser("Incorrect Format of new password! Atleast 1 Capital 1 small alphabet 1 digit and 1 special character needed")
                    pass_new1 = raw_input("Re-enter new password: ")
                    if pass_new == pass_new1:
                        cur.execute("update membersignup set password = :p where sapid = :s",{"p":pass_new,"s":sapid})
                        con.commit()
                        print("\n Password Updated Successfully!!!!!")
                    else:
                        print("Passwords do not match!!! Retry...\nRedirecting to main menu")
                        self.menu()
                else:
                    print("Wrong Password Entered!! Redirecting to main menu!!!")
                    self.menu()
            except sqlite3.DatabaseError as e:
                print("Database Error encountered",e)
                self.menu()
            except exception_raiser as e:
                e.print_exception()
                self.menu()
            except:
                print("Runtime Error encountered!!!")
                self.menu()
            else:
                print("Password Changed Successfully")
            finally:
                self.menu()
        elif inp == 5:
                homepage()
        else:
            print("Wrong Choice! Please Try again!")
            self.menu()
        
    ''' Menu Page for Admin Login '''
    def admin_menu(self):
        sleep(3)
        clear()
        print("1) Create new Event")
        print("2) Create new file for recent news and trends!")
        print("3) Read Feedbacks from Users")
        print("4) Register student/groups for upcoming events")
        print("5) Edit Core Committe Details and Members")
        print("6) Visit Homepage\n\n")
        inp = int(raw_input("Enter your choice: "))
        if inp == 1:
            print("Create new event!!!")
            name = raw_input("Enter Event Name for new entry :")
            file4 = open("Event_list.txt","a",1)
            w = "\n" + name
            file4.write(w)
            file4.close()
            content = raw_input("Enter Description of the event!!\n")
            filename = "Event_" + name + ".txt"
            file5 = open("filename","w",1)
            file5.write(content)
            file5.close()
            judge = raw_input("Enter name of the judge :")
            money = input("Enter Prize Money :")
            comm = raw_input("Enter name of the committee who is conducting the event : ")
            cur.execute("insert into events values (:name,:judge,:money,:comm)",{"name":name,"judge":judge,"money":money,"comm":comm})
            con.commit()
            print("\n\n\nNew Event Created!!!!!!!!!")
            self.admin_menu()
        elif inp == 2:
            print("Create new file for recent news and trends!!!")
            file_trend = open("flag_trend.txt","r",1)
            flag_trend = file_trend.read()
            file_trend.close()
            print("Current number of files present:",flag_trend)
            f = int(flag_trend)
            f = f + 1
            flag_trend = str(f) + ".txt"
            file_new = open(flag_trend,"w",1)
            content_name = raw_input("Enter name of the topic: ")
            f1 = open("recent_trend.txt","a",1)
            f2 = "\n" + str(f) + ") " + content_name
            f1.write(f2)
            inp = raw_input("Enter Content\n")
            file_new.write(inp)
            file_new.close()
            file_t = open("flag_trend.txt","w",1)
            file_t.write(str(f))
            self.admin_menu()
            print("\n\nTrend Created!!!")
        elif inp == 3:
            import os
            print("Available Support Files are:\n")
            path1 = raw_input("Enter path of current folder in Your pc to extract all Support files")
            for file in os.listdir(path1):#Path has to be inserted here Dont end with \ else unicode problem
                "Path for Lakshika PC is:/home/lakshika/Desktop/Python_Programs"
                if file.endswith(".txt") and file.startswith("Support_"):
                    print(os.path.join(file))
            filename = raw_input("\nEnter the file name of the above list which you want to read\n")
            f = open(filename,'r')
            content = f.read()
            print("\n\nThe Feedback in the file is ")
            print(content)
            self.admin_menu()
        elif inp == 5:
            print("1) Add new members to Core Committee")
            print("2) Update old data")
            inp = int(raw_input("Enter your choice: "))
            if inp == 1:
                print("Following Committee and their members are already enlisted")
                cur.execute("select * from committee_members")
                for row in cur:
                    print(row)
                print("Following Positions can be written")
                cur.execute("select * from positions")
                for row in cur:
                    print(row)
                comm_name = raw_input("Enter Committee in which member is to be entered: ")
                member_name = raw_input("Enter name of the Club Member who is to be entered: ")
                pos = raw_input("Enter position in which member is to be entered: ")
                try:
                    cur.execute("insert into committee_members values(:c,:m,:p)",{"c":comm_name,"m":member_name,"p":pos})
                    con.commit()
                except sqlite3.DatabaseError as e:
                    print("Database Error encountered:",e)
                except:
                    print("Runtime Error encountered")
                finally:
                    self.admin_menu()
            elif inp == 2:
                try:
                    input1 = raw_input("Enter SQL Statement to carry out the updation/deletion!!!")
                    cur.execute(input1)
                    con.commit()
                except sqlite3.DatabaseError as e:
                    print("Database Error encountered:",e)
                except:
                    print("Runtime Error Encountered")
                else:
                    print("Work Updated Successfully")
                finally:
                    self.admin_menu()
            else:
                print("Wrong Choice! Redirecting to Main Menu")
                self.admin_menu()
        elif inp == 4:
            print("Registering participants for the Events!!!")
            print("Following Events are available!!!")
            cur.execute("select * from events")
            for row in cur:
                print(row)
            e_name = raw_input("Enter name of event: ")
            g_name = raw_input("Enter group name :")
            fees = float(raw_input("Enter fees for the group!!!"))
            cur.execute("insert into participation values (:e,:g,:f)",{"e":e_name,"g":g_name,"f":fees})
            print("Now Enter details of the members of the group",g_name)
            inp3 = int(raw_input("Enter Number of participants [1,2,3,4]"))
            if inp3 >=1 and inp3 <=4:
                for i in range(0,inp3):
                    m_name = raw_input("Enter name of the member: ")
                    m_sap = raw_input("Enter sapid of the member: ")
                    cur.execute("insert into participation_members values (:e,:n,:s)",{"e":g_name,"n":m_name,"s":m_sap})
                    con.commit()
                print("\n Registration Done!!!!!")
                self.admin_menu()
            else:
                print("Invalid number of participants entered!")
                print("Restart from beginning! Redirecting to Admin menu")
                self.admin_menu()
        elif inp == 6:
            homepage()
        else:
            print("Wrong Choice! Please Try Again...")
            self.admin_menu()


''' Code For Signup Page '''	
class sign_up:
    def signup(self):
        try:
            sleep(8)
            clear()
            print("\t\t\t\t\t\t\t\t\t\tSignUp For Evolvve!\n\n\n")
            name = raw_input("Student Name : ")
            sap_id = raw_input("SAP Id : ")
            if len(sap_id)!=9:
                raise exception_raiser("Sap Id is always of length 9 characters. Please Retry....")
            else:
                for k in sap_id:
                    if ord(k)>=48 and ord(k)<=57:
                        pass
                    else:
                        raise exception_raiser("Invalid Character in Sap Id")

            password = raw_input("Password : ")
            '''check password function is called '''
            e1 = extra() #Object of class extra!!!
            check1 = e1.checkpass(password)
            if check1 == 0:
                raise exception_raiser("Password must contain 1 small letter, 1 capital letter, 1 special character and 1 digit") #User Defined Class
            ''' lets continue forward '''
            roll = raw_input("Registration No. : ")
            branch = raw_input("Branch : ")
            year = int(raw_input("Year Of Study [1/2/3/4] : "))
            gender = raw_input("Gender [M/F/O] : ")
            sleep(3)
            clear()
            e1.loading()
            clear()
            stuchapID = e1.studentID(sap_id)
            fees = e1.fee(name)
            stuchapID = str(stuchapID)
            fees = int(fees)
            print("Fees has been inserted")
            #Inserting Values to the Class User
            print("Creating object of user class")
            user1 = user(name,sap_id,password,roll,branch,year,gender,stuchapID,fees)
            user_flag_1 = 0
            user_flag_2 = 0
            print("Calling user name checker function")
            user_flag_1 = user1.name_checker(name)
            print("Calling user sap id function")
            user_flag_2 = user1.sap_id_checker(sap_id)
            if user_flag_1 == 1:
                raise exception_raiser("Incorrect expression in Name")
            elif user_flag_2 == 1:
                raise exeption_raiser("Incorrect Expression in SAP ID")
            #Inserting Values to the DataBase
            cur.execute("insert into membersignup values(:name,:sapid,:pass,:roll,:stuid,:branch,:year,:gender,:memberfee)",{"name":name,"sapid":sap_id,"pass":password,"roll":roll,"stuid":stuchapID,"branch":branch,"year":year,"gender":gender,"memberfee":fees})
        except sqlite3.DatabaseError as e:
            print("Database Error encountered",e)
            self.signup()
        except exception_raiser as e:
            e.print_exception()
            self.signup()
        except:
            print("Runtime Error encountered")
            self.signup()
        else:
            con.commit()
            sleep(7)
            clear()
            print("SignUp is successfully completed!!!")
        finally:
            homepage()

''' Class generic for users (either casual or admin) '''
class user:
    def __init__(self,name,sap_id,password,roll,branch,year,gender,stuchapID,fees):
        self.name = name
        self.sap_id = sap_id
        self.password = password
        self.roll = roll
        self.branch = branch
        self.year = year
        self.gender = gender
        self.stuchapID = stuchapID
        self.fees = fees
    def name_checker(self,name):
        count_1= 0
        for k in self.name:
            if ord(k)>=65 and ord(k)<=90 or ord(k)>=97 and ord(k)<=122 or ord(k)==32:
                continue
            else:
                count_1 += 1
        if count_1 == 0:
            return 0
        else:
            return 1
    def sap_id_checker(self,sap_id):
        count_nondigit = 0
        for k in self.sap_id:
            if ord(k)>=48 and ord(k)<=57:
                continue
            else:
                count_nondigit += 1
        if count_nondigit == 0:
            return 0
        else:
            return 1
        
''' Homepage of the Application '''
def homepage():
    sleep(4)
    clear()
    print("\t\t\t\t\t\t\t\t\tEvolvve: Student Chapter Application\n\n\n")
    print("\t\t\t1) Login")
    print("\t\t\t2) Admin Login")
    print("\t\t\t3) New User? -> Sign Up")
    print("\t\t\t4) About Evolvve!")
    print("\t\t\t5) Exit Application")
    inp = int(raw_input("Enter your choice: "))
    log_123 = login_pages() #Object of class Login Pages
    print("\n\n\n")
    if inp == 1:
        log_123.login()
    if inp == 2:
        log_123.adminlogin()
    if inp == 3:
        s = sign_up() #Creating object of class sign up
        s.signup()
    if inp == 4:
        e = extra() #e is the object of extra class which contains functions that are used multiple times in the project but are not related to body of chapter
        e.about()
    if inp == 5:
        quit()

''' Main code... Execution starts from here!!!'''
homepage()
con.close()
quit()


