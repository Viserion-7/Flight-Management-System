import getpass
import warnings
import csv
import time
import pickle
import os

#Login

def login():
    warnings.filterwarnings("ignore")
    print()
    print("\t\t\t\t\tWELCOME TO FLIGHT MANAGEMENT SYSTEM")
    print()
    time.sleep(1)
    print("\t\t\t\t\tPLEASE ENTER YOUR LOGIN DETAILS")
    time.sleep(1)
    for i in range(0,3):
        
        

        UID=input("\n Enter the User Name     : ")
        PWD=getpass.getpass(prompt="\n Enter the User Password : ")

        global f
        filein=open('ADMIN.csv','r')
        reader=csv.reader(filein)
        f=0
        for row in reader:
            if UID==row[0] and PWD==row[1]:
                f=1
                filein.close()
                admins()
        filein=open('MANAGER.csv','r')
        reader=csv.reader(filein)
        for row in reader:
            if UID==row[0] and PWD==row[1]:
                f=2
                filein.close
                managers()
        filein=open('USER.csv','r')
        reader=csv.reader(filein)
        for row in reader:
            if UID==row[0] and PWD==row[1]:
                f=3
                filein.close()
                users()
        
        
        if(f==0):
            time.sleep(1)
            print("\n... Entered User Name  / Password is wrong ...")
            time.sleep(1)
            print(2-i,"attempts remaing")
            if i==2:
                time.sleep(1)
                print("Sorry you have exhausted your attempts")
                time.sleep(1)
                print("Please try again later")
                time.sleep(1)
                print("... Closing Window ...")
                time.sleep(3)
                exit()
            
        else:
            print("\n System Starting.... \a\a\a\a\a\a")
#USER MANAGEMENT

#For Viewing all users
            
def view_all():

    filein=open('ADMIN.csv','r')
    reader=csv.reader(filein)
    time.sleep(1)
    print("Admins are :")
    for row in reader:
        print(row[0],"\t\t",end='')
        print('\n')
        time.sleep(1)
    filein.close()

    filein=open('MANAGER.csv','r')
    reader=csv.reader(filein)
    time.sleep(1)
    print("Managers are :")
    for row in reader:
        print(row[0],"\t\t",end='')
        print('\n')
        time.sleep(1)
    filein.close()

    filein=open('USER.csv','r')
    reader=csv.reader(filein)
    time.sleep(1)
    print("Users are :")
    for row in reader:
        print(row[0],"\t\t",end='')
        print('\n')
        time.sleep(1)
    filein.close()
    

#For adding admin
    
def add_admin():

    try:
        fileout = open("ADMIN.csv", "r")
        fileout.close()
    except IOError:
        time.sleep(1)
        print ("\n File doesn't exist")
        fileout = open("ADMIN.csv", "w",newline='')
        fields=["__ADMINS__","PWD"]
        writer = csv.writer(fileout,delimiter=',')
        writer.writerow(fields)
        fileout.close()
    time.sleep(1)
    uid=input("UID  : ")
    time.sleep(1)
    pwd=input("PWD  : ")
    fileout = open("ADMIN.csv", "a+",newline='')
    writer = csv.writer(fileout,delimiter=',')
    writer.writerow([uid,pwd])
    fileout.close()

#For deleting admin    

def del_admin():
    found=0
    time.sleep(1)
    pname=input("\n Enter the user to be removed: ")
    while True:
        if pname=="admin":
            time.sleep(1)
            print("Cannot delete Main Admin")
            time.sleep(1)
            del_admin()
            break
        else:
            filein=open('ADMIN.csv','r+')
            reader=csv.reader(filein)
            time.sleep(1)
            print("User ID\t\tPassword")
            time.sleep(1)
            for row in reader:
                if pname in row:
                    for col in row:
                        print(col,"\t\t\t",end='')
                        found=1
            print('\n')
            time.sleep(1)
            break            
            filein.close()

    if found==1:
        filein=open('ADMIN.csv','r')
        fileout=open('temp_ADMIN.csv','w',newline='')
        writer = csv.writer(fileout,delimiter=',')
        reader=csv.reader(filein)
        for row in reader:
            if row[0]==pname:
                pass
            else:
                writer.writerow(row)
        filein.close()
        fileout.close()
        os.remove("ADMIN.csv")
        os.rename("temp_ADMIN.csv","ADMIN.csv")
        time.sleep(1)
        print("\n Deletion completed........")
        time.sleep(1)
    else:
        time.sleep(1)
        print("\n Entered Name not found in search : ")
        time.sleep(1)
        del_admin()
    
