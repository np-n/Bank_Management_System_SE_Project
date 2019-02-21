from tkinter import *
#from PIL import Image,ImageTk
import time
from tkinter import ttk
from tkinter.font import Font
from tkinter.ttk import Combobox
from tkinter.ttk import Scrollbar
import mysql.connector

class statement:
    def __init__(self,master):
        self.master=master
        # left canvas to get register
        self.canvas1= Canvas(master, height=220,width=1380, bg="oldlace")
        self.canvas1.place(x=0,y=0)

        # Right Canvas to show the statements
        self.canvas4 = Canvas(master, height=10,width=1380, bg="thistle2")
        self.canvas4.place(x=-1,y=220)
        self.canvas5 = Canvas(master, height=500,width=1380, bg="thistle2")
        self.canvas5.place(x=-1,y=230)
        self.welcome = Label(master, text="Enter customer details to display statements",font=("Verdana Bold",18), bg="oldlace", fg="blue2").place(x=80, y=10)

        # left entry form
        self.name = Label(master, text="name",font=("Verdana Bold",12), bg="oldlace").place(x=100, y=80)
        self.name_entry = ttk.Entry(master,width=25)
        self.name_entry.place(x=300, y=80)
        self.account_num = Label(master, text="account number",font=("Verdana Bold",12), bg="oldlace").place(x=100, y=120)
        self.account_entry = ttk.Entry(master,width=25)
        self.account_entry.bind("<Return>",self.print_statement)
        self.account_entry.place(x=300, y=120)
        self.request_button = Button(master, text="request statements",fg="white",bg="blue2",font=("Verdana Bold",12),command=self.print_statement)
        self.request_button.place(x=400, y=150)

    def print_statement(self,event=""):
        self.canvas2 = Canvas(self.master, height=10,width=1380, bg="thistle2")
        self.canvas2.place(x=-1,y=220)
        self.canvas3 = Canvas(self.master, height=500,width=1380, bg="thistle2")
        self.canvas3.place(x=-1,y=230)
        # connecting to statement database in order to fetch
        statement_table = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="yvd_database",
        )
        statement = statement_table.cursor()
        user_name = self.name_entry.get()
        user_account=self.account_entry.get()
        user_var1=str(user_name)
        user_var2=str(user_account)
        user_var1=user_var1.lower()
        store_user = ""
        for var in user_var1:
            if (var.isspace() == True):
                store_user = store_user + "_"
            else:
                store_user = store_user + var

        store_user=store_user+"_"+user_var2
        print(store_user)
        # select_table="""select * from %s"""
        # statement.execute(select_table,(store_user,))
        statement.execute("SELECT * FROM %s" % store_user)
        result = statement.fetchall()
        row_count = statement.rowcount
        count = 1
        while (count <= row_count):
            for value in result:
                data = value
                date_and_time = data[0]
                operation = data[1]
                amount = data[2]
                performed_by = data[3]
                transferred_to = data[4]
                branch = data[5]
                issued_by = data[6]
                transjection_id = data[7]
                self.canvas2.create_line(1, 0, 0, 10, width=4, fill="black")
                self.canvas3.create_line(1, 0, 1, 25, width=4, fill="black")
                self.canvas2.create_line(165, 0, 165, 10, width=1, fill="black")
                self.canvas3.create_line(165, 0, 165, 25, width=1, fill="black")

                self.canvas2.create_line(331, 0, 331, 10, width=1, fill="black")
                self.canvas3.create_line(331, 0, 331, 25, width=1, fill="black")

                self.canvas2.create_line(497, 0, 497, 10, width=1, fill="black")
                self.canvas3.create_line(497, 0, 497, 25, width=1, fill="black")

                self.canvas2.create_line(663, 0, 663, 10, width=1, fill="black")
                self.canvas3.create_line(663, 0, 663, 25, width=1, fill="black")

                self.canvas2.create_line(829, 0, 829, 10, width=1, fill="black")
                self.canvas3.create_line(829, 0, 829, 25, width=1, fill="black")

                self.canvas2.create_line(995, 0,995, 10, width=1, fill="black")
                self.canvas3.create_line(995, 0,995, 25, width=1, fill="black")

                self.canvas2.create_line(1, 1, 13260, 1, width=4, fill="black")

                self.canvas2.create_line(1160, 0, 1160, 10, width=1, fill="black")
                self.canvas3.create_line(1161, 1, 1161, 25, width=1, fill="black")

                self.canvas2.create_line(1325, 0, 1325, 10, width=1, fill="black")
                self.canvas3.create_line(1325, 1, 1325, 25, width=1, fill="black")
                self.canvas2 = Canvas(self.master, height=10, width=100, bg="white")
                self.canvas2.place(x=1326, y=220)


                e2 = ttk.Entry(self.canvas3)
                e2.insert(6, date_and_time)
                e2.grid(row=count + 6, column=1, ipadx=20)
                e3 = ttk.Entry(self.canvas3)
                e3.insert(6, operation)
                e3.grid(row=count + 6, column=2, ipadx=20)
                e4 = ttk.Entry(self.canvas3)
                e4.insert(6, amount)
                e4.grid(row=count + 6, column=3, ipadx=20)
                e5 = ttk.Entry(self.canvas3)
                e5.insert(6, performed_by)
                e5.grid(row=count + 6, column=4, ipadx=20)
                e6 = ttk.Entry(self.canvas3)
                e6.insert(6, transferred_to)
                e6.grid(row=count + 6, column=5, ipadx=20)
                e7 = ttk.Entry(self.canvas3)
                e7.insert(6, branch)
                e7.grid(row=count + 6, column=6, ipadx=20)
                e8 = ttk.Entry(self.canvas3)
                e8.insert(6, issued_by)
                e8.grid(row=count + 6, column=7, ipadx=20)
                e9 = ttk.Entry(self.canvas3)
                e9.insert(6,transjection_id)
                e9.grid(row=count + 6, column=8, ipadx=20)
                count = count + 1
        #data = Label(self.canvas3, text="Date and time", fg="blue2", bg="thistle2", font=("Arial Bold", 12)).grid(row=1, column=1)
        data = Label(self.canvas3, text="Date and time", fg="blue2", bg="thistle2", font=("Arial Bold", 12)).grid(row=1, column=1)
        data = Label(self.canvas3, text="Operation", fg="blue2", bg="thistle2", font=("Arial Bold", 12)).grid(row=1, column=2)
        data = Label(self.canvas3, text="Amount", fg="blue2", bg="thistle2", font=("Arial Bold", 12)).grid(row=1, column=3)
        data = Label(self.canvas3, text="Performed by", fg="blue2", bg="thistle2", font=("Arial Bold", 12)).grid(row=1, column=4)
        data = Label(self.canvas3, text="Transferred To", fg="blue2", bg="thistle2", font=("Arial Bold", 12)).grid(row=1, column=5)
        data = Label(self.canvas3, text="Branch", fg="blue2", bg="thistle2", font=("Arial Bold", 12)).grid(row=1, column=6)
        data = Label(self.canvas3, text="Issued by", fg="blue2", bg="thistle2", font=("Arial Bold", 12)).grid(row=1, column=7)
        data = Label(self.canvas3, text="Transjection Id", fg="blue2", bg="thistle2", font=("Arial Bold", 12)).grid(row=1, column=8)


def statement_main(event=""):
    window_statement=Tk()
    window_statement.title("Youth Voice Nepal -Transjection history Management System")
    # to get full window
    width = window_statement.winfo_screenwidth()
    height = window_statement.winfo_screenheight()
    window_statement.geometry("%dx%d" % (width, height))
    # window.resizable(False,False)  # used for not resizable window
    # or window.resizable(0,0)
    window_statement.resizable(True, True)
    # icon on top
    # why this not work---------------------------------------------------------------------------------------------------------------
    #icon_image = Image("photo", file="1.ico")
    #window_statement.call('wm', 'iconphoto', window_statement._w, icon_image)
    perform_statement=statement(window_statement)
    window_statement.mainloop()




class transfer:
    def __init__(self,master):
        self.master=master
        # left canvas to get register
        self.canvas1= Canvas(master, width=700, height=730, bg="oldlace")
        self.canvas1.create_line(695,5,695,730,fill="green",width=30)
        self.canvas1.pack(fill=Y, side=LEFT, anchor=W)
        # Right Canvas to show the registered record
        self.canvas2 = Canvas(master, width=660, height=730, bg="thistle2")
        self.canvas2.pack(fill=Y, side=RIGHT)
        # left entry form for sender details
        self.label1 = Label(master, text="SENDER",font=("Verdana Bold", 18), bg="oldlace", fg="blue2").place(x=50, y=10)
        self.name1 = Label(master, text="name",font=("Verdana Bold",14),bg="oldlace").place(x=40, y=60)
        self.name_entry1 = ttk.Entry(master,width=25)
        self.name_entry1.place(x=230, y=60)
        self.account_number1 = Label(master, text="account number",font=("Verdana Bold",14),bg="oldlace").place(x=40, y=100)
        self.account_number_entry1= ttk.Entry(master,width=25)
        # binding sender entry
        self.account_number_entry1.bind("<Return>",self.get_sender_details)
        self.account_number_entry1.place(x=230, y=100)
        # request information button
        self.request__sender_details = Button(master, text="request information", fg="white", bg="blue2",font=("Verdana Bold",14),command=self.get_sender_details)
        self.request__sender_details.bind("<Return>",self.get_sender_details)
        self.request__sender_details.place(x=200, y=150)
        # right entry form for receiver
        self.label2 = Label(master, text="RECEIVER",font=("Verdana Bold", 18), bg="thistle2", fg="blue2").place(x=750, y=10)
        self.name2 = Label(master, text="name",font=("Verdana Bold",14),bg="thistle2").place(x=770, y=60)
        self.name_entry2 = ttk.Entry(master,width=25)
        self.name_entry2.place(x=960, y=60)
        self.account_number2 = Label(master, text="account number",font=("Verdana Bold",14),bg="thistle2").place(x=770, y=100)
        self.account_number_entry2 = ttk.Entry(master,width=25)
        # binding receiver entry
        self.account_number_entry2.bind("<Return>",self.get_receiver_details)
        self.account_number_entry2.place(x=960, y=100)
        self.request_receiver_details = Button(master, text="request information", fg="white", bg="blue2",font=("Verdana Bold",14),command=self.get_receiver_details)
        self.request_receiver_details.bind("<Return>",self.get_receiver_details)
        self.request_receiver_details.place(x=950, y=150)


    def get_sender_details(self,event=""):
        global ac_holder_name1
        global account_num1
        ac_holder_name1=self.name_entry1.get().title()
        account_num1=self.account_number_entry1.get()
        self.get_sender= mysql.connector.connect(
            user="root",
            host="localhost",
            passwd="",
            database="yvd_database",
        )
        self.request_sender = self.get_sender.cursor()
        sql_query_sender = """select * from customer_data where ac_holder_name = %s and account_num = %s """
        query_var_sender= (ac_holder_name1, account_num1,)
        self.request_sender.execute(sql_query_sender, query_var_sender)
        sender_data = self.request_sender.fetchall()
        for result in sender_data:
            self.name3 = result[0]
            self.mob_no3 = result[6]
            self.ac_type3 = result[7]
            self.id_no3 = result[8]
            self.occp3 = result[10]
            self.per_add3 = result[11]
            self.img_dir3 = result[14]
            self.ac_no3 = result[15]
            self.cr_amt3=result[13]
            self.br3 = result[18]
        self.request_sender.close()
        self.get_sender.close()
        global current_amt_sender
        current_amt_sender=int(self.cr_amt3)
        # request info deisplay section for sender
        # using self.master as window
        self.Name = Label(self.master, text="Name : ", font=("Verdana Bold", 12), bg="oldlace").place(x=30, y=220)
        self.Name_display = Label(self.master, text=self.name3, bg="oldlace").place(x=200, y=220)
        self.Account_No = Label(self.master, text="Account number :", font=("Verdana Bold", 12), bg="oldlace").place(x=30, y=260)
        self.Account_no_display = Label(self.master, text=self.ac_no3, bg="oldlace").place(x=200, y=260)
        self.Account_type = Label(self.master, text="Account type :", font=("Verdana Bold", 12), bg="oldlace").place(x=30, y=300)
        self.Account_type_display = Label(self.master, text=self.ac_type3, bg="oldlace").place(x=200, y=300)
        self.Mobile_No = Label(self.master, text="Mobile number:", font=("Verdana Bold", 12), bg="oldlace").place(x=30, y=340)
        self.Mobile_No_display = Label(self.master, text=self.mob_no3, bg="oldlace").place(x=200, y=340)
        self.Id_No = Label(self.master, text="ID Number:", font=("Verdana Bold", 12), bg="oldlace").place(x=30, y=380)
        self.Id_No_display = Label(self.master, text=self.id_no3, bg="oldlace").place(x=200, y=380)
        self.Address_label = Label(self.master, text="address", font=("Verdana Bold", 12), bg="oldlace").place(x=30,y=420)
        self.Address_display = Label(self.master, text=self.per_add3, bg="oldlace").place(x=200, y=420)
        self.Avl_balance = Label(self.master, text="Current amount :", font=("Verdana Bold", 12), bg="oldlace").place(x=30, y=460)
        self.Avl_balance_display = Label(self.master, text=self.cr_amt3, bg="oldlace").place(x=200, y=460)
        self.branch = Label(self.master, text="Branch ", font=("Verdana Bold", 12), bg="oldlace").place(x=30, y=500)
        self.branch_display = Label(self.master, text=self.br3, bg="oldlace").place(x=200, y=500)
        # canvas for receiver photo
        self.rectangle1 = self.canvas1.create_rectangle(470, 140, 670, 340, fill="mint cream")
        self.transfor_message = Label(self.master, text="Amount to send", font=("Verdana Bold", 14), bg="oldlace").place(x=30,y=550)
        self.amount_transfer = ttk.Entry(self.master, width=25)
        self.amount_transfer.bind("<Return>",self.sender_receiver_details_after_transfer)
        self.amount_transfer.place(x=260, y=550)
        # transfer amount  button
        # why error here----------------------------------------------------------------------------------------------------------------
        # self.transfer_button_import = PhotoImage(file='withdraw button1.png')
        # self.transfer_button = Button(self.master, image=self.withdraw_button_import, highlightthickness=0, bd=0,command=self.get_display)
        # self.transfer_button.place(x=370, y=640)
        self.withdraw_button = Button(self.master, text="perform transfer  ", bg="blue2", fg="white",font=("Verdana Bold",14),command=self.sender_receiver_details_after_transfer)
        self.withdraw_button.bind("<Return>",self.sender_receiver_details_after_transfer)
        self.withdraw_button.place(x=370, y=590)



    def get_receiver_details(self,event=""):
        global ac_holder_name2
        global account_num2
        ac_holder_name2=self.name_entry2.get().title()
        account_num2=self.account_number_entry2.get()
        self.get_receiver= mysql.connector.connect(
            user="root",
            host="localhost",
            passwd="",
            database="yvd_database",
        )
        self.request_receiver = self.get_receiver.cursor()
        sql_query_receiver= """select * from customer_data where ac_holder_name = %s and account_num = %s """
        query_var_receiver= (ac_holder_name2, account_num2,)
        self.request_receiver.execute(sql_query_receiver, query_var_receiver)
        receiver_data = self.request_receiver.fetchall()
        for value in receiver_data:
            self.name4 = value[0]
            self.mob_no4 = value[6]
            self.ac_type4 =value[7]
            self.id_no4 = value[8]
            self.occp4 =value[10]
            self.per_add4 =value[11]
            self.img_dir4 = value[14]
            self.ac_no4 = value[15]
            self.cr_amt4= value[13]
            self.br4 = value[18]
        self.request_receiver.close()
        self.get_receiver.close()
        global curent_amt_receiver
        curent_amt_receiver =int(self.cr_amt4)
        # using self.master as window
        self.Name4 = Label(self.master, text="Name  ", font=("Verdana Bold", 12), bg="thistle2").place(x=750, y=220)
        self.Name_display4 = Label(self.master, text=self.name4, bg="thistle2").place(x=900, y=220)
        self.Account_No4 = Label(self.master, text="Account number ", font=("Verdana Bold", 12), bg="thistle2").place(x=750, y=260)
        self.Account_No_display4= Label(self.master, text=self.ac_no4, bg="thistle2").place(x=900, y=260)
        self.Account_type4 = Label(self.master, text="Account type :", font=("Verdana Bold", 12), bg="thistle2").place(x=750, y=300)
        self.Account_type_display4 = Label(self.master, text=self.ac_type4, bg="thistle2").place(x=900, y=300)
        self.Mobile_No4 = Label(self.master, text="Mobile number:", font=("Verdana Bold", 12), bg="thistle2").place(x=750, y=340)
        self.Mobile_No_display4 = Label(self.master, text=self.mob_no4, bg="thistle2").place(x=900, y=340)
        self.Id_No24= Label(self.master, text="ID Number:", font=("Verdana Bold", 12),bg="thistle2").place(x=750, y=380)
        self.Id_No_display4 = Label(self.master, text=self.id_no4, bg="thistle2").place(x=900, y=380)
        self.Address_label = Label(self.master, text="address", font=("Verdana Bold", 12), bg="thistle2").place(x=750,y=420)
        self.Address_display = Label(self.master, text=self.per_add4, bg="thistle2").place(x=900, y=420)
        self.Avl_balance4 = Label(self.master, text="Current amount :", font=("Verdana Bold", 12),bg="thistle2").place(x=750, y=460)
        self.Avl_balance_display4 = Label(self.master, text=self.cr_amt4, bg="thistle2").place(x=900, y=460)
        self.branch4 = Label(self.master, text="Branch ", font=("Verdana Bold", 12),bg="thistle2").place(x=750, y=500)
        self.branch_display4 = Label(self.master, text=self.br4, bg="thistle2").place(x=900, y=500)
        # canvas for photo
        self.rectangle2 = self.canvas2.create_rectangle(450, 200, 650, 400, fill="mint cream")


    def sender_receiver_details_after_transfer(self,event=""):
        global send_amt
        send_amt= self.amount_transfer.get()
        send_amt=int(send_amt)
        cur_amt_sender=str(current_amt_sender)
        if(send_amt>current_amt_sender):
             self.withdraw_response =Label(self.master, text="you can't withdraw it because current amount is only  "+cur_amt_sender+"/-", fg="red", bg="oldlace",font=("Verdana Bold", 12)).place(x=80,y=650)
        elif(send_amt==0):
            self.withdraw_response = Label(self.master, text="you can't enter '0' , Please enter valid amount",fg="red", bg="oldlace", font=("Verdana Bold", 12)).place(x=80, y=650)
        elif (send_amt< 500 and send_amt>0):
            self.withdraw_response = Label(self.master, text="you can't deposit less than '500'",fg="red", bg="oldlace", font=("Verdana Bold", 12)).place(x=80, y=650)
        else:
            amt_after_transfer = current_amt_sender - send_amt
            # sender amount after transfer
            # for sender display after transfer operation
            self.get_sender_receiver = mysql.connector.connect(
                user="root",
                host="localhost",
                passwd="",
                database="yvd_database",
            )
            self.request_sender_receiver = self.get_sender_receiver.cursor()
            sql_query_sender1 = """update customer_data set current_amount=%s where ac_holder_name = %s and account_num = %s """
            query_var_sender1 = (amt_after_transfer, ac_holder_name1, account_num1,)
            self.request_sender_receiver.execute(sql_query_sender1, query_var_sender1)
            self.get_sender_receiver.commit()

            sql_query_sender2 = """select * from customer_data where ac_holder_name = %s and account_num = %s """
            query_var_sender2 = (ac_holder_name1, account_num1,)
            self.request_sender_receiver.execute(sql_query_sender2, query_var_sender2)
            sender_data2 = self.request_sender_receiver.fetchall()
            for result in sender_data2:
                self.cr_amt5 = result[13]
            current_amount_for_sender = self.cr_amt5

            # inserting transfer data on statement user
            customer_name = str(ac_holder_name1.lower())
            customer_acc = str(account_num1)
            store_customer = ""
            for var in customer_name:
                if (var.isspace() == True):
                    store_customer = store_customer + "_"
                else:
                    store_customer = store_customer + var

            store_customer = store_customer + "_" + customer_acc
            print(store_customer)
            opn = "Transfer"
            issued = "--------"
            ts = str(ac_holder_name2) + "(" + str(account_num2) + ")"
            per_by = ac_holder_name1
            cr_time = time.asctime()
            edit_insert_statement = " INSERT INTO " + store_customer + " ( date_and_time,operation,amount,performed_by,transfer_to,branch,issued_by) VALUES (%s,%s,%s,%s,%s,%s,%s) "
            record_statement2 = (cr_time, opn, send_amt, per_by, ts, self.br4, issued)
            self.request_sender_receiver.execute(edit_insert_statement, record_statement2)
            self.get_sender_receiver.commit()

            # for receiver calculation and display
            amount_after_receive = curent_amt_receiver + send_amt
            sql_query_receiver1 = """update customer_data set current_amount=%s where ac_holder_name = %s and account_num = %s """
            query_var_receiver1 = (amount_after_receive, ac_holder_name2, account_num2,)
            self.request_sender_receiver.execute(sql_query_receiver1, query_var_receiver1)
            self.get_sender_receiver.commit()

            sql_query_receiver2 = """select * from customer_data where ac_holder_name = %s and account_num = %s """
            query_var_receiver2 = (ac_holder_name2, account_num2,)
            self.request_sender_receiver.execute(sql_query_receiver2, query_var_receiver2)
            receiver_data2 = self.request_sender_receiver.fetchall()
            for value in receiver_data2:
                self.cr_amt6 = value[13]
            current_amount_for_receiver = self.cr_amt6
            # need to use roolback() to cancel all transjection if any error occurs-----------------------------------------------------------------------------------------------
            # displaying imformation after transfer
            self.operation_completion_message = Label(self.master, text="Transfer Succesfull",
                                                      font=("Verdana Bold", 12), fg="green", bg="oldlace").place(x=30,
                                                                                                                 y=600)
            self.Avl_balance_sender = Label(self.master, text="Current Amount after transfer",
                                            font=("Verdana Bold", 14), bg="oldlace").place(x=30, y=640)
            self.Avl_balance_sender_display = Label(self.master, text=current_amount_for_sender, bg="oldlace").place(
                x=400, y=640)
            # receiver amount after receive
            self.Avl_balance_receiver = Label(self.master, text="Current Amount after receive",
                                              font=("Verdana Bold", 14), bg="thistle2").place(x=750, y=550)
            self.Avl_balance_receiver_display = Label(self.master, text=current_amount_for_receiver,
                                                      bg="thistle2").place(x=1100, y=550)

            # inserting receiving data on statement user
            customer_name2 = str(ac_holder_name2.lower())
            customer_acc2 = str(account_num2)
            store_customer2 = ""
            for var in customer_name2:
                if (var.isspace() == True):
                    store_customer2 = store_customer2 + "_"
                else:
                    store_customer2 = store_customer2 + var
            store_customer2 = store_customer2 + "_" + customer_acc2
            print(store_customer2)
            opn2 = "Receive amt"
            issued2 = "--------"
            rs2 = str(ac_holder_name1) + "(" + str(account_num1) + ")"
            per_by2 = ac_holder_name1
            cr_time2 = time.asctime()
            edit_insert_statement = " INSERT INTO " + store_customer2 + " ( date_and_time,operation,amount,performed_by,transfer_to,branch,issued_by) VALUES (%s,%s,%s,%s,%s,%s,%s) "
            record_statement2 = (cr_time2, opn2, send_amt, per_by2, rs2, self.br3, issued2)
            self.request_sender_receiver.execute(edit_insert_statement, record_statement2)
            self.get_sender_receiver.commit()
            self.request_sender_receiver.close()
            self.get_sender_receiver.close()



