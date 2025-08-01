import mysql.connector          #package connect into mysql into python
from mysql.connector import Error   #it's for error handling
from abc import ABC,abstractmethod      #create abstract class

class contact(ABC):
            @abstractmethod
            def add_contact(self):
                pass
            @abstractmethod
            def view_contact(self):
                pass
            @abstractmethod
            def search_contact(self):
                pass
            @abstractmethod
            def update_contact(self):
                pass
            @abstractmethod
            def delete_contact(self):
                pass


class main(contact):
    def connect_db(self):
     return mysql.connector.connect(        #connecting database into python
        host="localhost",
        database="contact_info",
        user="root",        
        password="Bas@2004"     

    )
        
    def add_contact(self):
        try:
            conn=self.connect_db()      
            cursor=conn.cursor()        #cursor tool for communicate to mysql

            name=input("enter name:")
            mobile=input("enter mobile number:")
            email=input("enter email id:")

            
            query="INSERT INTO CONTACTS(contact_name,mobile_number,email_id) VALUES (%s,%s,%s)"
            cursor.execute(query,(name,mobile,email))       #excute :run the queries    
            conn.commit()       #save the changes in mysql
            print("contact added successfully")
        except mysql.connector.Error as err:
            print("error:",err)
        finally:
            if conn.is_connected():
                cursor.close()      #close connection for avoid sql injection
                conn.close()
            
    def view_contact(self):
            try:
                conn=self.connect_db()
                cursor=conn.cursor()
                cursor.execute("SELECT * FROM contacts")
                rows=cursor.fetchall()      #fetchall : return the all data from database
                if rows:
                    for row in rows:
                        print(f"ID:{row[0]},name: {row[1]}, Mobile number:{row[2]}, Email:{row[3]}")  #checks rows index wise reterive the data
                else:
                    print("No contacts found")
            except mysql.connector.Error as err:
                 print("Error",err)
            
            finally:
                 if conn.is_connected():
                      cursor.close()
                      conn.close()

    def search_contact(self):
            try:
                conn=self.connect_db()
                cursor=conn.cursor()
                name=input("Enter name to search:")
                query="SELECT * FROM contacts WHERE contact_name LIKE %s"
                cursor.execute(query,(f"%{name}%",))        #using wilcard return the data
                rows=cursor.fetchall()
                if rows:
                     for row in rows:
                          print(f"ID:{row[0]},Name:{row[1]},Mobile:{row[2]},email{row[3]}")
                else:
                     print("no matches are found")
                    
            except mysql.connector.Error as err:
                 print("error:",err)

            finally:
                 if conn.is_connected():
                      cursor.close()
                      conn.close()
                     
    def update_contact(self):
            try:
                conn=self.connect_db()
                cursor=conn.cursor()
                contact_id=input("enter contact id to update:")
                new_mobile=input("enter mobile number:")
                new_email=input("enter email id:")
                query="UPDATE contacts SET mobile_number=%s,email_id=%s WHERE id=%s"
                cursor.execute(query,(new_mobile,new_email,contact_id))
                conn.commit()
                if cursor.rowcount:
                     print("contact uploaded")
                else:
                     print("contact id not found")
            except mysql.connector.Error as err:
                 print("Error:",err)
            finally:
                 if conn.is_connected():
                      cursor.close()
                      conn.close()

    def delete_contact(self):
            try:
                conn=self.connect_db()
                cursor=conn.cursor()
                contact_id=input("enter customer id to delete:")
                query="DELETE FROM contacts WHERE id=%s"
                cursor.execute(query,(contact_id,))
                conn.commit()
                if cursor.rowcount:     #it's cursor property :check how many rows is affected
                     print("contact deleted successfully")
                else:
                     print("contact not found")
            except mysql.connector.Error as err:
                 print("Error:",err)
            finally:
                 if conn.is_connected():
                      cursor.close()
                      conn.close()

obj=main()

while True:
    print("\n--contact management--------")
    print("1.ADD CONTACTS")
    print("2.VIEW CONTACT")
    print("3.SEARCH CONTACT")
    print("4.DELETE CONTACT")
    print("5.UPDATE CONTACT")
    print("6.EXIT")        
            
    choice=input("ENTER YOUR CHOICE:")

    if choice=='1':
        obj.add_contact()
    elif choice=='2':
        obj.view_contact()
    elif choice=='3':
        obj.search_contact()
    elif choice=='4':
        obj.delete_contact()
    elif choice=='5':
        obj.update_contact()
    elif choice=='6':
        print("EXIT")
        quit()
    else:
        print("invalid command")
                            



     