# For viewing admin

def view_admin():
    filein=open('ADMIN.csv','r')
    reader=csv.reader(filein)
    time.sleep(1)
    for row in reader:
        print(row[0],"\t\t",end='')
        print('\n')
        time.sleep(1)
    filein.close()
    

#For adding manager
    
def add_manager():
    try:
        fileout = open("MANAGER.csv", "r")
        fileout.close()
    except IOError:
        time.sleep(1)
        print ("\n File doesn't exist")
        fileout = open("MANAGER.csv", "w",newline='')
        fields=["___","PWD"]
        writer = csv.writer(fileout,delimiter=',')
        writer.writerow(fields)
        fileout.close()
    time.sleep(1)
    uid=input("UID  : ")
    time.sleep(1)
    pwd=input("PWD  : ")
    fileout = open("MANAGER.csv", "a",newline='')
    writer = csv.writer(fileout,delimiter=',')
    writer.writerow([uid,pwd])
    fileout.close()

#For deleting manager
    
def del_manager():
    found=0
    
    pname=input("\n Enter the user to be removed : ")
    filein=open('MANAGER.csv','r+')
    reader=csv.reader(filein)
    time.sleep(1)
    print("User ID\t\tPassword")
    for row in reader:
        if pname in row:
            for col in row:
                print(col,"\t\t\t",end='')
                found=1
    print('\n')
    time.sleep(1)
    filein.close()
    
    if found==1:
        filein=open('MANAGER.csv','r')
        fileout=open('temp_MANAGER.csv','w',newline='')
        writer = csv.writer(fileout,delimiter=',')
        reader=csv.reader(filein)
        for row in reader:
            if row[0]==pname:
                pass
            else:
                writer.writerow(row)
        filein.close()
        fileout.close()
        os.remove("MANAGER.csv")
        os.rename("temp_MANAGER.csv","MANAGER.csv")
        time.sleep(1)
        print("\n Deletion completed........")
        time.sleep(1)
    else:
        time.sleep(1)
        print("\n Entered Name not found in search : ")
        time.sleep(1)
        del_manager()

#For viewing manager
        
def view_manager():
    filein=open('MANAGER.csv','r')
    reader=csv.reader(filein)
    time.sleep(1)
    for row in reader:
        print(row[0],"\t\t",end='')
        print('\n')
        time.sleep(1)
    filein.close()
    
#For adding user
    
def add_user():

    try:
        fileout = open("USER.csv", "r")
        fileout.close()
    except IOError:
        time.sleep(1)
        print ("\n File doesn't exist")
        fileout = open("USER.csv", "w",newline='')
        fields=["__USERS__","PWD"]
        writer = csv.writer(fileout,delimiter=',')
        writer.writerow(fields)
        fileout.close()
    time.sleep(1)
    uid=input("UID  : ")
    time.sleep(1)
    pwd=input("PWD  : ")
    fileout = open("USER.csv", "a",newline='')
    writer = csv.writer(fileout,delimiter=',')
    writer.writerow([uid,pwd])
    fileout.close()
    
#For deleting user
    