def transfer_main(event=""):
    window_transfer=Tk()
    window_transfer.title("Youth Voice Nepal -Transfer Control System")
    # to get full window
    width = window_transfer.winfo_screenwidth()
    height = window_transfer.winfo_screenheight()
    window_transfer.geometry("%dx%d" % (width, height))
    # window.resizable(False,False)  # used for not resizable window
    # or window.resizable(0,0)
    window_transfer.resizable(True, True)
    # icon on top
    # why this not work-----------------------------------------------------------------------------------------------------------------------------------------
    #icon_image = Image("photo", file="1.ico")
    #window_transfer.call('wm', 'iconphoto', window_transfer._w, icon_image)
    frame = Frame(window_transfer)
    frame.pack()
    perform_transger=transfer(window_transfer)
    window_transfer.mainloop()


class edit:
    def __init__(self, master):
        # Very important fact to pass in the function inside the class
        self.master=master
        # left canvas to get register
        self.canvas1= Canvas(master, width=730, height=730, bg="oldlace")
        self.canvas1.pack(fill=Y, side=LEFT, anchor=W)
        # Right Canvas to show the registered record
        self.canvas2 = Canvas(master, width=730, height=730,bg="thistle2")
        self.canvas2.pack(fill=Y, side=RIGHT)
        self.welcome = Label(master, text="Enter customer details to Edit info ",font=("Verdana Bold",18), bg="oldlace", fg="blue2").place(x=10, y=10)
        # left entry form
        self.name = Label(master, text="name",font=("Webdings Bold",14), bg="oldlace").place(x=50, y=80)
        self.name_entry = ttk.Entry(master,width=25)
        self.name_entry.place(x=200, y=80)
        self.account_num = Label(master, text="account number",font=("Webdings Bold",14), bg="oldlace").place(x=50, y=120)
        self.account_number_entry = ttk.Entry(master,width=25)
        # entry binding
        self.account_number_entry.bind("<Return>",self.get_request_editinfo)
        self.account_number_entry.place(x=200, y=120)
        # Request information  button
        # error ?-------------------------------------------------------------------------------------------------------------------------------------
        #self.request_button_import = PhotoImage(file='request info2.png')
        #self.request_button = Button(master, image=self.request_button_import, highlightthickness=0, bd=0,command=self.get_request)
        #self.request_button.place(x=140, y=180)
        self.request_editinfo_button = Button(master, text="request information",fg="white",bg="blue2",font=("Verdana Bold",12),command=self.get_request_editinfo)
        # button binding
        self.request_editinfo_button.bind("<Return>",self.get_request_editinfo)
        self.request_editinfo_button.place(x=140, y=180)


    # to display available balance
    def get_request_editinfo(self,event=""):
        global holder_name
        global account_num
        global mobile_num
        global id_num
        global avl_bal
        global deposit_amount

        holder_name=self.name_entry.get().title()
        account_num=self.account_number_entry.get()
        self.account_number1=account_num
        self.edit_account = mysql.connector.connect(
            user="root",
            host="localhost",
            passwd="",
            database="yvd_database",
        )
        self.edit_account_insert = self.edit_account.cursor()
        sql_query = """select * from customer_data where ac_holder_name like %s and account_num like %s """
        query_var = (holder_name, account_num,)
        self.edit_account_insert.execute(sql_query, query_var)
        customer_data = self.edit_account_insert.fetchall()
        for result in customer_data:
            self.name = result[0]
            self.father_name=result[1]
            self.mother_name=result[2]
            self.dob=result[4]
            self.mob_no = result[6]
            self.ac_type=result[7]
            self.id_no = result[8]
            self.id_type = result[9]
            self.occp= result[10]
            self.per_add= result[11]
            self.tem_add = result[12]
            self.img_dir=result[14]
            self.ac_no = result[15]
            self.br = result[18]

            self.edit_account_insert.close()
            self.edit_account.close()

        # using self.master as window
        self.Name = Label(self.master, text="Name : ",font=("Webdings Bold",14), bg="oldlace").place(x=50, y=250)
        self.Name_display = ttk.Entry(self.master,width=30)
        self.Name_display.insert(2, self.name)
        self.Name_display.place(x=200, y=250)
        self.f_name_label = Label(self.master, text="Father name :",font=("Webdings Bold",14), bg="oldlace").place(x=50, y=300)
        self.f_name_display = ttk.Entry(self.master, width=30)
        self.f_name_display.insert(2,  self.father_name)
        self.f_name_display.place(x=200, y=300)
        self.dob_label = Label(self.master, text="Date Of Birth :",font=("Webdings Bold",14), bg="oldlace").place(x=50, y=350)
        self.dob_display = ttk.Entry(self.master, width=30)
        self.dob_display.insert(2, self.dob)
        self.dob_display.place(x=200, y=350)
        self.Mobile_No = Label(self.master, text="Mobile no:",font=("Webdings Bold",14), bg="oldlace").place(x=50, y=400)
        self.Mobile_No_display = ttk.Entry(self.master, width=30)
        self.Mobile_No_display.insert(2,  self.mob_no)
        self.Mobile_No_display.place(x=200, y=400)
        # account type combo
        self.account_types = ["Current", "Saving", "Fixed account"]
        self.account_type = Label(self.master, text="account type", font=("Webdings Bold",14), bg="oldlace").place(x=50, y=450)
        self.account_type_combo = Combobox(self.master, values=self.account_types, width=15,state="readonly",font=("Webdings Bold",14))  # state prevent change in combo value
        self.account_type_combo.set(  self.ac_type)
        self.account_type_combo.place(x=200, y=450)
        self.Id_No = Label(self.master, text="Id Number:",font=("Webdings Bold",14), bg="oldlace").place(x=50, y=500)
        self.Id_No_display= ttk.Entry(self.master, width=30)
        self.Id_No_display.insert(2,self.id_no)
        self.Id_No_display.place(x=200, y=500)
        # id combo
        self.id_types=["Citizenship","driving License","Student Card"]
        self.id_type_label = Label(self.master, text="Id type",font=("Webdings Bold",14), bg="oldlace").place(x=50, y=550)
        self.id_type_combo = Combobox(self.master, values=self.id_types,width=15,state="readonly",font=("Webdings Bold",14))  # state prevent change in combo value
        self.id_type_combo.set(self.id_type)
        self.id_type_combo.place(x=200, y=550)

        self.mother_name_label= Label(self.master, text="Mother name :", font=("Webdings Bold", 14), bg="oldlace").place(x=50,y=600)
        self.mother_name_display = ttk.Entry(self.master, width=30)
        self.mother_name_display.insert(2, self.mother_name)
        self.mother_name_display.place(x=200, y=600)
        self.address = Label(self.master, text="Address", font=("verdana Bold", 14),bg="oldlace").place(x=440, y=430)
        self.permanent_address_label = Label(self.master, text="permanent ", font=("Webdings Bold",14),bg="oldlace").place(x=445, y=480)
        self.peramnent_address_entry = ttk.Entry(self.master,  width=25)
        self.peramnent_address_entry.place(x=550, y=480)
        self.peramnent_address_entry.insert(2,self.per_add)
        self.temporary_address_label = Label(self.master, text="temporary ", font=("Webdings Bold",14),bg="oldlace").place(x=450, y=520)
        self.temporary_address_entry = ttk.Entry(self.master, width=25)
        self.temporary_address_entry.place(x=550, y=520)
        self.temporary_address_entry.insert(2,self.tem_add)
        # combo for occupation
        self.occupation = ["Farmer", "Student", "Businessman", "Journalist", "Teacher", "Doctor", "Engineer", "Pilot","Driver", "Other"]
        self.occupation_type = Label(self.master, text="occupation", font=("Webdings Bold",14),bg="oldlace").place(x=450, y=560)
        self.occupation_combo = Combobox(self.master, values=self.occupation, width=12, font=("Webdings Bold",14))
        # combo binding
        # why not working---------------------------------------------------------------------------------------------------------------------------------------------------
        self.occupation_combo.bind("<Return>", self.get_edited_display)
        self.occupation_combo.set(self.occp)
        self.occupation_combo.place(x=550, y=560)
        # left canvas for photo
        self.rectangle1 = self.canvas1.create_rectangle(500, 60, 700, 260, fill="mint cream")
        # upload button in order to upload photo
        # not working it why-------------------------------------------------------------------------------------------------------------------------------------
        #self.upload_button_import = PhotoImage(file='upload.png')
        #self.upload_button = Button(self.master, image=self.upload_button_import, highlightthickness=0, bd=0)
        #self.upload_button.place(x=530, y=330)
        self.new_image_directory_label= Label(self.master, text="Image directory ", font=("Webdings Bold",14),bg="oldlace").place(x=400, y=300)
        self.new_image_directory_entry = ttk.Entry(self.master, width=25,font=("Webdings Bold", 10))
        self.new_image_directory_entry.place(x=550, y=300)
        self.new_image_directory_entry.insert(2,self.img_dir)
        self.new_image_directory_label = Label(self.master, text="only .jpg and .png extension supported", font=("Webdings Bold", 12),bg="oldlace",fg="red").place(x=440, y=340)
        self.upload_new_image = Button(self.master,text="upload to update ",fg="white",bg="blue2",font=("Verdana Bold",12))
        self.upload_new_image.place(x=530, y=380)
        # upadate button import
        #self.update_button_import = PhotoImage(file='update1.png')
        #self.update_button_display = Button(self.master, image=self.update_button_import, bd=0, highlightthickness=0,command=self.get_current_display).place(x=500, y=600)
        self.edit_button = Button(self.master,text="Edit submit",fg="white",bg="blue2",font=("Verdana Bold",12),command=self.get_edited_display)
        # button bind
        self.edit_button.bind("<Return>",self.get_edited_display)
        self.edit_button.place(x=500, y=620)


    # to display customer information after update
    def get_edited_display(self,event=""):

        self.name1= self.Name_display.get()
        self.f_name1=self.f_name_display.get()
        self.m_name1=self.mother_name_display.get()
        self.dob1=self.dob_display.get()
        self.mob1= self.Mobile_No_display.get()
        self.acount_type1=self.account_type_combo.get()
        self.id_no1=self.Id_No_display.get()
        self.id_type1=self.id_type_combo .get()
        self.per_ad1=self.peramnent_address_entry.get()
        self.tem_ad1=self.temporary_address_entry.get()
        self.occp1=self.occupation_combo.get()
        self.img1= self.new_image_directory_entry.get()

        self.edit_account = mysql.connector.connect(
            user="root",
            host="localhost",
            passwd="",
            database="yvd_database",
        )
        self.edit_account_insert = self.edit_account.cursor()
        self.sql_query1="UPDATE customer_data SET ac_holder_name=%s,f_name=%s,m_name=%s,dob=%s,mobile_no=%s,account_type=%s,id_number=%s,id_type=%s,occupation=%s,per_address=%s,tem_address=%s,image_directory=%s WHERE account_num=%s "
        self.edit_records=(self.name1,self.f_name1,self.m_name1,self.dob1,self.mob1,self.acount_type1,self.id_no1,self.id_type1,self.occp1,self.per_ad1,self.tem_ad1,self.img1,self.account_number1)
        self.edit_account_insert.execute(self.sql_query1,self.edit_records)
        self.edit_account.commit()
        self.edit_account_insert.close()
        self.edit_account.close()

        # inorder to display edited content
        self.edit_account_diplay = mysql.connector.connect(
            user="root",
            host="localhost",
            passwd="",
            database="yvd_database",
        )
        self.edit_account_display_cursor = self.edit_account_diplay.cursor()
        sql_query2 = """select * from customer_data where account_num = %s """
        query_var2 = (account_num,)
        self.edit_account_display_cursor.execute(sql_query2, query_var2)
        edited_data = self.edit_account_display_cursor.fetchall()
        for result in edited_data:
            self.name2 = result[0]
            self.father_name2=result[1]
            self.mother_name2=result[2]
            self.sex2=result[3]
            self.dob2=result[4]
            self.age2 = result[5]
            self.mob_no2 = result[6]
            self.ac_type2=result[7]
            self.id_no2 = result[8]
            self.id_type2 = result[9]
            self.occp2= result[10]
            self.per_add2= result[11]
            self.tem_add2 = result[12]
            self.img_dir2=result[14]
            self.ac_no2 = result[15]
            self.br2= result[18]
            self.cr_bl2=result[13]

        # inserting edited data on statement user
        customer_name = str(self.name2.lower())
        customer_acc = str(self.ac_no2)
        store_customer = ""
        for var in customer_name:
            if (var.isspace() == True):
                store_customer = store_customer + "_"
            else:
                store_customer = store_customer + var

        store_customer = store_customer + "_" + customer_acc
        print(store_customer)
        opn = "edit"
        issued = "--------"
        ts = "--------"
        per_by="self"
        amnt="0"
        cr_time = time.asctime()
        edit_insert_statement = " INSERT INTO " + store_customer + " ( date_and_time,operation,amount,performed_by,transfer_to,branch,issued_by) VALUES (%s,%s,%s,%s,%s,%s,%s) "
        record_statement2 = (cr_time, opn,amnt,per_by, ts, self.br2, issued)
        self.edit_account_display_cursor.execute(edit_insert_statement, record_statement2)
        self.edit_account_diplay.commit()
        self.edit_account_display_cursor.close()
        self.edit_account_diplay.close()

        self.print_name = Label(self.master, text="Account updated succesfully and is ", font=("Verdana Bold", 18), fg="blue2", bg="thistle2").place(x=750, y=10)
        self.font1 = "helvetica Bold ", 14
        self.name_label2 = Label(self.master, text="Name", font=("Kokila Bold",20), fg="green", bg="thistle2").place(x=750, y=80)
        self.name_display2 = Label(self.master, text=self.name2, font=("Kokila Bold", 20), bg="thistle2").place(x=900, y=80)
        self.f_name_label2 = Label(self.master, text="Father name",fg="green", font=("Kokila Bold",20), bg="thistle2").place(x=750,y=130)
        self.f_name_display2 = Label(self.master, text= self.father_name2, font=("Kokila Bold", 20),bg="thistle2").place(x=900, y=130)
        self.mother_name_label2 = Label(self.master, text="Mother name", fg="green", font=("Kokila Bold",20), bg="thistle2").place(x=750,y=180)
        self.mother_name_display2 = Label(self.master, text=self.mother_name2, font=("Kokila Bold", 20), bg="thistle2").place(x=900, y=180)
        self.sex_label2 = Label(self.master, text="Sex",fg="green", font=("Kokila Bold",20), bg="thistle2").place(x=750, y=230)
        self.sex_display2 = Label(self.master, text= self.sex2, font=("Kokila Bold", 20), bg="thistle2").place(x=900, y=230)
        self.dob_label2= Label(self.master, text="Date of birth", fg="green", font=("Kokila Bold",20), bg="thistle2").place(x=750, y=280)
        self.dob_display2= Label(self.master, text=self.dob2, font=("Kokila Bold",20), bg="thistle2").place(x=900, y=280)
        self.age_label2 = Label(self.master, text="age", fg="green", font=("Kokila Bold",20), bg="thistle2").place(x=750, y=330)
        self.age_display2 = Label(self.master, text=self.age2, font=("Kokila Bold", 20), bg="thistle2").place(x=900, y=330)
        self.mob_label2 = Label(self.master, text="mobile number",fg="green", font=("Kokila Bold",20), bg="thistle2").place(x=750, y=380)
        self.mob_diplay2 = Label(self.master, text=self.mob_no2,font=("Kokila Bold", 20),bg="thistle2").place(x=900, y=380)
        self.account_type_label2= Label(self.master, text="account type", fg="green", font=("Kokila Bold",20), bg="thistle2").place(x=750,y=430)
        self.account_type_display2= Label(self.master, text=self.ac_type2, font=("Kokila Bold", 20),bg="thistle2").place(x=900, y=430)
        self.id_number_label2 = Label(self.master, text="id number", fg="green", font=("Kokila Bold", 20),bg="thistle2").place(x=750, y=480)
        self.id_number_display2 = Label(self.master, text=self.id_no2,font=("Kokila Bold",20), bg="thistle2").place(x=900, y=480)
        self.id_type_label2 = Label(self.master, text="id type", fg="green", font=("Kokila Bold",20), bg="thistle2").place(x=750,y=530)
        self.id_type_display2 = Label(self.master, text=self.id_type2,font=("Kokila Bold", 20),bg="thistle2").place(x=900, y=530)
        self.occupation_label2= Label(self.master, text="Ocuupation",fg="green", font=("Kokila Bold",20), bg="thistle2").place(x=750,y=580)
        self.occupation_display2 = Label(self.master, text=self.occp2,font=("Kokila Bold", 20),bg="thistle2").place(x=900, y=580)
        self.branch_label2 = Label(self.master, text="branch",fg="green", font=("Kokila Bold",20), bg="thistle2").place(x=750, y=630)
        self.branch_display2 = Label(self.master, text=self.br2, font=("Kokila Bold", 20),bg="thistle2").place(x=900, y=630)
        self.address_label2 = Label(self.master, text="Address", fg="green", font=("Kokila Bold",20), bg="thistle2").place(x=1050,y=380)
        self.permanent_address_labe2 = Label(self.master, text="permanent", fg="green", font=("Kokila Bold", 20),bg="thistle2").place(x=1050, y=430)
        self.permanent_address_display2 = Label(self.master, text=self.per_add2, font=("Kokila Bold", 20), bg="thistle2").place(x=1200, y=430)
        self.temporary_address_labe2 = Label(self.master, text="Temporary", fg="green", font=("Kokila Bold",20), bg="thistle2").place(x=1050,y=480)
        self.temporary_address_display2 = Label(self.master, text=self.tem_add2,font=("Kokila Bold", 20),bg="thistle2").place(x=1200, y=480)
        self.ac_no_label2 = Label(self.master, text="account number",fg="green", font=("Kokila Bold",20), bg="thistle2").place(x=1050, y=530)
        self.ac_no_display2 = Label(self.master, text=self.ac_no2,font=("Kokila Bold", 20),bg="thistle2").place(x=1200, y=530)
        self.balance_label2 = Label(self.master, text="Current balance",fg="green", font=("Kokila Bold",20), bg="thistle2").place(x=1050, y=580)
        self.balance_display2 = Label(self.master, text=self.cr_bl2,font=("Kokila Bold", 20),bg="thistle2").place(x=1200, y=580)

        # image display on result
        self.rectangle2 = self.canvas2.create_rectangle(400, 60, 600, 300, fill="mint cream")
        #self.img_directory_display= Label(self.master, text=self.img_dir2,fg="green", font=("Kokila Bold",20), bg="mint cream").place(x=430, y=150)


