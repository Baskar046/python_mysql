import mysql.connector
from mysql.connector import Error
from abc import ABC,abstractmethod

class to_do(ABC):
    @abstractmethod
    def add_task(self):
        pass

    @abstractmethod
    def view_task(self):
        pass

    @abstractmethod
    def delete_task(self):
        pass

    @abstractmethod
    def update_task(self):
        pass

class main(to_do):
    def connect_db(self):
        return mysql.connector.connect(
            host="localhost",
            database="to_do",
            user="root", 
            password="Bas@2004"

        )
    
    def add_task(self):
        try:
             
            conn=self.connect_db()
            cursor=conn.cursor()

            tasks=input("enter task:")

            query="INSERT INTO task (add_) VALUES(%s)"
            cursor.execute(query,(tasks,))
            conn.commit()
            print("task added")
        except mysql.connector.Error as err:
            print("Error",err)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def view_task(self):
        try:
            conn=self.connect_db()
            cursor=conn.cursor()

            cursor.execute("SELECT * FROM task")
            rows=cursor.fetchall()
            if rows:
                for row in rows:
                    print(f"ID:{row[1]}, task:{row[0]}")
            else:
                print("no tasks are found")

        except mysql.connector.Error as err:
            print("Error",err)

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def delete_task(self):
        try:
            conn=self.connect_db()
            cursor=conn.cursor()

            remove=input("which task you gone remove:")
            query="DELETE  FROM task WHERE add_ LIKE %s"
            cursor.execute(query,(f"%{remove}%",))
            conn.commit()
            if cursor.rowcount:
                print("task is deleted")
            else:
                print("no more matches")
        
        except mysql.connector.Error as err:
            print("Error",err)

        finally :
            if conn.is_connected():
                cursor.close()
                conn.close()

    def update_task(self):
        try:
            conn=self.connect_db()
            cursor=conn.cursor()

            task_id=input("ente id of task to update")
            new_task=input("update the task:")

            query="UPDATE task SET add_=%s WHERE id=%s"
            cursor.execute(query,(new_task,task_id))
            conn.commit()
            if cursor.rowcount:
                print("updated successfully")
            else:
                print("no more matches")

        except mysql.connector.Error as err:
            print("Error",err)

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

obj=main()

while True:
    print("-----TO DO LIST----------")
    print("1.ADD TASK")
    print("2.VIEW TASK")
    print("3.DELETE TASK")
    print("4.UPDATE TASK")
    print("5.EXIT")

    choice=input("enter your choice:")

    if choice=="1":
        obj.add_task()
    elif choice=="2":
        obj.view_task()
    elif choice=="3":
        obj.delete_task()
    elif choice=="4":
        obj.update_task()
    elif choice=="5":
        print("EXIT")
        quit()
    else:
        print("invalid choice")