def del_user():
    
    found=0
    
    pname=input("\n Enter the user to be removed : ")
    filein=open('USER.csv','r+')
    reader=csv.reader(filein)
    time.sleep(1)
    print("User ID\t\tPassword")
    for row in reader:
        if pname in row:
            for col in row:
                print(col,"\t\t\t",end='')
                found=1
    print('\n')
    time.sleep(1)
    filein.close()
    
    if found==1:
        filein=open('USER.csv','r')
        fileout=open('temp_USER.csv','w',newline='')
        writer = csv.writer(fileout,delimiter=',')
        reader=csv.reader(filein)
        for row in reader:
            if row[0]==pname:
                pass
            else:
                writer.writerow(row)
        filein.close()
        fileout.close()
        os.remove("USER.csv")
        os.rename("temp_USER.csv","USER.csv")
        time.sleep(1)
        print("\n Deletion completed........")
        time.sleep(1)
    else:
        time.sleep(1)
        print("\n Entered Name not found in search : ")
        time.sleep(1)
        del_user()

#For viewing user
        
def view_user():
    filein=open('USER.csv','r')
    reader=csv.reader(filein)
    time.sleep(1)
    for row in reader:
        print(row[0],"\t\t",end='')
        print('\n')
        time.sleep(1)
    filein.close()

#For viewing flights
    
def view_flights():
    time.sleep(1)
    print("SCHEDULED FLIGHTS", end='\n\n')
    time.sleep(1)
    filein=open('scheduled.csv','r')
    reader=csv.reader(filein)
    for row in reader:
        print("%20s %20s %20s %20s %20s %20s" %(row[0],row[1],row[2],row[3],row[4],row[5]))
        print('\n')
        time.sleep(1)
    filein.close()
    time.sleep(1)
    print("CANCELLED FLIGHTS", end='\n\n')
    time.sleep(1)
    filein=open('cancelled.csv','r')
    reader=csv.reader(filein)
    for row in reader:
        print("%20s %20s %20s %20s" %(row[0],row[1],row[2],row[3]))
        print('\n')
        time.sleep(1)
    filein.close()
    
#For adding flights
    
def add_flights():
    fileout=open('scheduled.csv','a',newline='')
    writer = csv.writer(fileout,delimiter=',')
    time.sleep(1)
    fno=input("Enter flight no:- ")
    time.sleep(1)
    eta=input("Enter time of arrival:- ")
    time.sleep(1)
    dest=input("Enter destination:- ")
    time.sleep(1)
    stat=input("Enter status:- ")
    time.sleep(1)
    seats=input("Enter the number of seats:- ")
    time.sleep(1)
    cst=input("Enter the cost:- ")
    time.sleep(1)
    writer.writerow([fno,eta,dest,stat,seats,cst])
    fileout.close()
    time.sleep(1)

#For cancelling flights
    
def cancel_flights():
    found=0
    time.sleep(1)
    fno=input("Enter the number of the flight to be cancelled:- ")
    filein=open('scheduled.csv','r+')
    reader=csv.reader(filein)
    for row in reader:
        if fno in row:
            for col in row:
                found=1
    filein.close()
    
    if(found==0):
        time.sleep(1)
        print('flight not found')
        cancel_flights()
        time.sleep(1)
    else:
        fileout=open('cancelled.csv','a')
        filein=open('scheduled.csv','r')
        writer=csv.writer(fileout,delimiter=',')
        reader=csv.reader(filein)
        for row in reader:
                if row[0]==fno:
                    l=[row[0],row[1],row[2],"cancelled"]
                    writer.writerow(l)
        fileout.close()
        filein.close()
        filein=open('scheduled.csv','r')
        fileout=open('temp_scheduled.csv','w',newline='')
        writer = csv.writer(fileout,delimiter=',')
        reader=csv.reader(filein)
        for row in reader:
                if row==[]:
                    pass
                elif row[0]==fno:
                    pass
                else:
                    writer.writerow(row)
        filein.close()
        fileout.close()
        os.remove("scheduled.csv")
        os.rename("temp_scheduled.csv","scheduled.csv")
        time.sleep(1)
        print("Flight cancelled successfully")
        time.sleep(1)
    
def sort_helper_by_cost(x):
    return int(x[-1])

def sort_helper_by_arrival(x):
    if x[3] == 'Scheduled':
        return 2
    return 1