def edit_main(event=""):
    window_edit=Tk()
    window_edit.title("Youth Voice Nepal - Edit Section")
    # to get full window
    width = window_edit.winfo_screenwidth()
    height = window_edit.winfo_screenheight()
    window_edit.geometry("%dx%d" % (width, height))
    # window.resizable(False,False)  # used for not resizable window
    # or window.resizable(0,0)
    window_edit.resizable(True, True)
    # icon on top
    # error here-----------------------------------------------------------------------------------------------------------------------------------------------------
    #icon_image = Image("photo", file="1.ico")
    #window_edit.call('wm', 'iconphoto', window_edit._w, icon_image)
    frame = Frame(window_edit)
    frame.pack()
    get_edit=edit(window_edit)
    window_edit.mainloop()



class delete:
    def __init__(self, master):
        # Very important fact to pass in the function inside the class
        self.master=master
        # left canvas to get register
        self.canvas1= Canvas(master, width=730, height=730, bg="oldlace")
        self.canvas1.pack(fill=Y, side=LEFT, anchor=W)
        # Right Canvas to show the registered record
        self.canvas2 = Canvas(master, width=730, height=730, bg="wheat2")
        self.canvas2.pack(fill=Y, side=RIGHT)
        self.welcome = Label(master, text="Enter customer details to delete account ",font=("Verdana Bold",18), bg="oldlace", fg="blue2").place(x=10, y=10)
        # left entry form
        self.name_delete = Label(master, text="name",font=("Webdings Bold",14), bg="oldlace").place(x=50, y=80)
        self.name_delete_entry = ttk.Entry(master,width=25)
        self.name_delete_entry.place(x=200, y=80)
        self.account_num_delete = Label(master, text="account number",font=("Webdings Bold",14), bg="oldlace").place(x=50, y=120)
        self.account_number_delete_entry = ttk.Entry(master,width=25)
        # entry binding
        self.account_number_delete_entry.bind("<Return>",self.get_request_delete)
        self.account_number_delete_entry.place(x=200, y=120)
        # Request information  button
        # this is not working----------------------------------------------------------------------------------------------------------------------
        #self.request_button_import = PhotoImage(file='request info2.png')
        #self.request_button = Button(master, image=self.request_button_import, highlightthickness=0, bd=0,command=self.get_request)
        #self.request_button.place(x=140, y=180)
        self.request_information_button = Button(master,text="request information",fg="white",bg="blue2",font=("Verdana Bold",12),command=self.get_request_delete)
        # binding button
        self.request_information_button.bind("<Return>",self.get_request_delete)
        self.request_information_button.place(x=140, y=180)


    # to display available balance
    def get_request_delete(self,event=""):
        global ac_holder_name
        global account_number
        ac_holder_name= self.name_delete_entry.get().title()
        account_number= self.account_number_delete_entry.get()

        # inorder to display customer info who want to delete account
        self.delete_account= mysql.connector.connect(
            user="root",
            host="localhost",
            passwd="",
            database="yvd_database",
        )
        self.request_delete_account_info= self.delete_account.cursor()
        sql_query5 = """select * from customer_data where ac_holder_name=%s and account_num = %s """
        query_var5 = (ac_holder_name,account_number,)
        self.request_delete_account_info.execute(sql_query5, query_var5)
        delete_request_data = self.request_delete_account_info.fetchall()
        for result in delete_request_data:
            self.name5 = result[0]
            self.mob_no5 = result[6]
            self.id_no5 = result[8]
            self.ac_no5 = result[15]
            self.br5 = result[18]
            self.cr_bl5 = result[13]

        # using self.master as window
        self.Name = Label(self.master, text="Name : ",font=("Webdings Bold",14), bg="oldlace").place(x=50, y=250)
        self.Name_display = Label(self.master, text=self.name5).place(x=200, y=250)
        self.Account_No = Label(self.master, text="Account number :",font=("Webdings Bold",14), bg="oldlace").place(x=50, y=300)
        self.Account_No_display = Label(self.master, text=self.ac_no5).place(x=200, y=300)
        self.Mobile_No = Label(self.master, text="Mobile number:",font=("Webdings Bold",14), bg="oldlace").place(x=50, y=350)
        self.Mobile_No_display = Label(self.master, text=self.mob_no5).place(x=200, y=350)
        self.Id_No = Label(self.master, text="ID Number:",font=("Webdings Bold",14), bg="oldlace").place(x=50, y=400)
        self.Id_No_display = Label(self.master, text=self.id_no5).place(x=200, y=400)
        self.Avl_balance = Label(self.master, text="Current amount :",font=("Webdings Bold",14), bg="oldlace").place(x=50, y=450)
        self.Avl_balance_display = Label(self.master, text=self.cr_bl5).place(x=200, y=450)
        self.branch = Label(self.master, text="Branch ", font=("Webdings Bold",14), bg="oldlace").place(x=50, y=500)
        self.branch_display = Label(self.master, text=self.br5).place(x=200, y=500)
        # canvas for photo
        self.rectangle1 = self.canvas1.create_rectangle(500, 60, 720, 300, fill="mint cream")
        self.user_info = Label(self.master, text="Why custormer want to delete this account ? ", font=("Verdana Bold", 15),bg="oldlace", fg="blue2").place(x=50, y=540)
        text = Text(self.master, width=60, height=3, wrap=WORD, selectbackground="yellow", selectforeground="red",bd=4)
        text.configure(font=("Arial Bold", 10))
        text.place(x=60,y=595)
        # upadate button import
        # this is not working------------------------------------------------------------------------------------------------------------------------------------
        #self.update_button_import=PhotoImage(file='update1.png')
        #self.update_button_display=Button(self.master,image=self.update_button_import,bd=0, highlightthickness=0,command=self.get_delete).place(x=500,y=600)
        self.update_button_display=Button(self.master,text="delete information",fg="white",bg="blue2",font=("Verdana Bold",12),command=self.get_delete_info)
        # binding button
        self.update_button_display.bind("<Return>",self.get_delete_info)
        self.update_button_display.place(x=530,y=620)


    # to display customer information after update
    def get_delete_info(self,event=""):
        current_balance5=int(self.cr_bl5)
        # inorder to withdraw amount first
        if(current_balance5>=100):
            self.cs_info = Label(self.master, text="Withdraw first your current amount "+str(current_balance5), font=("Verdana Bold", 12), fg="red",bg="oldlace").place(x=300,y=450)
            self.withdraw_button_display = Button(self.master, text="Withdraw here", fg="white", bg="blue2",font=("Verdana Bold", 12), command=withdraw_main)
            # binding button
            self.withdraw_button_display.bind("<Return>", self.get_delete_info)
            self.withdraw_button_display.place(x=530, y=500)
        elif(current_balance5<100):
            sql_query6 = "delete from customer_data where ac_holder_name=%s and account_num = %s "
            query_var6 = (ac_holder_name, account_number,)
            self.request_delete_account_info.execute(sql_query6, query_var6)
            self.delete_account.commit()
            self.request_delete_account_info.close()
            self.delete_account.close()
            # if no error occurs
            print_name = Label(self.master, text="Account deleted succesfully.", font=("Verdana Bold", 18),fg="blue2", bg="thistle2").place(x=750, y=400)

        # whats the hell is going here ---------------------------------------------------------------------------------------------------------------------------------------
        #from tkinter import messagebox
        #self.user_input1 = messagebox.askquestion("Account deletion inquiry!", "Are you sure to delete account ?")
        #if(self.user_input1=='yes'):
        #print_name = Label(self.master, text="Account deleted succesfully.", font=("Verdana Bold", 18),fg="blue2", bg="thistle2").place(x=750, y=10)
        # self.master.destroy()


def delete_main(event=""):
    window_delete=Tk()
    window_delete.title("Youth Voice Nepal - Account Delete Section")
    # to get full window
    width = window_delete.winfo_screenwidth()
    height = window_delete.winfo_screenheight()
    window_delete.geometry("%dx%d" % (width, height))
    # window.resizable(False,False)  # used for not resizable window
    # or window.resizable(0,0)
    window_delete.resizable(True, True)
    # icon on top
    # this is not working--------------------------------------------------------------------------------------------------------------------------
    #icon_image = Image("photo", file="1.ico")
    #window_delete.call('wm', 'iconphoto', window_delete._w, icon_image)
    frame = Frame(window_delete)
    frame.pack()
    get_delete=delete(window_delete)
    window_delete.mainloop()


class deposit:
    def __init__(self, master):
        # Very important fact to pass in the function inside the class
        self.master = master
        # left canvas to get register
        self.canvas1 = Canvas(master, width=730, height=730, bg="oldlace")
        self.canvas1.pack(fill=Y, side=LEFT, anchor=W)
        # Right Canvas to show the registered record
        self.canvas2 = Canvas(master, width=730, height=730, bg="wheat2")
        self.canvas2.pack(fill=Y, side=RIGHT)
        self.welcome = Label(master, text="Enter customer details to withdraw ", font=("Verdana Bold", 18),
                             bg="oldlace", fg="blue2").place(x=10, y=10)
        # left entry form
        self.name = Label(master, text="name", font=("Verdana Bold", 12), bg="oldlace").place(x=50, y=80)
        self.name_entry = ttk.Entry(master, width=25)
        self.name_entry.place(x=200, y=80)
        self.account_num = Label(master, text="account number", font=("Verdana Bold", 12), bg="oldlace").place(x=50,
                                                                                                               y=120)
        self.account_number_entry = ttk.Entry(master, width=25)
        self.account_number_entry.bind("<Return>", self.get_request_deposit)
        self.account_number_entry.place(x=200, y=120)
        # Request information  button
        # why error here-----------------------------------------------------------------------------------------------------------------
        # self.request_button_import = PhotoImage(file='request info2.png')
        # self.request_button = Button(master, image=self.request_button_import, highlightthickness=0, bd=0,command=self.get_request)
        # self.request_button.place(x=140, y=180)
        self.request_deposit_button = Button(master, text="request information", fg="white", bg="blue2",
                                              font=("Verdana Bold", 14), command=self.get_request_deposit)
        self.request_deposit_button.bind("<Return>", self.get_request_deposit)
        self.request_deposit_button.place(x=140, y=180)

        # to display available balance

    def get_request_deposit(self, event=""):
        global holder_name
        global account_num
        global mobile_num
        global id_num
        global avl_bal
        global deposit_amount
        holder_name = self.name_entry.get().title()
        account_num = self.account_number_entry.get()
        self.deposit_account = mysql.connector.connect(
            user="root",
            host="localhost",
            passwd="",
            database="yvd_database",
        )
        self.customer_account_register = self.deposit_account.cursor()
        sql_query = """select * from customer_data where ac_holder_name like %s and account_num like %s """
        query_var = (holder_name, account_num,)
        self.customer_account_register.execute(sql_query, query_var)
        output = self.customer_account_register.fetchall()
        for result in output:
            self.name = result[0]
            self.ac_no = result[15]
            self.mob_no = result[6]
            self.id_no = result[8]
            self.cur_amt = result[13]
            self.br = result[18]

            print(self.name)
            print(self.ac_no)
            print(self.mob_no)
            print(self.id_no)
            print(self.cur_amt)
            print(self.br)
            self.customer_account_register.close()
            self.deposit_account.close()
        # using self.master as window
        self.Name = Label(self.master, text="Name : ", font=("Verdana Bold", 12), bg="oldlace").place(x=50, y=250)
        self.Name_display = Label(self.master, text=self.name).place(x=200, y=250)
        self.Account_No = Label(self.master, text="Account number :", font=("Verdana Bold", 12), bg="oldlace").place(
            x=50, y=300)
        self.Account_No_display = Label(self.master, text=self.ac_no).place(x=200, y=300)
        self.Mobile_No_label = Label(self.master, text="Mobile number:", font=("Verdana Bold", 12), bg="oldlace").place(
            x=50, y=350)
        self.Mobile_No_display = Label(self.master, text=self.mob_no).place(x=200, y=350)
        self.Id_No = Label(self.master, text="ID Number:", font=("Verdana Bold", 12), bg="oldlace").place(x=50, y=400)
        self.Id_No_display = Label(self.master, text=self.id_no).place(x=200, y=400)
        self.Avl_balance = Label(self.master, text="Current amount :", font=("Verdana Bold", 12), bg="oldlace").place(
            x=50, y=450)
        self.Avl_balance_display = Label(self.master, text=self.cur_amt).place(x=200, y=450)
        self.branch = Label(self.master, text="Branch ", font=("Verdana Bold", 12), bg="oldlace").place(x=50, y=500)
        self.branch_display = Label(self.master, text=self.br).place(x=200, y=500)
        # canvas for photo
        self.rectangle1 = self.canvas1.create_rectangle(500, 60, 720, 300, fill="mint cream")
        self.user_info = Label(self.master, text="Please read and enter carefully ", font=("Verdana Bold", 14),
                               bg="oldlace", fg="blue2").place(x=50, y=540)
        self.deposited_by_label = Label(self.master, text="Deposited by", font=("Verdana Bold", 12),
                                        bg="oldlace").place(x=50, y=580)
        self.deposited_by_entry = ttk.Entry(self.master, width=25)
        self.deposited_by_entry.place(x=260, y=580)
        self.deposit_message = Label(self.master, text="Amount to Deposit", font=("Verdana Bold", 12),
                                      bg="oldlace").place(x=50, y=610)
        self.amount_deposit = ttk.Entry(self.master, width=25)
        self.amount_deposit.bind("<Return>", self.get_display_deposit)
        self.amount_deposit.place(x=260, y=610)
        # withdraw amount  button
        # why error here----------------------------------------------------------------------------------------------------------------
        # self.withdraw_button_import = PhotoImage(file='withdraw button1.png')
        # self.withdraw_button = Button(self.master, image=self.withdraw_button_import, highlightthickness=0, bd=0,command=self.get_display)
        # self.withdraw_button.place(x=370, y=640)
        self.deposit_button = Button(self.master, text="perform deposit ", bg="blue2", fg="white",
                                      font=("Verdana Bold", 14), command=self.get_display_deposit)
        self.deposit_button.bind("<Return>", self.get_display_deposit)
        self.deposit_button.place(x=450, y=615)

        # to display amout after withdraw

    def get_display_deposit(self, event=""):
        self.current_time = time.asctime()
        self.deposited_by_name = self.deposited_by_entry.get()
        self.deposit_amt = self.amount_deposit.get()
        self.deposit_desire = int(self.deposit_amt)
        self.current_amt = int(self.cur_amt)
        if (self.deposit_desire < 1000):
            self.withdraw_response = Label(self.master,text="you can't deposit amount less than '1000'",fg="red", bg="oldlace", font=("Verdana Bold", 12)).place(x=80, y=650)
        elif (self.deposit_desire == 0):
            self.withdraw_response = Label(self.master, text="you can't enter '0' , Please enter valid amount",fg="red", bg="oldlace", font=("Verdana Bold", 12)).place(x=80, y=650)
        elif (self.deposit_desire >= 10000000):
            self.withdraw_response = Label(self.master, text="you can't deposit more than '10000000' in a single day ",fg="red", bg="oldlace", font=("Verdana Bold", 12)).place(x=80, y=650)
        else:
            self.amount_after_deposit = self.current_amt + self.deposit_desire
            self.deposit_update = mysql.connector.connect(
                user="root",
                host="localhost",
                passwd="",
                database="yvd_database",
            )
            self.update_amount_after_deposit = self.deposit_update.cursor()
            self.update_amount_after_deposit.execute("UPDATE customer_data SET current_amount=%s WHERE account_num = %s ",(self.amount_after_deposit, self.ac_no,))
            self.deposit_update.commit()
            sql_query2 = """select * from customer_data where ac_holder_name like %s and account_num like %s """
            query_var2 = (holder_name, account_num,)
            self.update_amount_after_deposit.execute(sql_query2, query_var2)
            data = self.update_amount_after_deposit.fetchall()
            for result in data:
                self.name1 = result[0]
                self.ac_no1 = result[15]
                self.id_no1 = result[8]
                self.cur_amt1 = result[13]


            # inserting deposit data on statement user
            customer_name=str(self.name1.lower())
            customer_acc=str(self.ac_no1)
            store_customer = ""
            for var in customer_name:
                if (var.isspace() == True):
                    store_customer = store_customer + "_"
                else:
                    store_customer = store_customer + var

            store_customer = store_customer + "_" + customer_acc
            print(store_customer)
            opn="deposit"
            issued="--------"
            ts= "--------"
            cr_time=time.asctime()
            deposit_insert_statement=" INSERT INTO " + store_customer + " ( date_and_time,operation,amount,performed_by,transfer_to,branch,issued_by) VALUES (%s,%s,%s,%s,%s,%s,%s) "
            record_statement1=(cr_time,opn, self.deposit_desire,self.deposited_by_name,ts,self.br,issued)
            self.update_amount_after_deposit.execute(deposit_insert_statement,record_statement1)
            self.deposit_update.commit()
            self.update_amount_after_deposit.close()
            self.deposit_update.close()

            self.label = Label(self.master, text="Deposited amount succesfully,current info is",
                               font=("Verdana Bold", 16), fg="blue2", bg="wheat2").place(x=780, y=70)
            # canvas for photo
            # self.rectangle2 = self.canvas2.create_rectangle(770, 130, 1200, 570, fill="mint cream")
            self.name_label = Label(self.master, text="Name : ", font=("Verdana Bold", 12), bg="wheat2").place(x=780,y=150)
            self.name_name_display = Label(self.master, text=self.name1, bg="wheat2").place(x=950, y=150)
            self.account_label = Label(self.master, text="Account number :", font=("Verdana Bold", 12),bg="wheat2").place(x=780, y=200)
            self.account_no_display = Label(self.master, text=self.ac_no1, bg="wheat2").place(x=950, y=200)
            self.amountt_ladel = Label(self.master, text="Current Balance :", font=("Verdana Bold", 12), bg="wheat2").place(x=780, y=250)
            self.Amount_after_withdraw = Label(self.master, text=self.cur_amt1, bg="wheat2").place(x=950, y=250)
            self.date_label = Label(self.master, text="Date", font=("Verdana Bold", 12), bg="wheat2").place(x=780, y=300)
            self.date_display = Label(self.master, text=self.current_time, bg="wheat2").place(x=950, y=300)
            self.Id_No = Label(self.master, text="ID Number:", font=("Verdana Bold", 12), bg="wheat2").place(x=780, y=350)
            self.Id_No_display = Label(self.master, text=self.id_no1, bg="wheat2").place(x=950, y=350)
            self.deposited_by = Label(self.master, text="Withdrawn By", font=("Verdana Bold", 12), bg="wheat2").place( x=780, y=400)
            self.deposited_by_display = Label(self.master, text=self.deposited_by_name, bg="wheat2").place(x=950, y=400)
            self.Id_No = Label(self.master, text="Issued By", font=("Verdana Bold", 12), bg="wheat2").place(x=780,y=450)
            self.Id_No_display = Label(self.master, text="", bg="wheat2").place(x=950, y=450)


def deposit_main(event=""):
    window_deposit=Tk()
    window_deposit.title("Youth Voice Nepal -Deposit Section")
    # to get full window
    width = window_deposit.winfo_screenwidth()
    height = window_deposit.winfo_screenheight()
    window_deposit.geometry("%dx%d" % (width, height))
    # window.resizable(False,False)  # used for not resizable window
    # or window.resizable(0,0)
    window_deposit.resizable(True, True)
    # icon on top
    # why error here ---------------------------------------------------------------------------------------------------------------------
    #icon_image = Image("photo", file="1.ico")
    #window_deposit.call('wm', 'iconphoto', window_deposit._w, icon_image)
    frame = Frame(window_deposit)
    frame.pack()
    get_deposit=deposit(window_deposit)
    window_deposit.mainloop()


class withdraw:
    def __init__(self, master):
        # Very important fact to pass in the function inside the class
        self.master = master
        # left canvas to get register
        self.canvas1 = Canvas(master, width=730, height=730, bg="oldlace")
        self.canvas1.pack(fill=Y, side=LEFT, anchor=W)
        # Right Canvas to show the registered record
        self.canvas2 = Canvas(master, width=730, height=730, bg="wheat2")
        self.canvas2.pack(fill=Y, side=RIGHT)
        self.welcome = Label(master, text="Enter customer details to withdraw ", font=("Verdana Bold", 18), bg="oldlace", fg="blue2").place(x=10, y=10)
        # left entry form
        self.name = Label(master, text="name", font=("Verdana Bold", 12), bg="oldlace").place(x=50, y=80)
        self.name_entry = ttk.Entry(master, width=25)
        self.name_entry.place(x=200, y=80)
        self.account_num = Label(master, text="account number", font=("Verdana Bold", 12), bg="oldlace").place(x=50,y=120)
        self.account_number_entry = ttk.Entry(master, width=25)
        self.account_number_entry.bind("<Return>",self.get_request_withdraw)
        self.account_number_entry.place(x=200, y=120)
        # Request information  button
        # why error here-----------------------------------------------------------------------------------------------------------------
        # self.request_button_import = PhotoImage(file='request info2.png')
        # self.request_button = Button(master, image=self.request_button_import, highlightthickness=0, bd=0,command=self.get_request)
        # self.request_button.place(x=140, y=180)
        self.request_withdraw_button = Button(master, text="request information", fg="white", bg="blue2",font=("Verdana Bold",14),command=self.get_request_withdraw)
        self.request_withdraw_button.bind("<Return>",self.get_request_withdraw)
        self.request_withdraw_button.place(x=140, y=180)


    # to display available balance
    def get_request_withdraw(self,event=""):
        global holder_name
        global account_num
        global mobile_num
        global id_num
        global avl_bal
        global deposit_amount
        holder_name=self.name_entry.get().title()
        account_num=self.account_number_entry.get()
        self.withdraw_account = mysql.connector.connect(
            user="root",
            host="localhost",
            passwd="",
            database="yvd_database",
        )
        self.customer_account_register=self.withdraw_account.cursor()
        sql_query="""select * from customer_data where ac_holder_name like %s and account_num like %s """
        query_var=(holder_name,account_num,)
        self.customer_account_register.execute(sql_query,query_var)
        output=self.customer_account_register.fetchall()
        for result in output:
            self.name=result[0]
            self.ac_no=result[15]
            self.mob_no =result[6]
            self.id_no = result[8]
            self.cur_amt = result[13]
            self.br= result[18]

            print(self.name)
            print(self.ac_no)
            print(self.mob_no)
            print(self.id_no)
            print(self.cur_amt)
            print(self.br)
            self.customer_account_register.close()
            self.withdraw_account.close()
        # using self.master as window
        self.Name = Label(self.master, text="Name : ", font=("Verdana Bold", 12), bg="oldlace").place(x=50, y=250)
        self.Name_display = Label(self.master, text=self.name).place(x=200, y=250)
        self.Account_No = Label(self.master, text="Account number :", font=("Verdana Bold", 12), bg="oldlace").place(x=50, y=300)
        self.Account_No_display = Label(self.master, text=self.ac_no).place(x=200, y=300)
        self.Mobile_No_label= Label(self.master, text="Mobile number:", font=("Verdana Bold", 12), bg="oldlace").place(x=50, y=350)
        self.Mobile_No_display = Label(self.master,text=self.mob_no).place(x=200, y=350)
        self.Id_No = Label(self.master, text="ID Number:", font=("Verdana Bold", 12), bg="oldlace").place(x=50, y=400)
        self.Id_No_display = Label(self.master, text=self.id_no).place(x=200, y=400)
        self.Avl_balance = Label(self.master, text="Current amount :", font=("Verdana Bold", 12), bg="oldlace").place(x=50, y=450)
        self.Avl_balance_display = Label(self.master, text=self.cur_amt).place(x=200, y=450)
        self.branch = Label(self.master, text="Branch ", font=("Verdana Bold", 12), bg="oldlace").place(x=50, y=500)
        self.branch_display = Label(self.master, text=self.br).place(x=200, y=500)
        # canvas for photo
        self.rectangle1 = self.canvas1.create_rectangle(500, 60, 720, 300, fill="mint cream")
        self.user_info = Label(self.master, text="Please read and enter carefully ", font=("Verdana Bold", 14),bg="oldlace", fg="blue2").place(x=50, y=540)
        self.withdrawn_by_label = Label(self.master, text="withdrawn by", font=("Verdana Bold", 12), bg="oldlace").place(x=50, y=580)
        self.withdrawn_by_entry=ttk.Entry(self.master, width=25)
        self.withdrawn_by_entry .place(x=260,y=580)
        self.withdrawn_by_cheque = Label(self.master, text="(from cheque)", font=("Verdana Bold", 12), fg="green",bg="oldlace").place(x=500, y=580)
        self.withdraw_message = Label(self.master, text="Amount to Withdraw", font=("Verdana Bold", 12), bg="oldlace").place(x=50,y=610)
        self.amount_withdraw = ttk.Entry(self.master, width=25)
        self.amount_withdraw.bind("<Return>",self.get_display_withdraw)
        self.amount_withdraw.place(x=260, y=610)
        # withdraw amount  button
        # why error here----------------------------------------------------------------------------------------------------------------
        # self.withdraw_button_import = PhotoImage(file='withdraw button1.png')
        # self.withdraw_button = Button(self.master, image=self.withdraw_button_import, highlightthickness=0, bd=0,command=self.get_display)
        # self.withdraw_button.place(x=370, y=640)
        self.withdraw_button = Button(self.master, text="perform withdraw  ", bg="blue2", fg="white",font=("Verdana Bold",14),command=self.get_display_withdraw)
        self.withdraw_button.bind("<Return>",self.get_display_withdraw)
        self.withdraw_button.place(x=460, y=615)



    # to display amout after withdraw
    def get_display_withdraw(self,event=""):
        self.current_time = time.asctime()
        self.withdrawn_by_name= self.withdrawn_by_entry.get()
        self.withdraw_amt=self.amount_withdraw.get()
        self.withdraw_desire=int(self.withdraw_amt)
        self.current_amt=int( self.cur_amt)
        if(self.withdraw_desire>self.current_amt):
             self.withdraw_response =Label(self.master, text="you can't withdraw it because current amount is only  "+self.cur_amt+"/-", fg="red", bg="oldlace",font=("Verdana Bold", 12)).place(x=80,y=650)
        elif(self.withdraw_desire==0):
            self.withdraw_response = Label(self.master, text="you can't enter '0' , Please enter valid amount",fg="red", bg="oldlace", font=("Verdana Bold", 12)).place(x=80, y=650)
        elif (self.withdraw_desire < 500):
            self.withdraw_response = Label(self.master, text="you can't deposit less than '500'",fg="red", bg="oldlace", font=("Verdana Bold", 12)).place(x=80, y=650)
        elif(self.withdraw_desire>=1000000):
            self.withdraw_response = Label(self.master,text="you can't withdraw more than '1000000' in a single day ",fg="red", bg="oldlace", font=("Verdana Bold", 12)).place(x=80, y=650)
        else:
            self.amount_after_withdraw=self.current_amt-self.withdraw_desire
            self.withdraw_update = mysql.connector.connect(
                user="root",
                host="localhost",
                passwd="",
                database="yvd_database",
            )
            self.update_amount_after_withdraw = self.withdraw_update.cursor()
            self.update_amount_after_withdraw.execute("UPDATE customer_data SET current_amount=%s WHERE account_num = %s ",(self.amount_after_withdraw, self.ac_no,))
            self.withdraw_update.commit()
            sql_query1 = """select * from customer_data where ac_holder_name like %s and account_num like %s """
            query_var1 = (holder_name, account_num,)
            self.update_amount_after_withdraw.execute(sql_query1, query_var1)
            datas= self.update_amount_after_withdraw.fetchall()
            for result in datas:
                self.name1 = result[0]
                self.ac_no1= result[15]
                self.id_no1 = result[8]
                self.cur_amt1 = result[13]

            # inserting withdraw data on statement user
            cs_name=str(self.name1.lower())
            cs_acc=str(self.ac_no1)
            store_cs = ""
            for var in cs_name:
                if (var.isspace() == True):
                    store_cs = store_cs + "_"
                else:
                    store_cs = store_cs + var

            store_cs = store_cs + "_" + cs_acc
            print(store_cs)
            opn="withdraw"
            issue="--------"
            ts= "--------"
            #WHY ERROR HERE-------------------------------------------------------------------------------------------------------------------------------------
            withdraw_insert_statement=" INSERT INTO " + store_cs + " ( date_and_time,operation,amount,performed_by,transfer_to,branch,issued_by) VALUES (%s,%s,%s,%s,%s,%s,%s) "
            record_statement=(self.current_time,opn, self.withdraw_desire,self.withdrawn_by_name,ts,self.br,issue)
            self.update_amount_after_withdraw.execute(withdraw_insert_statement,record_statement)
            self.withdraw_update.commit()

            self.update_amount_after_withdraw.close()
            self.withdraw_update.close()

            self.label = Label(self.master, text="Withdraw perform succesfully,current info is", font=("Verdana Bold", 16),fg="blue2", bg="wheat2").place(x=780, y=70)
            # canvas for photo
            #self.rectangle2 = self.canvas2.create_rectangle(770, 130, 1200, 570, fill="mint cream")
            self.name_label = Label(self.master, text="Name : ", font=("Verdana Bold", 12), bg="wheat2").place(x=780, y=150)
            self.name_name_display = Label(self.master, text= self.name1,bg="wheat2").place(x=950, y=150)
            self.account_label = Label(self.master, text="Account number :", font=("Verdana Bold", 12), bg="wheat2").place(x=780,                                                                                                          y=200)
            self.account_no_display = Label(self.master, text=self.ac_no1,bg="wheat2").place(x=950, y=200)
            self.amountt_ladel = Label(self.master, text="Current Balance :", font=("Verdana Bold", 12), bg="wheat2").place(x=780,y=250)
            self.Amount_after_withdraw = Label(self.master, text= self.cur_amt1,bg="wheat2").place(x=950, y=250)
            self.date_label = Label(self.master, text="Date", font=("Verdana Bold", 12), bg="wheat2").place(x=780, y=300)
            self.date_display = Label(self.master, text=self.current_time,bg="wheat2").place(x=950, y=300)
            self.Id_No = Label(self.master, text="ID Number:", font=("Verdana Bold", 12), bg="wheat2").place(x=780, y=350)
            self.Id_No_display = Label(self.master, text=  self.id_no1,bg="wheat2").place(x=950, y=350)
            self.withdrawn_by = Label(self.master, text="Withdrawn By", font=("Verdana Bold", 12), bg="wheat2").place(x=780, y=400)
            self.withdrawn_by_display = Label(self.master, text= self.withdrawn_by_name,bg="wheat2").place(x=950, y=400)
            self.Id_No = Label(self.master, text="Issued By", font=("Verdana Bold", 12), bg="wheat2").place(x=780, y=450)
            self.Id_No_display = Label(self.master, text="",bg="wheat2").place(x=950, y=450)