#For sorting flights by destination

def sort_dest_admins():
    found=0
    time.sleep(1)
    dest=input('Enter the destination: ')
    while True:
        time.sleep(1)
        type = input("""
To sort flights by cost                  press 1
To sort flights by status of arrival     press 2
To return to control panel               press 0
 """)
        if type.isnumeric():
            type = int(type)
            if type==1 or type==2 or type==0:
                break
            else:
                time.sleep(1)
                print("Invalid input. Please Try Again")
        else:
            time.sleep(1)
            print("Invalid input. Please try again")

    if type == 1:
        filein=open('scheduled.csv','r')
        reader=csv.reader(filein)
        temp_list = []
        for row in reader:
            if row[2]==dest:
                temp_list.append(list(row))
                found += 1
        if found==0:
            time.sleep(1)
            print("Currently there are No Flights for",dest)
        else:
            temp_list.sort(key=sort_helper_by_cost)
            time.sleep(1)

            print("%20s %20s %20s %20s %20s %20s" %("Flight No","ETA","Destination","Status","Seats Available","Cost"))
            for row in temp_list:
                time.sleep(1)
                print("%20s %20s %20s %20s %20s %20s" %(row[0],row[1],row[2],row[3],row[4],row[5]))
        filein.close()
        
    elif type == 2:
        filein=open('scheduled.csv','r')
        reader=csv.reader(filein)
        temp_list = []
        for row in reader:
            if row[2]==dest:
                temp_list.append(list(row))
                found += 1
        if found==0:
            time.sleep(1)
            print("Currently there are no flights for",dest)
        else:
            temp_list.sort(key=sort_helper_by_arrival)
            temp_list = temp_list[::-1]
            time.sleep(1)
            print("%20s %20s %20s %20s %20s %20s" %("Flight No","ETA","Destination","Status","Seats Available","Cost"))
            for row in temp_list:
                time.sleep(1)
                print("%20s %20s %20s %20s %20s %20s" %(row[0],row[1],row[2],row[3],row[4],row[5]))
        filein.close()
     

    elif type==0:
        admins()
    
    
def admins():
    global time
    q=1
    while q==1:
        try:
            time.sleep(1)
            time.sleep(1)
            option=int(input('''
To view Flight details           press 1
To add a new flight              press 2
To cancel a flight               press 3
To manage users                  press 4
To search a Flight               press 5
Press any other key to exit
'''))
        except:
            time.sleep(1)
            print('... Thank you...')
            time.sleep(1)
            print('...Have a nice day...')
            time.sleep(1)
            print('... Closing Window ...')

            time.sleep(2)
            exit()
        if option==1:
            try:
                view_flights()
                    
            except:
                admins()
        elif option==2:
            add_flights()
            admins()
        elif option==3:
            cancel_flights()
            admins()
        elif option==4:
            try:
                time.sleep(1)
                user_option=int(input('''
To view users                    press 1
To add new user                  press 2
To delete existing user          press 3
To return to control panel       press 0
Press any other key to exit
'''))
            except:
                time.sleep(1)
                print('... Thank you...')
                time.sleep(1)
                print('...Have a nice day...')
                time.sleep(1)
                print('... Closing Window ...')

                time.sleep(2)
                exit()
            if user_option==1:
                try:
                    time.sleep(1)
                    view_option=int(input('''
To view admins                   press 1
To view managers                 press 2
To view users                    press 3
To view all users                press 4
To return to control panel       press 0
Press any other key to exit
'''))
                except:
                    time.sleep(1)
                    print('... Thank you...')
                    time.sleep(1)
                    print('...Have a nice day...')
                    time.sleep(1)
                    print('... Closing Window ...')

                    time.sleep(2)
                    exit()
                if view_option==1:
                    view_admin()
                elif view_option==2:
                    view_manager()
                elif view_option==3:
                    view_user()
                elif view_option==4:
                    view_all()
                elif view_option==0:
                    admins()
                else:
                    time.sleep(1)
                    print('... Thank you...')
                    time.sleep(1)
                    print('...Have a nice day...')
                    time.sleep(1)
                    print('... Closing Window ...')

                    time.sleep(2)
                    exit()
            elif user_option==2:
                try:
                    time.sleep(1)
                    add_user_option=int(input('''
To add admin                     press 1
To add manager                   press 2
To add user                      press 3
To return to control panel       press 0
Press any other key to exit
'''))
                except:
                    time.sleep(1)
                    print('... Thank you...')
                    time.sleep(1)
                    print('...Have a nice day...')
                    time.sleep(1)
                    print('... Closing Window ...')

                    time.sleep(2)
                    exit()
                    time.sleep(3)
                    exit()
                if add_user_option==1:
                    add_admin()
                    admins()
                elif add_user_option==2:
                    add_manager()
                    admins()
                elif add_user_option==3:
                    add_user()
                    admins()
                elif add_user_option==0:
                    admins()
                else:
                    time.sleep(1)
                    print('... Thank you...')
                    time.sleep(1)
                    print('...Have a nice day...')
                    time.sleep(1)
                    print('... Closing Window ...')

                    time.sleep(2)
                    exit()
                        
            elif user_option==3:
                try:
                    time.sleep(1)
                    add_user_option=int(input('''
To remove admin                     press 1
To remove manager                   press 2
To remove user                      press 3
To return to control panel          press 0
Press any other key to exit
'''))
                except:
                    time.sleep(1)
                    print('... Thank you...')
                    time.sleep(1)
                    print('...Have a nice day...')
                    time.sleep(1)
                    print('... Closing Window ...')

                    time.sleep(2)
                    exit()
                                    
                if add_user_option==1:
                    del_admin()
                    admins()
                elif add_user_option==2:
                    del_manager()
                    admins()
                elif add_user_option==3:
                    del_user()
                    admins()
                elif add_user_option==0:
                    admins()
                else:
                    time.sleep(1)
                    print('... Thank you...')
                    time.sleep(1)
                    print('...Have a nice day...')
                    time.sleep(1)
                    print('... Closing Window ...')

                    time.sleep(2)
                    exit()
                        
            elif user_option==0:
                admins()
            else:
                    time.sleep(1)
                    print('... Thank you...')
                    time.sleep(1)
                    print('...Have a nice day...')
                    time.sleep(1)
                    print('... Closing Window ...')

                    time.sleep(2)
                    exit()
        elif option==5:
            sort_dest_admins()
            admins()
                
        else:
            time.sleep(1)
            print('... Thank you...')
            time.sleep(1)
            print('...Have a nice day...')
            time.sleep(1)
            print('... Closing Window ...')

            time.sleep(2)
            exit()

def sort_dest_managers():
    found=0
    time.sleep(1)
    dest=input('Enter the destination: ')
    while True:
        time.sleep()
        type = input("""
To sort flights by cost                  press 1
To sort flights by status of arrival     press 2
To return to control panel               press 0
Press any other key to exit
 """)
        if type.isnumeric():
            type = int(type)
            if type in (0,2):
                break
            else:
                time.sleep(1)
                print("Invalid input. Please Try Again")
        else:
            time.sleep(1)
            print("Invalid input. Please try again")

    if type == 1:
        filein=open('scheduled.csv','r')
        reader=csv.reader(filein)
        temp_list = []
        for row in reader:
            if row[2]==dest:
                temp_list.append(list(row))
                found += 1
        if found==0:
            time.sleep(1)
            print("Currently there are No Flights for",dest)
        else:
            temp_list.sort(key=sort_helper_by_cost)
            time.sleep(1)

            print("%20s %20s %20s %20s %20s %20s" %("Flight No","Time","Destination","Status","Seats Available","Cost"))
            for row in temp_list:
                time.sleep(1)
                print("%20s %20s %20s %20s %20s %20s" %(row[0],row[1],row[2],row[3],row[4],row[5]))
        filein.close()
        
    elif type == 2:
        filein=open('scheduled.csv','r')
        reader=csv.reader(filein)
        temp_list = []
        for row in reader:
            if row[2]==dest:
                temp_list.append(list(row))
                found += 1
        if found==0:
            time.sleep(1)
            print("currently there are no flights for",dest)
        else:
            temp_list.sort(key=sort_helper_by_arrival)
            temp_list = temp_list[::-1]
            time.sleep(1)
            print("%20s %20s %20s %20s %20s %20s" %("Flight No","Time","Destination","Status","Seats Available","Cost"))
            for row in temp_list:
                time.sleep(1)
                print("%20s %20s %20s %20s %20s %20s" %(row[0],row[1],row[2],row[3],row[4],row[5]))
        filein.close()
     

    elif type==0:
        managers()
        