def withdraw_main(event=""):
    window_withdraw = Tk()
    window_withdraw.title("Youth Voice Nepal -Withdraw Section")
    # to get full window
    width = window_withdraw.winfo_screenwidth()
    height = window_withdraw.winfo_screenheight()
    window_withdraw.geometry("%dx%d" % (width, height))
    # window.resizable(False,False)  # used for not resizable window
    # or window.resizable(0,0)
    window_withdraw.resizable(True, True)
    # icon on top
    # icon not working
    # icon_image = Image("photo", file="1.ico")
    # window_withdraw.call('wm', 'iconphoto', window_withdraw._w, icon_image)
    frame = Frame(window_withdraw)
    frame.pack()
    get_deposit = withdraw(window_withdraw)
    window_withdraw.mainloop()



class register():
    def __init__(self,master):
        self.font = "Verdana", 10
        # left canvas to get register
        self.canvas1= Canvas(master, width=680, height=730, bg="oldlace")
        self.canvas1.pack(fill=Y, side=LEFT, anchor=W)
        # Right Canvas to show the registered record
        self.canvas2 = Canvas(master, width=680, height=730, bg="thistle2")
        self.canvas2.pack(fill=Y, side=RIGHT)
        self.welcome = Label(master, text="Enter customer details & click save button",font=("Verdana Bold", 18), bg="oldlace", fg="blue2").place(x=10, y=10)
        # left entry form
        self.name_label = Label(master, text="name",font=("Verdana Bold",10), bg="oldlace").place(x=20, y=60)
        self.name_entry = ttk.Entry(master,width=25)
        self.name_entry.place(x=130, y=60)
        self.label_f_name = Label(master, text="father name",font=("Verdana Bold",10), bg="oldlace").place(x=20, y=100)
        self.father_entry = ttk.Entry(master,width=25)
        self.father_entry.place(x=130, y=100)
        self.label_m_name = Label(master, text="mother name",font=("Verdana Bold",10), bg="oldlace").place(x=20, y=150)
        self.mother_entry = ttk.Entry(master,width=25)
        self.mother_entry.place(x=130, y=150)
        self.gender = Label(master, text="sex",font=("Verdana Bold",10), bg="oldlace").place(x=20, y=200)
        # gender combobox
        self.gender_value = ("male", "female", "other")
        self.sex_combo = Combobox(master, values=self.gender_value,width=22,state="readonly")  # state prevent change in combo value
        self.sex_combo.set("select")
        self.sex_combo.place(x=130, y=200)
        # combobox  for dob
        self.label_dob = Label(master, text="Date of birth", font=("Verdana Bold", 10), bg="oldlace").place(x=20, y=250)
        # date combo
        self.date=list(range(1950,2076))
        self.year_combo= Combobox(master,height=10,values=self.date,width=6,state="readonly")
        self.year_combo.set("year")
        self.year_combo.place(x=130, y=250)
        # month combo
        self.month = list(range(1, 13))
        self.month_combo = Combobox(master,values=self.month,height=10,width=5,state="readonly")
        self.month_combo.set("month")
        self.month_combo.place(x=188, y=250)
        # day combo
        self.day = list(range(1, 33))
        self.day_combo = Combobox(master,height=10,values=self.day, width=4,state="readonly")
        self.day_combo.set("day")
        self.day_combo.place(x=240, y=250)
        self.age = Label(master, text="age",font=("Verdana Bold",10), bg="oldlace").place(x=20, y=300)
        # spinbox for age
        self.age_list = list(range(1, 150))
        self.age_combo = Combobox(master,height=10,values=self.age_list,width=22,state="readonly")
        self.age_combo.set("select")
        self.age_combo.place(x=130, y=300)
        self.label_mobile_number = Label(master, text="mobile number",font=("Verdana Bold",10), bg="oldlace").place(x=20, y=350)
        self.mobile_number_entry = ttk.Entry(master,width=25)
        self.mobile_number_entry.place(x=130, y=350)
        # combo for account type
        self.account_types_list=["Current","Saving","Fixed account"]
        self.account_type_label = Label(master, text="account type",font=("Verdana Bold",10), bg="oldlace").place(x=20, y=400)
        self.account_type_combo = Combobox(master, values=self.account_types_list,width=22,state="readonly")  # state prevent change in combo value
        self.account_type_combo.set("select")
        self.account_type_combo.place(x=130, y=400)
        # getting current time automatically
        self.current_time=time.asctime()
        self.id_number_label = Label(master, text="id number",font=("Verdana Bold",10), bg="oldlace").place(x=20, y=450)
        self.id_number_entry = ttk.Entry(master,width=25)
        self.id_number_entry.place(x=130, y=450)
        # id type combo
        self.id_types_list=["Citizenship","driving License","Student Card"]
        self.id_type_label = Label(master, text="id type",font=("Verdana Bold",10), bg="oldlace").place(x=20, y=500)
        self.id_type_combo = Combobox(master, values=self.id_types_list,width=22,state="readonly")  # state prevent change in combo value
        self.id_type_combo.set("select")
        self.id_type_combo.place(x=130, y=500)
        # branch combo
        self.branch_list=["Kathmandu","Pokhara","Butwal","Walling","Bharatpur","Mahendranagar"]
        self.branch_label = Label(master, text="branch",font=("Verdana Bold",10), bg="oldlace").place(x=20, y=550)
        self.branch_combo = Combobox(master, values=self.branch_list,width=22,state="readonly")  # state prevent change in combo value
        self.branch_combo.set("select")
        self.branch_combo.place(x=130, y=550)
        # RIGHT input form
        # occupation combo
        self.occupation_list=["Farmer","Student","Businessman","Journalist","Teacher","Doctor","Engineer","Pilot","Driver","Other"]
        self.occupation_type = Label(master, text="occupation",font=("Verdana Bold",10), bg="oldlace").place(x=355, y=60)
        self.occupation_combo = Combobox(master, values=self.occupation_list, width=22)
        self.occupation_combo.set("select/Enter")
        self.occupation_combo.place(x=450, y=60)
        # address section
        self.address = Label(master, text="Address", font=("verdana Bold",14)).place(x=355, y=102)
        self.permanent_address = Label(master, text="permanent ",font=("Verdana Bold",10), bg="oldlace").place(x=355, y=140)
        self.peramnent_address_entry = ttk.Entry(master,width=25)
        self.peramnent_address_entry.place(x=450, y=140)
        self.tem_address= StringVar()
        self.temporary_address = Label(master, text="temporary ",font=("Verdana Bold",10), bg="oldlace").place(x=355, y=170)
        self.temporary_address_entry = ttk.Entry(master, textvariable=self.tem_address,width=25)
        self.temporary_address_entry.place(x=450, y=170)
        # deposit amount
        self.deposit=Label(master,text="Deposit amt",font=("Verdana Bold",10), bg="oldlace").place(x=355,y=205)
        self.deposit_entry=ttk.Entry(master,width=25)
        self.deposit_entry.place(x=450,y=205)
        self.deposit = Label(master, text="Customer Image", font=("verdana Bold",12)).place(x=355, y=240)
        # canvas for photo
        self.rectangle1 = self.canvas1.create_rectangle(390, 270, 590, 470, fill="mint cream")
        # why error here-------------------------------------------------------------------------------------------------------------
        # upload button in order to upload photo(replacing with normal button)
        #self.upload_button_import =PhotoImage(file="upload.png")
        #self.upload_button = Button(master, image=self.upload_button_import, highlightthickness=0, bd=0,command=self.upload_photo)
        #self.upload_button.place(x=450, y=500)
        #self.master=master
        self.directory_info = Label(master, text="image directory",font=("Verdana Bold",10), bg="oldlace").place(x=355, y=480)
        self.image_directory1 = ttk.Entry(master, width=30)
        self.image_directory1.place(x=480, y=480)
        #self.image_format = Label(master, text="format", font=("Verdana Bold",10), fg="blue2").place(x=380,y=510)                                                                                                         y=510)
        self.user_message = Label(master, text="'only jpg and png format is supported'",font=("Verdana Bold",10), bg="oldlace",fg="red").place(x=400, y=510)
        self.upload_button = Button(master, text="upload photo", bg="blue1",fg="white",font=("verdana",14),command=self.upload_photo)
        self.upload_button.place(x=450, y=550)
        self.master=master
        #why error here----------------------------------------------------------------------------
        # register account  button(replacing with normal button)
        #self.register_button_import = PhotoImage(file="register-now.png")
        #self.register_button = Button(master, image=self.register_button_import, highlightthickness=0, bd=0,command=self.get_savedinfo)
        #self.register_button.place(x=300, y=625)
        self.register_button = Button(master, text="register now", bg="blue1",fg="white",font=("verdana",14),command=self.get_register_and_savedinfo)
        self.register_button.place(x=300, y=625)


    def get_register_and_savedinfo(self,event=""):
        self.a=self.name_entry.get().title()
        print(self.a)
        self.b=self.father_entry.get().title()
        print(self.b)
        self.c= self.mother_entry .get().title()
        print(self.c)
        self.d=self.sex_combo .get()
        print(self.d)
        self.e= self.year_combo.get()
        print(self.e)
        self.f= self.month_combo.get()
        print(self.f)
        self.g= self.day_combo.get()
        print(self.g)
        # adding all dates together
        self.date=self.e+"-"+self.f+"-"+self.g
        print(self.date)
        self.h= self.age_combo.get()
        print(self.h)
        self.i=self.mobile_number_entry.get()
        print(self.i)
        self.j=self.account_type_combo.get()
        print(self.j)
        self.k= self.id_number_entry .get()
        print(self.k)
        self.l=self.id_type_combo.get()
        print(self.l)
        self.m=self.occupation_combo.get()
        print(self.m)
        self.n=self.peramnent_address_entry .get()
        print(self.n)
        self.o=self.temporary_address_entry.get()
        print(self.o)
        self.p=self.deposit_entry.get()
        print(self.p)
        self.q = self.current_time
        print(self.q)
        self.r=self.branch_combo.get()
        print(self.r)
        self.created_by="Netra Prasad Neupane"
        # getting image directory
        self.image_directory=self.image_directory1.get()
        self.image_directory=str(self.image_directory)
        self.directory_store=""
        # converting to compatible directory
        for self.char in self.image_directory:
            if(self.char=="\\"):
                self.directory_store=self.directory_store+"/"
            else:
                self.directory_store=self.directory_store+self.char
        print(self.directory_store)
        self.register_accouont = mysql.connector.connect(
            user="root",
            host="localhost",
            passwd="",
            database="yvd_database",
        )
        self.customer_account_register=self.register_accouont.cursor()
        self.sql_input = "INSERT INTO customer_data(ac_holder_name,f_name,m_name,sex,dob,age,mobile_no,account_type,id_number,id_type,occupation,per_address,tem_address,current_amount,image_directory,created_by,date_account_open,branch) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.append_record = (self.a,self.b,self.c,self.d,self.date,self.h,self.i,self.j,self.k,self.l,self.m,self.n,self.o,self.p,self.image_directory,self.created_by,self.q,self.r)
        self.customer_account_register.execute(self.sql_input, self.append_record)
        self.register_accouont.commit()

        # Here self.master is our window inside funcion get_savedinfo()
        self.print_name = Label(self.master, text="Your account created succesfully and is ", font=("Verdana Bold",18),fg="blue2",bg="thistle2").place(x=740, y=10)
        self.font1="helvetica Bold ",14

        # right display information
        self.customer_account_register.execute("SELECT * FROM customer_data where Ac_holder_name LIKE %s", (self.a,))
        self.result=self.customer_account_register.fetchall()
        self.count=self.customer_account_register.rowcount
        for self.data in self.result:
            self.name=self.data[0]
            self.fname=self.data[1]
            self.mname = self.data[2]
            self.sex= self.data[3]
            self.dob = self.data[4]
            self.age = self.data[5]
            self.mob = self.data[6]
            self.acc_type = self.data[7]
            self.id_nm = self.data[8]
            self.id_tp = self.data[9]
            self.occup = self.data[10]
            self.per = self.data[11]
            self.tem = self.data[12]
            self.dao= self.data[17]
            self.ca = self.data[13]
            self.img_dir = self.data[14]
            self.account_num=self.data[15]
            self.cr_by = self.data[16]
            self.br=self.data[18]

        self.name_label = Label(self.master, text="Name",fg="green",bg="thistle2",font=self.font1).place(x=700, y=80)
        self.name_print = Label(self.master, text= self.name, fg="green", bg="thistle2",font=self.font1).place(x=840, y=80)
        self.father_name_label = Label(self.master, text="Father name", fg="green",font=self.font1,bg="thistle2").place(x=700, y=130)
        self.father_name_print = Label(self.master, text=self.fname, fg="green", bg="thistle2", font=self.font1).place(x=840, y=130)
        self.mother_name_label = Label(self.master, text="Mother name", fg="green",font=self.font1,bg="thistle2").place(x=700, y=180)
        self.mother_name_print= Label(self.master, text=self.mname, fg="green", font=self.font1,bg="thistle2").place(x=840, y=180)
        self.sex_label = Label(self.master, text="Mother name", fg="green",font=self.font1,bg="thistle2").place(x=700, y=230)
        self.sex_print = Label(self.master, text= self.sex,font=self.font1,bg="thistle2").place(x=840, y=230)
        self.dob_label = Label(self.master, text="Date of birth", fg="green",font=self.font1,bg="thistle2").place(x=700, y=280)
        self.dob_label_print = Label(self.master, text=self.dob,font=self.font1, bg="thistle2").place(x=840, y=280)
        self.age_label = Label(self.master, text="age", fg="green",font=self.font1,bg="thistle2").place(x=700, y=320)
        self.age_print= Label(self.master, text=self.age,font=self.font1,bg="thistle2").place(x=840, y=320)
        self.mobile_number_label1 = Label(self.master, text="mobile number", fg="green",font=self.font1,bg="thistle2").place(x=700, y=380)
        self.mobile_number_print = Label(self.master, text=self.mob,font=self.font1,bg="thistle2").place(x=840, y=380)
        self.account_type_label = Label(self.master, text="account type", fg="green",font=self.font1,bg="thistle2").place(x=700, y=430)
        self.account_type_print = Label(self.master, text=self.acc_type,font=self.font1,bg="thistle2").place(x=840, y=430)
        self.id_number_label = Label(self.master, text="id number", fg="green",font= self.font1,bg="thistle2").place(x=700, y=480)
        self.id_num_print = Label(self.master, text=self.id_nm,font=self.font1, bg="thistle2").place(x=840, y=480)
        self.id_type_label = Label(self.master, text="id type", fg="green",font= self.font1,bg="thistle2").place(x=700, y=530)
        self.id_type_display = Label(self.master, text=self.id_tp,font=self.font1, bg="thistle2").place(x=840,y=530)
        self.occupation_label = Label(self.master, text="Ocuupation", fg="green", font=self.font1, bg="thistle2").place(x=700,y=580)
        self.occupation_print = Label(self.master, text=self.occup, font=self.font1, bg="thistle2").place(x=840,y=580)
        self.branch_label = Label(self.master, text="Branch", fg="green", font=self.font1, bg="thistle2").place(x=700,y=620)
        self.branch_print = Label(self.master, text=self.r, font=self.font1, bg="thistle2").place(x=840,y=620)
        self.account_number_label = Label(self.master, text="Account number", fg="green", font=self.font1, bg="thistle2").place(x=700,y=660)
        self.account_number_print = Label(self.master, text=self.account_num, font=self.font1, bg="thistle2").place(x=840,y=660)
        self.print_address = Label(self.master, text="Address", fg="green",font= self.font1,bg="thistle2").place(x=1000, y=380)
        self.per_address_label = Label(self.master, text="permanent", fg="green",font= self.font1,bg="thistle2").place(x=1000, y=430)
        self.per_address_print= Label(self.master,text=self.per, font=self.font1, bg="thistle2").place(x=1200, y=430)
        self.tem_address_display= Label(self.master, text="Temporary", fg="green",font= self.font1,bg="thistle2").place(x=1000, y=480)
        self.tem_address_print = Label(self.master, text=self.tem, font=self.font1, bg="thistle2").place(x=1200,y=480)
        self.date_open_display= Label(self.master, text="date of Ac creation",font= self.font1,fg="green",bg="thistle2").place(x=1000, y=530)
        self.date_open_print = Label(self.master, text=self.dao, font=self.font1,bg="thistle2").place(x=1200, y=530)
        self.current_amount_display = Label(self.master, text="Current balance", fg="green",font= self.font1,bg="thistle2").place(x=1000, y=580)
        self.current_amount_print = Label(self.master, text=self.ca, font=self.font1, bg="thistle2").place(x=1200, y=580)
        self.created_by_display = Label(self.master, text="Created by", fg="green",font= self.font1,bg="thistle2").place(x=1000, y=630)
        self.created_by_print = Label(self.master, text=self.cr_by, font=self.font1, bg="thistle2").place(x=1200, y=630)
        # canvas for photo
        self.rectangle2 = self.canvas2.create_rectangle(450, 120, 650, 320, outline="green")
        self.created_by_print = Label(self.canvas2, text=self.img_dir , fg="green", font=self.font1, bg="thistle2").place(x=460, y=190)


        # if register perform succesfully then creating  statement table here
        user_name1 = str(self.name)
        user_account1= str(self.account_num)
        user_name1= user_name1.lower()
        store_user1 = ""
        for var in user_name1:
            if (var.isspace() == True):
                store_user1 = store_user1 + "_"
            else:
                store_user1 = store_user1 + var

        store_user1 = store_user1 + "_" + user_account1
        print(store_user1)
        opern="Acoount register"
        trs_amt="______________"
        cur_balance=str(self.ca)+"(deposit)"
        per_by="self"
        t_id=user_account1+"0000"
        t_id=int(t_id)
        query_statement = """CREATE TABLE  %s(date_and_time  VARCHAR(255), operation  VARCHAR(255),amount  VARCHAR(255),performed_by  VARCHAR(255),transfer_to  VARCHAR(255),branch  VARCHAR(255),issued_by  VARCHAR(255),transjection_id  BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY)""" % (store_user1)
        self.customer_account_register.execute(query_statement)
        #self.customer_account_register.execute("CREATE TABLE   %s(date_and_time  VARCHAR(255), operation  VARCHAR(255),amount  VARCHAR(255),performed_by  VARCHAR(255),transfer_to  VARCHAR(255),branch  VARCHAR(255),issued_by  VARCHAR(255),transjection_id  NOT NULL AUTO_INCREMENT,PRIMARY KEY(transjection_id))",(store_user1,))

        #inserting register history inorder to fixed transjection id
        register_insert_statement = " INSERT INTO " + store_user1 + " ( date_and_time,operation,amount,performed_by,transfer_to,branch,issued_by,transjection_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
        register_record_statement = (self.dao, opern,cur_balance,per_by, trs_amt, self.br,self.cr_by,t_id)
        self.customer_account_register.execute(register_insert_statement, register_record_statement)
        self.register_accouont.commit()
        self.customer_account_register.close()
        self.register_accouont.close()


    def upload_photo(self,event=""):
        # inorder to upload image
        from PIL import Image, ImageTk
        # use self.master as window
        self.image_directory1 = self.image_directory.get()
        self.image_directory2 = str(self.image_directory1)
        self.directory_store = ""
        # converting to compatible directory
        for self.char in self.image_directory2:
            if (self.char == "\\"):
                self.directory_store = self.directory_store + "/"
            else:
                self.directory_store = self.directory_store + self.char
        print(self.directory_store)
        self.path =self.directory_store
        self.image = Image.open(self.path)
        self.img = self.image.resize((200, 200), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(self.img)
        self.label1 = ttk.Label(self.master, image=self.image1)
        self.label1.self.img=self.image
        self.label1.place(x=390, y=270)




def register_main(event=""):
    window_register=Tk()
    window_register.title("Youth Voice Nepal -Register customer Control System")
    # to get full window
    width = window_register.winfo_screenwidth()
    height = window_register.winfo_screenheight()
    window_register.geometry("%dx%d" % (width, height))
    # window.resizable(False,False)  # used for not resizable window
    # or window.resizable(0,0)
    window_register.resizable(True, True)
    # icon on top
    # why error here-------------------------------------------------------------------------------------
    #icon_image2 = Image("photo", file="3.ico")
    #window_register.call('wm', 'iconphoto', window_register._w, icon_image2)
    frame = Frame(window_register)
    frame.pack()
    perform_register=register(window_register)
    window_register.mainloop()


class operations_manager:
    def __init__(self,master):
        self.master=master
        # left canvas
        self.canvas1= Canvas(master, width=420, height=730, bg="orchid")
        self.register_staff1 = Button(master, text="Register Staff", font=("Gadugi", 22), bg="#C0C0C0", fg="midnightblue",width=24)
        # binding register button
        #self.register_staff1.bind("<Return>",register_staff_main)
        self.register_staff1.place(x=15, y=20)
        self.register1 = Button(master, text="Register Customer", font=("Gadugi", 22), bg="white", fg="midnightblue",width=24,command=register_main)
        # binding register button
        self.register1.bind("<Return>",register_main)
        self.register1.place(x=15, y=95)
        self.withdraw1 = Button(master, text="Withdraw", font=("Gadugi", 22), bg="light pink",fg="midnightblue", width=24,command=withdraw_main)
        # binding withdraw button
        self.register1.bind("<Return>", withdraw_main)
        self.withdraw1.place(x=15, y=170)
        self.deposit1 = Button(master, text="Deposit", font=("Gadugi", 22), bg="aquamarine",width=24,command=deposit_main)
        self.deposit1.bind("<Return>",deposit_main)
        self.deposit1.place(x=15, y=245)
        self.transfer1 = Button(master, text="Transfer", font=("Gadugi", 22), bg="khaki1",fg="midnightblue", width=24,command=transfer_main)
        self.transfer1.bind("<Return>", transfer_main)
        self.transfer1.place(x=15, y=320)
        self.loan = Button(master, text="Get loan", font=("Gadugi", 22), bg="#C0C0C0",width=24).place(x=15, y=395)
        self.edit_update = Button(master, text="Update/Edit ", font=("Gadugi", 22), bg="aquamarine",width=24,command=edit_main)
        # binding edit button
        self.edit_update.bind("<Return>",edit_main)
        self.edit_update.place(x=15, y=470)
        self.delete_button = Button(master, text="Acc Delete", font=("Gadugi", 22), bg="#C0C0C0",width=24,command=delete_main)
        # binding detete button
        self.delete_button.bind("<Return>",delete_main)
        self.delete_button.place(x=15, y=545)
        self.canvas1.pack(fill=Y,side=LEFT,anchor=W)
        self.statement = Button(master, text="   Statements  ", font=("Gadugi", 22), bg="light pink",width=24,command=statement_main)
        #self.statement.bind("<Return>",statement_main)
        self.statement.place(x=15, y=620)
        self.canvas1.pack(fill=Y, side=LEFT, anchor=W)
        # Canvas for search on right
        self.canvas2 = Canvas(master, width=935, height=200, bg="OliveDrab2")
        self.welcome = Label(master, text="Welcome to Youth Voice Nepal- Operation Platform",font=("Verdana Bold", 23),bg="OliveDrab2",fg="black").place(x=450, y=10)
        self.search = Label(master, text=" Search   ", font=("Verdana Bold", 35), bg="OliveDrab2", fg="blue").place(x=540, y=75)
        self.search_types = ("Name", "Account number", "Address(pmt)", "Mobile number", "ID number")
        self.combo = Combobox(master, values=self.search_types, width=12, font=("Arial", 20),state="readonly")
        self.combo.set("Search by")
        self.combo.place(x=775, y=90)
        self.entry = ttk.Entry(master, width=20, font=("Arial", 20))
        self.entry.bind("<Return>",self.display_request_search)
        self.entry.place(x=978,y=90)
        self.canvas2.pack(side=RIGHT,anchor=N,expand=TRUE)
        #self.search_button=Button(master,text="search",fg="white",bg="blue2",width=15)
        #self.search_button.bind("<Return>",self.display_request_search)
        #self.search_button.place(x=1200,y=150)

    def display_request_search(self,event=""):
            self.canvas3 = Canvas(self.master, width=870, height=440, bg="skyblue1")
            search_value = self.entry.get().title()
            print(search_value)
            combo_input = self.combo.get()
            print(combo_input)
            search_value = '%' + search_value + '%'
            # for name search
            if (combo_input == "Name" or combo_input=="Search by"):
                self.search_accouont = mysql.connector.connect(
                    user="root",
                    host="localhost",
                    passwd="",
                    database="yvd_database",
                )
                self.search_cursor = self.search_accouont.cursor()
                self.search_cursor.execute("SELECT * FROM customer_data where ac_holder_name LIKE %s", (search_value,))
                result = self.search_cursor.fetchall()
                row_num = self.search_cursor.rowcount
                print(row_num)
                count = 1
                a = []
                for db in result:
                    # inorder to format name in single index
                    user_var2 = db[0]
                    store_user2 = ""
                    for var2 in user_var2:
                        if (var2.isspace() == True):
                            store_user2 = store_user2 + "_"
                        else:
                            store_user2 = store_user2 + var2
                    # why not formatting in listbox---------------------------------------------------------------------------------------------------------------------
                    search_str = '{0:45}{1:20}{2:20}{3:20}'.format(store_user2, str(db[15]), str(db[4]), str(db[6]))
                    # a.insert(count, str(db[0])+"  "+str(db[15])+"  "+ str(db[4])+"  "+str(db[6]))
                    a.insert(count, search_str)
                    count = count + 1
                print(a)
                self.print_search_listbox1(count,a,row_num)

            # for account number search
            if (combo_input == "Account number"):
                self.search_accouont = mysql.connector.connect(
                    user="root",
                    host="localhost",
                    passwd="",
                    database="yvd_database",
                )
                self.search_cursor = self.search_accouont.cursor()
                self.search_cursor.execute("SELECT * FROM customer_data where account_num LIKE %s", (search_value,))
                result = self.search_cursor.fetchall()
                row_num = self.search_cursor.rowcount
                print(row_num)
                count = 1
                a = []
                for db in result:
                    # inorder to format name in single index
                    user_var2 = db[0]
                    store_user2 = ""
                    for var2 in user_var2:
                        if (var2.isspace() == True):
                            store_user2 = store_user2 + "_"
                        else:
                            store_user2 = store_user2 + var2
                    # why not formatting in listbox---------------------------------------------------------------------------------------------------------------------
                    search_str = '{0:45}{1:20}{2:20}{3:20}'.format(store_user2, str(db[15]), str(db[4]), str(db[6]))
                    # a.insert(count, str(db[0])+"  "+str(db[15])+"  "+ str(db[4])+"  "+str(db[6]))
                    a.insert(count, search_str)
                    count = count + 1
                print(a)
                self.print_search_listbox1(count,a,row_num)

            # search for address
            if (combo_input == "Address(pmt)"):
                self.search_accouont = mysql.connector.connect(
                    user="root",
                    host="localhost",
                    passwd="",
                    database="yvd_database",
                )
                self.search_cursor = self.search_accouont.cursor()
                self.search_cursor.execute("SELECT * FROM customer_data where per_address LIKE %s", (search_value,))
                result = self.search_cursor.fetchall()
                row_num = self.search_cursor.rowcount
                print(row_num)
                count = 1
                a = []
                for db in result:
                    # inorder to format name in single index
                    user_var2 = db[0]
                    store_user2 = ""
                    for var2 in user_var2:
                        if (var2.isspace() == True):
                            store_user2 = store_user2 + "_"
                        else:
                            store_user2 = store_user2 + var2
                    # why not formatting in listbox---------------------------------------------------------------------------------------------------------------------
                    search_str = '{0:45}{1:20}{2:20}{3:20}'.format(store_user2, str(db[15]), str(db[4]), str(db[6]))
                    # a.insert(count, str(db[0])+"  "+str(db[15])+"  "+ str(db[4])+"  "+str(db[6]))
                    a.insert(count, search_str)
                    count = count + 1
                print(a)
                self.print_search_listbox1(count,a,row_num)

            # search for mobile number
            if (combo_input == "Mobile number"):
                self.search_accouont = mysql.connector.connect(
                    user="root",
                    host="localhost",
                    passwd="",
                    database="yvd_database",
                )
                self.search_cursor = self.search_accouont.cursor()
                self.search_cursor.execute("SELECT * FROM customer_data where mobile_no LIKE %s", (search_value,))
                result = self.search_cursor.fetchall()
                row_num = self.search_cursor.rowcount
                print(row_num)
                count = 1
                a = []
                for db in result:
                    # inorder to format name in single index
                    user_var2 = db[0]
                    store_user2 = ""
                    for var2 in user_var2:
                        if (var2.isspace() == True):
                            store_user2 = store_user2 + "_"
                        else:
                            store_user2 = store_user2 + var2
                    # why not formatting in listbox---------------------------------------------------------------------------------------------------------------------
                    search_str = '{0:45}{1:20}{2:20}{3:20}'.format(store_user2, str(db[15]), str(db[4]), str(db[6]))
                    # a.insert(count, str(db[0])+"  "+str(db[15])+"  "+ str(db[4])+"  "+str(db[6]))
                    a.insert(count, search_str)
                    count = count + 1
                print(a)
                self.print_search_listbox1(count,a,row_num)

            # search by id number
            if (combo_input == "ID number"):
                self.search_accouont = mysql.connector.connect(
                    user="root",
                    host="localhost",
                    passwd="",
                    database="yvd_database",
                )
                self.search_cursor = self.search_accouont.cursor()
                self.search_cursor.execute("SELECT * FROM customer_data where id_number LIKE %s", (search_value,))
                result = self.search_cursor.fetchall()
                row_num = self.search_cursor.rowcount
                print(row_num)
                count = 1
                a = []
                for db in result:
                    # inorder to format name in single index
                    user_var2 = db[0]
                    store_user2 = ""
                    for var2 in user_var2:
                        if (var2.isspace() == True):
                            store_user2 = store_user2 + "_"
                        else:
                            store_user2 = store_user2 + var2
                    # why not formatting in listbox---------------------------------------------------------------------------------------------------------------------
                    search_str = '{0:45}{1:20}{2:20}{3:20}'.format(store_user2, str(db[15]), str(db[4]), str(db[6]))
                    # a.insert(count, str(db[0])+"  "+str(db[15])+"  "+ str(db[4])+"  "+str(db[6]))
                    a.insert(count, search_str)
                    count = count + 1
                print(a)
                self.print_search_listbox1(count,a,row_num)

    def print_search_listbox1(self,count1,a1,row_num1):
        cnt = 1
        bottomframe = Frame(self.canvas3, height=450, width=890, highlightcolor="red", highlightthickness=1)
        scroll_v = Scrollbar(self.master)
        scroll_v.pack(side=RIGHT, fill=Y)
        scroll_h = Scrollbar(self.master, orient=HORIZONTAL)
        scroll_h.pack(side=BOTTOM, fill=Y)

        self.listbox1 = Listbox(bottomframe, width=145, height=26, selectmode=BROWSE,
                                yscrollcommand=scroll_v.set,
                                xscrollcommand=scroll_h.set)  # select mode includes: BROWSE,SINGLE,MULTIPLE
        while (cnt <= row_num1):
            self.listbox1.insert(count1, a1[cnt - 1])
            self.listbox1.bind("<<ListboxSelect>>", self.get_selection_name1)
            cnt = cnt + 1
        self.listbox1.place(x=10, y=10)
        scroll_v.config(command=self.listbox1.yview)
        scroll_h.config(command=self.listbox1.xview)

        # button = Button(window, text="select", command=get_message, fg="blue").place(x=120, y=110)
        bottomframe.pack(side=RIGHT, anchor=S, padx=20, pady=20)

        self.canvas3.place(x=425, y=205)

    def get_selection_name1(self,event=""):
        self.font5 = "Verdana Bold", 12
        self.font6="Verdana",12
        clicked_item1=self.listbox1.curselection()
        for item1 in clicked_item1:
            a1=self.listbox1.get(item1)
        print(a1)

        listbox_selected_info=a1.split()
        print(listbox_selected_info)
        name_cs=listbox_selected_info[0]
        account_cs=listbox_selected_info[1]
        print(name_cs)
        print(account_cs)
        store_name_search= ""
        for var3 in name_cs:
            if (var3 == "_"):
                store_name_search = store_name_search + " "
            else:
                store_name_search = store_name_search + var3
        print(store_name_search)
        self.display_for_name_search1(store_name_search,account_cs)


    def display_for_name_search1(self,store_name_search4,account_number4):

        window_search_display = Tk()
        window_search_display.title("Youth Voice Nepal -information display section")
        # to get full window
        width1 = window_search_display.winfo_screenwidth()
        height1 = window_search_display.winfo_screenheight()
        window_search_display.geometry("%dx%d" % (width1, height1))
        # window.resizable(False,False)  # used for not resizable window
        # or window.resizable(0,0)
        window_search_display.resizable(True, True)
        # icon on top
        # icon_image = Image("photo", file="1.ico")
        # window_loan.call('wm', 'iconphoto', window_loan._w, icon_image)
        frame = Frame(window_search_display)
        frame.pack()

        self.canvas11 = Canvas(window_search_display, width=680, bg="oldlace")
        self.canvas11.pack(fill=Y, side=LEFT, anchor=W)
        self.canvas12 = Canvas(window_search_display, width=680, bg="azure2")
        self.canvas12.pack(fill=Y, side=RIGHT, anchor=W)

        sql_query_display = """select * from customer_data where ac_holder_name=%s and account_num=%s"""
        query_record = (store_name_search4, account_number4,)
        self.search_cursor.execute(sql_query_display, query_record)
        get_store_information = self.search_cursor.fetchall()
        for self.data4 in get_store_information:
            name4 = self.data4[0]
            self.fname4 = self.data4[1]
            self.mname4 = self.data4[2]
            self.sex4 = self.data4[3]
            self.dob4 = self.data4[4]
            self.age4 = self.data4[5]
            self.mob4 = self.data4[6]
            self.acc_type4 = self.data4[7]
            self.id_nm4 = self.data4[8]
            self.id_tp4 = self.data4[9]
            self.occup4 = self.data4[10]
            self.per4 = self.data4[11]
            self.tem4 = self.data4[12]
            self.dao4 = self.data4[17]
            self.ca4 = self.data4[13]
            self.img_dir4 = self.data4[14]
            self.account_num4 = self.data4[15]
            self.cr_by4 = self.data4[16]
            self.br4 = self.data4[18]

        self.name_label = Label(window_search_display, text="Name", fg="blue2", bg="oldlace", font=self.font5).place(
            x=100, y=80)
        self.name_print = Label(window_search_display, text=name4, bg="oldlace", font=self.font6).place(x=300,
                                                                                                             y=80)
        self.father_name_label = Label(window_search_display, text="Father name", fg="blue2", font=self.font5,
                                       bg="oldlace").place(x=100, y=130)
        self.father_name_print = Label(window_search_display, text=self.fname4, bg="oldlace", font=self.font6).place(
            x=300, y=130)
        self.mother_name_label = Label(window_search_display, text="Mother name", fg="blue2", font=self.font5,
                                       bg="oldlace").place(x=100, y=180)
        self.mother_name_print = Label(window_search_display, text=self.mname4, font=self.font6, bg="oldlace").place(
            x=300, y=180)
        self.sex_label = Label(window_search_display, text="Sex", fg="blue2", font=self.font5, bg="oldlace").place(
            x=100,
            y=230)
        self.sex_print = Label(window_search_display, text=self.sex4, font=self.font6, bg="oldlace").place(x=300, y=230)
        self.dob_label = Label(window_search_display, text="Date of birth", fg="blue2", font=self.font5,
                               bg="oldlace").place(
            x=100, y=280)
        self.dob_label_print = Label(window_search_display, text=self.dob4, font=self.font6, bg="oldlace").place(x=300,
                                                                                                                 y=280)
        self.age_label = Label(window_search_display, text="age", fg="blue2", font=self.font5, bg="oldlace").place(
            x=100, y=320)
        self.age_print = Label(window_search_display, text=self.age4, font=self.font6, bg="oldlace").place(x=300, y=320)
        self.mobile_number_label1 = Label(window_search_display, text="mobile number", fg="blue2", font=self.font5,
                                          bg="oldlace").place(x=100, y=380)
        self.mobile_number_print = Label(window_search_display, text=self.mob4, font=self.font6, bg="oldlace").place(
            x=300, y=380)
        self.account_type_label = Label(window_search_display, text="account type", fg="blue2", font=self.font5,
                                        bg="oldlace").place(x=100, y=430)
        self.account_type_print = Label(window_search_display, text=self.acc_type4, font=self.font6,
                                        bg="oldlace").place(x=300,
                                                            y=430)
        self.id_number_label = Label(window_search_display, text="id number", fg="blue2", font=self.font5,
                                     bg="oldlace").place(
            x=100, y=480)
        self.id_num_print = Label(window_search_display, text=self.id_nm4, font=self.font6, bg="oldlace").place(x=300,
                                                                                                                y=480)
        self.id_type_label = Label(window_search_display, text="id type", fg="blue2", font=self.font5,
                                   bg="oldlace").place(x=100,
                                                       y=530)
        self.id_type_display = Label(window_search_display, text=self.id_tp4, font=self.font6, bg="oldlace").place(
            x=300, y=530)
        self.occupation_label = Label(window_search_display, text="Ocuupation", fg="blue2", font=self.font5,
                                      bg="oldlace").place(
            x=100, y=580)
        self.occupation_print = Label(window_search_display, text=self.occup4, font=self.font6, bg="oldlace").place(
            x=300, y=580)
        self.branch_label = Label(window_search_display, text="Branch", fg="blue2", font=self.font5,
                                  bg="oldlace").place(x=100,
                                                      y=620)
        self.branch_print = Label(window_search_display, text=self.br4, font=self.font6, bg="oldlace").place(x=300,
                                                                                                             y=620)
        self.account_number_label = Label(window_search_display, text="Account number", fg="blue2", font=self.font5,
                                          bg="azure2").place(x=700, y=330)
        self.account_number_print = Label(window_search_display, text=self.account_num4, font=self.font6,
                                          bg="azure2").place(
            x=900, y=330)
        self.print_address = Label(window_search_display, text="Address", fg="blue2", font=("Verdana Bold", 14)).place(
            x=700, y=380)
        self.per_address_label = Label(window_search_display, text="permanent", fg="blue2", font=self.font5,
                                       bg="azure2").place(
            x=700, y=430)
        self.per_address_print = Label(window_search_display, text=self.per4, font=self.font6, bg="azure2").place(x=900,
                                                                                                                  y=430)
        self.tem_address_display = Label(window_search_display, text="Temporary", fg="blue2", font=self.font5,
                                         bg="azure2").place(x=700, y=480)
        self.tem_address_print = Label(window_search_display, text=self.tem4, font=self.font6, bg="azure2").place(x=900,
                                                                                                                  y=480)
        self.date_open_display = Label(window_search_display, text="date of Ac creation", font=self.font5, fg="blue2",
                                       bg="azure2").place(x=700, y=530)
        self.date_open_print = Label(window_search_display, text=self.dao4, font=self.font6, bg="azure2").place(x=900,
                                                                                                                y=530)
        self.current_amount_display = Label(window_search_display, text="Current balance", fg="blue2", font=self.font5,
                                            bg="azure2").place(x=700, y=580)
        self.current_amount_print = Label(window_search_display, text=self.ca4, font=self.font6, bg="azure2").place(
            x=900, y=580)
        self.created_by_display = Label(window_search_display, text="Created by", fg="blue2", font=self.font5,
                                        bg="azure2").place(x=700, y=630)
        self.created_by_print = Label(window_search_display, text=self.cr_by4, font=self.font6, bg="azure2").place(
            x=900, y=630)
        # canvas for photo
        self.rectangle12 = self.canvas12.create_rectangle(450, 80, 650, 280, outline="green")
        self.created_by_print = Label(self.canvas12, text=self.img_dir4, fg="green", font=self.font5,
                                      bg="thistle2").place(x=460, y=190)

        window_search_display.mainloop()



def operation_main_manager():
    window_first.destroy()
    window_second_1=Tk()
    window_second_1.title("Youth Voice Nepal -Operation Control System")
    # to get full window
    width = window_second_1.winfo_screenwidth()
    height = window_second_1.winfo_screenheight()
    window_second_1.geometry("%dx%d" % (width, height))
    # window.resizable(False,False)  # used for not resizable window
    # or window.resizable(0,0)
    window_second_1.resizable(True, True)
    # icon on top
    icon_image1 = Image("photo", file="2.ico")
    window_second_1.call('wm', 'iconphoto', window_second_1._w, icon_image1)
    frame = Frame(window_second_1)
    frame.pack()
    perform_operation=operations_manager(window_second_1)
    window_second_1.mainloop()


class operations:
    def __init__(self,master):
        self.master=master
        # left canvas
        self.canvas1= Canvas(master, width=420, height=730, bg="orchid")
        self.register1 = Button(master, text="Register account", font=("Gadugi", 25), bg="white", fg="midnightblue",width=21,command=register_main)
        # binding register button
        self.register1.bind("<Return>",register_main)
        self.register1.place(x=20, y=20)
        self.withdraw1 = Button(master, text="Withdraw", font=("Gadugi", 25), bg="light pink",fg="midnightblue", width=21,command=withdraw_main)
        # binding withdraw button
        self.register1.bind("<Return>", withdraw_main)
        self.withdraw1.place(x=20, y=102)
        self.deposit1 = Button(master, text="Deposit", font=("Gadugi", 25), bg="aquamarine",width=21,command=deposit_main)
        self.deposit1.bind("<Return>",deposit_main)
        self.deposit1.place(x=20, y=184)
        self.transfer1 = Button(master, text="Transfer", font=("Gadugi", 25), bg="khaki1",fg="midnightblue", width=21,command=transfer_main)
        self.transfer1.bind("<Return>", transfer_main)
        self.transfer1.place(x=20, y=266)
        self.loan = Button(master, text="Get loan", font=("Gadugi", 25), bg="#C0C0C0",width=21).place(x=20, y=355)
        self.edit_update = Button(master, text="Update/Edit ", font=("Gadugi", 25), bg="aquamarine",width=21,command=edit_main)
        # binding edit button
        self.edit_update.bind("<Return>",edit_main)
        self.edit_update.place(x=20, y=440)
        self.delete_button = Button(master, text="Acc Delete", font=("Gadugi", 25), bg="#C0C0C0",width=21,command=delete_main)
        # binding detete button
        self.delete_button.bind("<Return>",delete_main)
        self.delete_button.place(x=20, y=525)
        self.canvas1.pack(fill=Y,side=LEFT,anchor=W)
        self.statement = Button(master, text="   Statements  ", font=("Gadugi", 25), bg="light pink",width=21,command=statement_main)
        #self.statement.bind("<Return>",statement_main)
        self.statement.place(x=20, y=610)
        self.canvas1.pack(fill=Y, side=LEFT, anchor=W)
        # Canvas for search on right
        self.canvas2 = Canvas(master, width=935, height=200, bg="OliveDrab2")
        self.welcome = Label(master, text="Welcome to Youth Voice Nepal- Operation Platform",font=("Verdana Bold", 23),bg="OliveDrab2",fg="black").place(x=450, y=10)
        self.search = Label(master, text=" Search   ", font=("Verdana Bold", 35), bg="OliveDrab2", fg="blue").place(x=540, y=75)
        self.search_types = ("Name", "Account number", "Address(pmt)", "Mobile number", "ID number")
        self.combo = Combobox(master, values=self.search_types, width=12, font=("Arial", 20),state="readonly")
        self.combo.set("Search by")
        self.combo.place(x=775, y=90)
        self.entry = ttk.Entry(master, width=20, font=("Arial", 20))
        self.entry.bind("<Return>",self.display_request_search)
        self.entry.place(x=978,y=90)
        self.canvas2.pack(side=RIGHT,anchor=N,expand=TRUE)
        #self.search_button=Button(master,text="search",fg="white",bg="blue2",width=15)
        #self.search_button.bind("<Return>",self.display_request_search)
        #self.search_button.place(x=1200,y=150)

    def display_request_search(self,event=""):
            self.canvas3 = Canvas(self.master, width=870, height=440, bg="skyblue1")
            search_value = self.entry.get().title()
            print(search_value)
            combo_input = self.combo.get()
            print(combo_input)
            search_value = '%' + search_value + '%'
            # for name search
            if (combo_input == "Name"):
                self.search_accouont = mysql.connector.connect(
                    user="root",
                    host="localhost",
                    passwd="",
                    database="yvd_database",
                )
                self.search_cursor = self.search_accouont.cursor()
                self.search_cursor.execute("SELECT * FROM customer_data where ac_holder_name LIKE %s", (search_value,))
                result = self.search_cursor.fetchall()
                row_num = self.search_cursor.rowcount
                print(row_num)
                count = 1
                a = []
                for db in result:
                    # inorder to format name in single index
                    user_var2 = db[0]
                    store_user2 = ""
                    for var2 in user_var2:
                        if (var2.isspace() == True):
                            store_user2 = store_user2 + "_"
                        else:
                            store_user2 = store_user2 + var2
                    # why not formatting in listbox---------------------------------------------------------------------------------------------------------------------
                    search_str = '{0:45}{1:20}{2:20}{3:20}'.format(store_user2, str(db[15]), str(db[4]), str(db[6]))
                    # a.insert(count, str(db[0])+"  "+str(db[15])+"  "+ str(db[4])+"  "+str(db[6]))
                    a.insert(count, search_str)
                    count = count + 1
                print(a)
                self.print_search_listbox(count,a,row_num)

            # for account number search
            if (combo_input == "Account number"):
                self.search_accouont = mysql.connector.connect(
                    user="root",
                    host="localhost",
                    passwd="",
                    database="yvd_database",
                )
                self.search_cursor = self.search_accouont.cursor()
                self.search_cursor.execute("SELECT * FROM customer_data where account_num LIKE %s", (search_value,))
                result = self.search_cursor.fetchall()
                row_num = self.search_cursor.rowcount
                print(row_num)
                count = 1
                a = []
                for db in result:
                    # inorder to format name in single index
                    user_var2 = db[0]
                    store_user2 = ""
                    for var2 in user_var2:
                        if (var2.isspace() == True):
                            store_user2 = store_user2 + "_"
                        else:
                            store_user2 = store_user2 + var2
                    # why not formatting in listbox---------------------------------------------------------------------------------------------------------------------
                    search_str = '{0:45}{1:20}{2:20}{3:20}'.format(store_user2, str(db[15]), str(db[4]), str(db[6]))
                    # a.insert(count, str(db[0])+"  "+str(db[15])+"  "+ str(db[4])+"  "+str(db[6]))
                    a.insert(count, search_str)
                    count = count + 1
                print(a)
                self.print_search_listbox(count,a,row_num)

            # search for address
            if (combo_input == "Address(pmt)"):
                self.search_accouont = mysql.connector.connect(
                    user="root",
                    host="localhost",
                    passwd="",
                    database="yvd_database",
                )
                self.search_cursor = self.search_accouont.cursor()
                self.search_cursor.execute("SELECT * FROM customer_data where per_address LIKE %s", (search_value,))
                result = self.search_cursor.fetchall()
                row_num = self.search_cursor.rowcount
                print(row_num)
                count = 1
                a = []
                for db in result:
                    # inorder to format name in single index
                    user_var2 = db[0]
                    store_user2 = ""
                    for var2 in user_var2:
                        if (var2.isspace() == True):
                            store_user2 = store_user2 + "_"
                        else:
                            store_user2 = store_user2 + var2
                    # why not formatting in listbox---------------------------------------------------------------------------------------------------------------------
                    search_str = '{0:45}{1:20}{2:20}{3:20}'.format(store_user2, str(db[15]), str(db[4]), str(db[6]))
                    # a.insert(count, str(db[0])+"  "+str(db[15])+"  "+ str(db[4])+"  "+str(db[6]))
                    a.insert(count, search_str)
                    count = count + 1
                print(a)
                self.print_search_listbox(count,a,row_num)

            # search for mobile number
            if (combo_input == "Mobile number"):
                self.search_accouont = mysql.connector.connect(
                    user="root",
                    host="localhost",
                    passwd="",
                    database="yvd_database",
                )
                self.search_cursor = self.search_accouont.cursor()
                self.search_cursor.execute("SELECT * FROM customer_data where mobile_no LIKE %s", (search_value,))
                result = self.search_cursor.fetchall()
                row_num = self.search_cursor.rowcount
                print(row_num)
                count = 1
                a = []
                for db in result:
                    # inorder to format name in single index
                    user_var2 = db[0]
                    store_user2 = ""
                    for var2 in user_var2:
                        if (var2.isspace() == True):
                            store_user2 = store_user2 + "_"
                        else:
                            store_user2 = store_user2 + var2
                    # why not formatting in listbox---------------------------------------------------------------------------------------------------------------------
                    search_str = '{0:45}{1:20}{2:20}{3:20}'.format(store_user2, str(db[15]), str(db[4]), str(db[6]))
                    # a.insert(count, str(db[0])+"  "+str(db[15])+"  "+ str(db[4])+"  "+str(db[6]))
                    a.insert(count, search_str)
                    count = count + 1
                print(a)
                self.print_search_listbox(count,a,row_num)

            # search by id number
            if (combo_input == "ID number"):
                self.search_accouont = mysql.connector.connect(
                    user="root",
                    host="localhost",
                    passwd="",
                    database="yvd_database",
                )
                self.search_cursor = self.search_accouont.cursor()
                self.search_cursor.execute("SELECT * FROM customer_data where id_number LIKE %s", (search_value,))
                result = self.search_cursor.fetchall()
                row_num = self.search_cursor.rowcount
                print(row_num)
                count = 1
                a = []
                for db in result:
                    # inorder to format name in single index
                    user_var2 = db[0]
                    store_user2 = ""
                    for var2 in user_var2:
                        if (var2.isspace() == True):
                            store_user2 = store_user2 + "_"
                        else:
                            store_user2 = store_user2 + var2
                    # why not formatting in listbox---------------------------------------------------------------------------------------------------------------------
                    search_str = '{0:45}{1:20}{2:20}{3:20}'.format(store_user2, str(db[15]), str(db[4]), str(db[6]))
                    # a.insert(count, str(db[0])+"  "+str(db[15])+"  "+ str(db[4])+"  "+str(db[6]))
                    a.insert(count, search_str)
                    count = count + 1
                print(a)
                self.print_search_listbox(count,a,row_num)

    def print_search_listbox(self,count1,a1,row_num1):
        cnt = 1
        bottomframe = Frame(self.canvas3, height=450, width=890, highlightcolor="red", highlightthickness=1)
        scroll_v = Scrollbar(self.master)
        scroll_v.pack(side=RIGHT, fill=Y)
        scroll_h = Scrollbar(self.master, orient=HORIZONTAL)
        scroll_h.pack(side=BOTTOM, fill=Y)

        self.listbox1 = Listbox(bottomframe, width=145, height=26, selectmode=BROWSE,
                                yscrollcommand=scroll_v.set,
                                xscrollcommand=scroll_h.set)  # select mode includes: BROWSE,SINGLE,MULTIPLE
        while (cnt <= row_num1):
            self.listbox1.insert(count1, a1[cnt - 1])
            self.listbox1.bind("<<ListboxSelect>>", self.get_selection_name)
            cnt = cnt + 1
        self.listbox1.place(x=10, y=10)
        scroll_v.config(command=self.listbox1.yview)
        scroll_h.config(command=self.listbox1.xview)

        # button = Button(window, text="select", command=get_message, fg="blue").place(x=120, y=110)
        bottomframe.pack(side=RIGHT, anchor=S, padx=20, pady=20)

        self.canvas3.place(x=425, y=205)


    def get_selection_name(self,event=""):
        self.font5 = "Verdana Bold", 12
        self.font6="Verdana",12
        clicked_item1=self.listbox1.curselection()
        for item1 in clicked_item1:
            a1=self.listbox1.get(item1)
        print(a1)

        listbox_selected_info=a1.split()
        print(listbox_selected_info)
        name_cs=listbox_selected_info[0]
        account_cs=listbox_selected_info[1]
        print(name_cs)
        print(account_cs)
        store_name_search= ""
        for var3 in name_cs:
            if (var3 == "_"):
                store_name_search = store_name_search + " "
            else:
                store_name_search = store_name_search + var3
        print(store_name_search)
        self.display_for_name_search(store_name_search,account_cs)


    def display_for_name_search(self,store_name_search4,account_number4):

        window_search_display = Tk()
        window_search_display.title("Youth Voice Nepal -information display section")
        # to get full window
        width1 = window_search_display.winfo_screenwidth()
        height1 = window_search_display.winfo_screenheight()
        window_search_display.geometry("%dx%d" % (width1, height1))
        # window.resizable(False,False)  # used for not resizable window
        # or window.resizable(0,0)
        window_search_display.resizable(True, True)
        # icon on top
        # icon_image = Image("photo", file="1.ico")
        # window_loan.call('wm', 'iconphoto', window_loan._w, icon_image)
        frame = Frame(window_search_display)
        frame.pack()

        self.canvas11 = Canvas(window_search_display, width=680, bg="oldlace")
        self.canvas11.pack(fill=Y, side=LEFT, anchor=W)
        self.canvas12 = Canvas(window_search_display, width=680, bg="azure2")
        self.canvas12.pack(fill=Y, side=RIGHT, anchor=W)

        sql_query_display = """select * from customer_data where ac_holder_name=%s and account_num=%s"""
        query_record = (store_name_search4, account_number4,)
        self.search_cursor.execute(sql_query_display, query_record)
        get_store_information = self.search_cursor.fetchall()
        for self.data4 in get_store_information:
            name4 = self.data4[0]
            self.fname4 = self.data4[1]
            self.mname4 = self.data4[2]
            self.sex4 = self.data4[3]
            self.dob4 = self.data4[4]
            self.age4 = self.data4[5]
            self.mob4 = self.data4[6]
            self.acc_type4 = self.data4[7]
            self.id_nm4 = self.data4[8]
            self.id_tp4 = self.data4[9]
            self.occup4 = self.data4[10]
            self.per4 = self.data4[11]
            self.tem4 = self.data4[12]
            self.dao4 = self.data4[17]
            self.ca4 = self.data4[13]
            self.img_dir4 = self.data4[14]
            self.account_num4 = self.data4[15]
            self.cr_by4 = self.data4[16]
            self.br4 = self.data4[18]

        self.name_label = Label(window_search_display, text="Name", fg="blue2", bg="oldlace", font=self.font5).place(
            x=100, y=80)
        self.name_print = Label(window_search_display, text=name4, bg="oldlace", font=self.font6).place(x=300,
                                                                                                             y=80)
        self.father_name_label = Label(window_search_display, text="Father name", fg="blue2", font=self.font5,
                                       bg="oldlace").place(x=100, y=130)
        self.father_name_print = Label(window_search_display, text=self.fname4, bg="oldlace", font=self.font6).place(
            x=300, y=130)
        self.mother_name_label = Label(window_search_display, text="Mother name", fg="blue2", font=self.font5,
                                       bg="oldlace").place(x=100, y=180)
        self.mother_name_print = Label(window_search_display, text=self.mname4, font=self.font6, bg="oldlace").place(
            x=300, y=180)
        self.sex_label = Label(window_search_display, text="Sex", fg="blue2", font=self.font5, bg="oldlace").place(
            x=100,
            y=230)
        self.sex_print = Label(window_search_display, text=self.sex4, font=self.font6, bg="oldlace").place(x=300, y=230)
        self.dob_label = Label(window_search_display, text="Date of birth", fg="blue2", font=self.font5,
                               bg="oldlace").place(
            x=100, y=280)
        self.dob_label_print = Label(window_search_display, text=self.dob4, font=self.font6, bg="oldlace").place(x=300,
                                                                                                                 y=280)
        self.age_label = Label(window_search_display, text="age", fg="blue2", font=self.font5, bg="oldlace").place(
            x=100, y=320)
        self.age_print = Label(window_search_display, text=self.age4, font=self.font6, bg="oldlace").place(x=300, y=320)
        self.mobile_number_label1 = Label(window_search_display, text="mobile number", fg="blue2", font=self.font5,
                                          bg="oldlace").place(x=100, y=380)
        self.mobile_number_print = Label(window_search_display, text=self.mob4, font=self.font6, bg="oldlace").place(
            x=300, y=380)
        self.account_type_label = Label(window_search_display, text="account type", fg="blue2", font=self.font5,
                                        bg="oldlace").place(x=100, y=430)
        self.account_type_print = Label(window_search_display, text=self.acc_type4, font=self.font6,
                                        bg="oldlace").place(x=300,
                                                            y=430)
        self.id_number_label = Label(window_search_display, text="id number", fg="blue2", font=self.font5,
                                     bg="oldlace").place(
            x=100, y=480)
        self.id_num_print = Label(window_search_display, text=self.id_nm4, font=self.font6, bg="oldlace").place(x=300,
                                                                                                                y=480)
        self.id_type_label = Label(window_search_display, text="id type", fg="blue2", font=self.font5,
                                   bg="oldlace").place(x=100,
                                                       y=530)
        self.id_type_display = Label(window_search_display, text=self.id_tp4, font=self.font6, bg="oldlace").place(
            x=300, y=530)
        self.occupation_label = Label(window_search_display, text="Ocuupation", fg="blue2", font=self.font5,
                                      bg="oldlace").place(
            x=100, y=580)
        self.occupation_print = Label(window_search_display, text=self.occup4, font=self.font6, bg="oldlace").place(
            x=300, y=580)
        self.branch_label = Label(window_search_display, text="Branch", fg="blue2", font=self.font5,
                                  bg="oldlace").place(x=100,
                                                      y=620)
        self.branch_print = Label(window_search_display, text=self.br4, font=self.font6, bg="oldlace").place(x=300,
                                                                                                             y=620)
        self.account_number_label = Label(window_search_display, text="Account number", fg="blue2", font=self.font5,
                                          bg="azure2").place(x=700, y=330)
        self.account_number_print = Label(window_search_display, text=self.account_num4, font=self.font6,
                                          bg="azure2").place(
            x=900, y=330)
        self.print_address = Label(window_search_display, text="Address", fg="blue2", font=("Verdana Bold", 14)).place(
            x=700, y=380)
        self.per_address_label = Label(window_search_display, text="permanent", fg="blue2", font=self.font5,
                                       bg="azure2").place(
            x=700, y=430)
        self.per_address_print = Label(window_search_display, text=self.per4, font=self.font6, bg="azure2").place(x=900,
                                                                                                                  y=430)
        self.tem_address_display = Label(window_search_display, text="Temporary", fg="blue2", font=self.font5,
                                         bg="azure2").place(x=700, y=480)
        self.tem_address_print = Label(window_search_display, text=self.tem4, font=self.font6, bg="azure2").place(x=900,
                                                                                                                  y=480)
        self.date_open_display = Label(window_search_display, text="date of Ac creation", font=self.font5, fg="blue2",
                                       bg="azure2").place(x=700, y=530)
        self.date_open_print = Label(window_search_display, text=self.dao4, font=self.font6, bg="azure2").place(x=900,
                                                                                                                y=530)
        self.current_amount_display = Label(window_search_display, text="Current balance", fg="blue2", font=self.font5,
                                            bg="azure2").place(x=700, y=580)
        self.current_amount_print = Label(window_search_display, text=self.ca4, font=self.font6, bg="azure2").place(
            x=900, y=580)
        self.created_by_display = Label(window_search_display, text="Created by", fg="blue2", font=self.font5,
                                        bg="azure2").place(x=700, y=630)
        self.created_by_print = Label(window_search_display, text=self.cr_by4, font=self.font6, bg="azure2").place(
            x=900, y=630)
        # canvas for photo
        self.rectangle12 = self.canvas12.create_rectangle(450, 80, 650, 280, outline="green")
        self.created_by_print = Label(self.canvas12, text=self.img_dir4, fg="green", font=self.font5,
                                      bg="thistle2").place(x=460, y=190)

        window_search_display.mainloop()





def operation_main():
    window_first.destroy()
    window_second=Tk()
    window_second.title("Youth Voice Nepal -Operation Control System")
    # to get full window
    width = window_second.winfo_screenwidth()
    height = window_second.winfo_screenheight()
    window_second.geometry("%dx%d" % (width, height))
    # window.resizable(False,False)  # used for not resizable window
    # or window.resizable(0,0)
    window_second.resizable(True, True)
    # icon on top
    icon_image1 = Image("photo", file="2.ico")
    window_second.call('wm', 'iconphoto', window_second._w, icon_image1)
    frame = Frame(window_second)
    frame.pack()
    perform_operation=operations(window_second)
    window_second.mainloop()



class login:
    def __init__(self,master):
        self.master=master
        # Right top Canvas
        self.canvas1=Canvas(master,width=910,height=280,bg="#C0C0C0")
        self.canvas1.pack(side=RIGHT,anchor=N,expand=True)
        # Right bottom Canvas
        #self.canvas4 = Canvas(master, width=910, height=150)
        #self.canvas4.pack( side=BOTTOM,anchor=SW)
        # Left Canvas
        self.canvas2 = Canvas(master, width=380, height=700, bg="#90EE90")
        self.canvas2.pack(fill=Y, side=LEFT,expand=True)
        self.canvas3 = Canvas(master, width=70, height=700, bg="purple")
        self.canvas3.pack(fill=Y,side=LEFT,expand="True")
        # right text
        self.label1 = Label(master, text="Welcome to ", font=("Verdana Bold", 35), bg="#C0C0C0",fg="#00008B").place(x=520,y=80)
        self.label2 = Label(master, text="Youth Voice Nepal Bank Limited", font=("Verdana Bold", 30), bg="#C0C0C0",fg="#191970").place(x=580, y=150)
        self.label3 = Label(master, text="Pokhara,Nepal", font=("Arial Bold", 24), bg="#C0C0C0").place(x=880, y=210)
        self.label4 = Label(master,text="Enter the following details appropriately in order to perform banking operation",font=("Calibri Bold", 18), fg="blue2").place(x=500, y=375)
        # first entry username
        self.user_name=StringVar()
        self.labe15 = Label(master, text="Username", font=("Calibri Bold", 18), fg="green").place(x=620,y=450)
        self.entry1 = ttk.Entry(master, font=("Verdana", 14), width=20,textvariable=self.user_name)
        # binding entry1
        self.entry1.bind("<Return>", self.get_login)
        self.entry1.place(x=800, y=450)
        # Second entry password
        self.pass_word=StringVar()
        self.labe6 = Label(master, text="Password", font=("Calibri Bold", 18), fg="green").place(x=620, y=500)
        self.entry2 = ttk.Entry(master, font=("Verdana", 14), width=20, show="*",textvariable=self.pass_word)
        # binding entry 2
        self.entry2.bind("<Return>", self.get_login)
        self.entry2.place(x=800, y=500)
        # position combobox
        self.list_values=["Manager","Teller","Loan officer","Financial Analyst"]
        self.label7 = Label(master,text="Position", font=("Calibri Bold", 18),fg="green").place(x=620, y=543)
        self.combo = Combobox(master,values=self.list_values,width=17,font=("Arial",18),state="readonly")
        self.combo.set("Select")
        # binding the combobox
        self.combo.bind("<Return>",self.get_login)
        self.combo.place(x=800,y=540)
        #self.button1=Button(master,text="  login  ",fg="red",bg="yellow",font=("Calibri Bold",14) ).place(x=770,y=600)
        # inorder to use login button
        self.login_button_import = PhotoImage(file='login2.png')
        self.login_button = Button(master, image=self.login_button_import, bg="#C0C0C0",highlightthickness = 0, bd = 0,command=self.get_login)
        self.login_button.bind("<Return>",self.get_login)
        self.login_button.place(x=1050, y=590)


    # to check wheter the input is true or not
    def get_login(self,event=""):
        global username
        self.username=self.user_name.get()
        username=self.username
        self.password=self.pass_word.get()
        self.position=self.combo.get()
        # connecting to database
        staff_login=mysql.connector.connect(
            user="root",
            host="localhost",
            passwd="",
            database="yvd_database",
        )
        staff_login_cursor=staff_login.cursor()
        staff_login_cursor.execute("SELECT * FROM staff_only")
        fetched_data=staff_login_cursor.fetchall()
        # to count how many row of staff is available in database
        count=staff_login_cursor.rowcount
        flag = True
        # inorder to check using count as variable and to stop using flag
        while(count>0 and flag==True):
        # to fetch data from database
            for data in fetched_data:
                    username = data[2]
                    password = data[3]
                    position = data[6]
                    if(username==self.username and password==self.password and position==self.position):
                         staff_login_cursor.close()
                         staff_login.close()
                         if(self.position=="Manager"):
                             operation_main_manager()
                             break
                         else:
                            operation_main()
                            flag=False
                            break
                    else:
                       count=count-1
                       if(count==0):
                           self.warn_label = Label(self.master, text="username, password or position may be incorrect",font=(" Verdana Bold",16),fg="red")
                           self.warn_label.place(x=680, y=415)
                           staff_login_cursor.close()
                           staff_login.close()



# window first =login window
window_first=Tk()
window_first.title("Youth Voice Nepal -Login Section")
# to get full window
width = window_first.winfo_screenwidth()
height = window_first.winfo_screenheight()
window_first.geometry("%dx%d" % (width, height))
# window.resizable(False,False)  # used for not resizable window
# or window.resizable(0,0)
window_first.resizable(True, True)
# icon on top
icon_image = Image("photo", file="1.ico")
window_first.call('wm', 'iconphoto', window_first._w, icon_image)
frame = Frame(window_first)
frame.pack()
get_login1=login(window_first)
window_first.mainloop()