def managers():
    global time
    q=1
    while q==1:
        try:
            time.sleep(1)
            time.sleep(1)
            option=int(input('''
To view Flight details           press 1
To add a new flight              press 2
To cancel a flight               press 3
To manage users                  press 4
To search a Flight               press 5
Press any other key to exit
'''))
        except:
            time.sleep(1)
            print('... Thank you...')
            time.sleep(1)
            print('...Have a nice day...')
            time.sleep(1)
            print('... Closing Window ...')

            time.sleep(2)
            exit()
        if option==1:
            try:
                view_flights()
                    
            except:
                managers()
        elif option==2:
            add_flights()
            managers()
        elif option==3:
            cancel_flights()
            managers()
        elif option==4:
            try:
                time.sleep(1)
                user_option=int(input('''
To view users                    press 1
To add new user                  press 2
To delete existing user          press 3
To return to control panel       press 0
Press any other key to exit
'''))
            except:
                time.sleep(1)
                print('... Thank you...')
                time.sleep(1)
                print('...Have a nice day...')
                time.sleep(1)
                print('... Closing Window ...')

                time.sleep(2)
                exit()
            if user_option==1:
                try:
                    time.sleep(1)
                    view_option=int(input('''
To view admins                   press 1
To view managers                 press 2
To view users                    press 3
To view all users                press 4
To return to control panel       press 0
Press any other key to exit
'''))
                except:
                    time.sleep(1)
                    print('... Thank you...')
                    time.sleep(1)
                    print('...Have a nice day...')
                    time.sleep(1)
                    print('... Closing Window ...')

                    time.sleep(2)
                    exit()
                if view_option==1:
                    view_admin()
                elif view_option==2:
                    view_manager()
                elif view_option==3:
                    view_user()
                elif view_option==4:
                    view_all()
                elif view_option==0:
                    managers()
                else:
                    time.sleep(1)
                    print('... Thank you...')
                    time.sleep(1)
                    print('...Have a nice day...')
                    time.sleep(1)
                    print('... Closing Window ...')

                    time.sleep(2)
                    exit()
            elif user_option==2:
                try:
                    time.sleep(1)
                    add_user_option=int(input('''
To add manager                   press 1
To add user                      press 2
To return to control panel       press 0
Press any other key to exit
'''))
                except:
                    time.sleep(1)
                    print('... Thank you...')
                    time.sleep(1)
                    print('...Have a nice day...')
                    time.sleep(1)
                    print('... Closing Window ...')

                    time.sleep(2)
                    exit()
                if add_user_option==1:
                    add_manager()
                    managers()
                elif add_user_option==2:
                    add_user()
                    managers()
                elif add_user_option==0:
                    managers()
                else:
                    time.sleep(1)
                    print('... Thank you...')
                    time.sleep(1)
                    print('...Have a nice day...')
                    time.sleep(1)
                    print('... Closing Window ...')

                    time.sleep(2)
                    exit()
                        
            elif user_option==3:
                try:
                    time.sleep(1)
                    add_user_option=int(input('''
To remove manager                   press 1
To remove user                      press 2
To return to control panel          press 0
Press any other key to exit
'''))
                except:
                    time.sleep(1)
                    print('... Thank you...')
                    time.sleep(1)
                    print('...Have a nice day...')
                    time.sleep(1)
                    print('... Closing Window ...')

                    time.sleep(2)
                    exit()  
                if add_user_option==1:
                    del_manager()
                    managers()
                elif add_user_option==2:
                    del_user()
                    managers()
                elif add_user_option==0:
                    managers()
                else:
                    time.sleep(1)
                    print('... Thank you...')
                    time.sleep(1)
                    print('...Have a nice day...')
                    time.sleep(1)
                    print('... Closing Window ...')

                    time.sleep(2)
                    exit()
                        
            elif user_option==0:
                managers()
            else:
                time.sleep(1)
                print('... Thank you...')
                time.sleep(1)
                print('...Have a nice day...')
                time.sleep(1)
                print('... Closing Window ...')

                time.sleep(2)
                exit()
        elif option==5:
            sort_dest_managers()
            managers()
        else:
            time.sleep(1)
            print('... Thank you...')
            time.sleep(1)
            print('...Have a nice day...')
            time.sleep(1)
            print('... Closing Window ...')

            time.sleep(2)
            exit()

def sort_dest_users():
    found=0
    time.sleep(1)
    dest=input('Enter the destination: ')
    while True:
        time.sleep()
        type = input("""
To sort flights by cost                  press 1
To sort flights by status of arrival     press 2
To return to control panel               press 0
Press any other key to exit
 """)
        if type.isnumeric():
            type = int(type)
            if type in (0,2):
                break
            else:
                time.sleep(1)
                print("Invalid input. Please Try Again")
        else:
            time.sleep(1)
            print("Invalid input. Please try again")

    if type == 1:
        filein=open('scheduled.csv','r')
        reader=csv.reader(filein)
        temp_list = []
        for row in reader:
            if row[2]==dest:
                temp_list.append(list(row))
                found += 1
        if found==0:
            time.sleep(1)
            print("Currently there are No Flights for",dest)
        else:
            temp_list.sort(key=sort_helper_by_cost)
            time.sleep(1)

            print("%20s %20s %20s %20s %20s %20s" %("Flight No","Time","Destination","Status","Seats Available","Cost"))
            for row in temp_list:
                time.sleep(1)
                print("%20s %20s %20s %20s %20s %20s" %(row[0],row[1],row[2],row[3],row[4],row[5]))
        filein.close()
        
    elif type == 2:
        filein=open('scheduled.csv','r')
        reader=csv.reader(filein)
        temp_list = []
        for row in reader:
            if row[2]==dest:
                temp_list.append(list(row))
                found += 1
        if found==0:
            time.sleep(1)
            print("currently there are no flights for",dest)
        else:
            temp_list.sort(key=sort_helper_by_arrival)
            temp_list = temp_list[::-1]
            time.sleep(1)
            print("%20s %20s %20s %20s %20s %20s" %("Flight No","Time","Destination","Status","Seats Available","Cost"))
            for row in temp_list:
                time.sleep(1)
                print("%20s %20s %20s %20s %20s %20s" %(row[0],row[1],row[2],row[3],row[4],row[5]))
        filein.close()
     

    elif type==0:
        users()

def users():
    global time
    q=1
    while q==1:
        try:
            time.sleep(1)
            time.sleep(1)
            option=int(input('''
To view Flight details           press 1
To search a Flight               press 2
Press any other key to exit
'''))
        except:
            time.sleep(1)
            print('... Thank you...')
            time.sleep(1)
            print('...Have a nice day...')
            time.sleep(1)
            print('... Closing Window ...')

            time.sleep(2)
            exit()
        if option==1:
            try:
                view_flights()
                    
            except:
                users()
        elif option==2:
            sort_dest_users()
            users()
        else:
            time.sleep(1)
            print('... Thank you...')
            time.sleep(1)
            print('...Have a nice day...')
            time.sleep(1)
            print('... Closing Window ...')

            time.sleep(2)
            exit()
                
login()