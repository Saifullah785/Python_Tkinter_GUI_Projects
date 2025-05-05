from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

#functionality part

def employee_form():
    global back_image
    employee_frame=Frame(window,width=1070,height=567,bg='white')
    employee_frame.place(x=200, y=100)
    heading_Label=Label(employee_frame,text='Manage Employee Detail',font=('times new roman',16,'bold'),bg='#0f4d7d',fg='white')
    heading_Label.place(x=0,y=0,relwidth=1)

    # creating back button
    back_image = PhotoImage(file='E:/python projects/inventory management system/images/backbutton.png')


    #1. #####################################################################
    # creating top Frame

    top_Frame=Frame(employee_frame,bg='white')
    top_Frame.place(x=0,y=40,relwidth=1,height=235)

    back_button=Button(top_Frame,image=back_image,bd=0,cursor='hand2',command=lambda:employee_frame.place_forget())
    back_button.place(x=10,y=0)

    search_frame=Frame(top_Frame,bg='white')
    search_frame.pack()

    search_combobox =ttk.Combobox(search_frame,values=('ID','Name','Email'),font=('times new roman',12),state='readonly')
    search_combobox.set('Search By')
    search_combobox.grid(row=0,column=0,padx=20)

    search_entry=Entry(search_frame,font=('times new roman',12),bg='lightyellow')
    search_entry.grid(row=0,column=1)

    search_button =Button(search_frame,text='Search',font=("times new roman",12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    search_button.grid(row=0,column=2,padx=20)

    show_button = Button(search_frame,text='Show All',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    show_button.grid(row=0,column=3 )
    horizontal_scrollbar=Scrollbar(top_Frame,orient=HORIZONTAL)
    vertical_scrollbar=Scrollbar(top_Frame,orient=VERTICAL)

    #2.  ############################################################
    
    #creating Treeview section for searching all employee detail

    employee_treeview =ttk.Treeview(top_Frame,columns=('empid','name','email','gender','dob',
                                                       'contact','employement_type','education',
                                                       'work_shift','address','obj','salary','usertype'),show='headings',
                                    yscrollcommand=vertical_scrollbar.set,xscrollcommand=horizontal_scrollbar.set)
    horizontal_scrollbar.pack(side=BOTTOM,fill=X)
    vertical_scrollbar.pack(side=RIGHT,fill=Y,pady=(10,0))
    horizontal_scrollbar.config(command=employee_treeview.xview)
    vertical_scrollbar.config(command=employee_treeview.yview)


    employee_treeview.pack(pady=(10,0))

    employee_treeview.heading('empid',text='EmpId')
    employee_treeview.heading('name',text='Name')
    employee_treeview.heading('email',text='Email')
    employee_treeview.heading('gender',text='Gender')
    employee_treeview.heading('dob',text='Date of Birth')
    employee_treeview.heading('contact',text='Contact')
    employee_treeview.heading('employement_type',text='Employement Type')
    employee_treeview.heading('education',text='Education')
    employee_treeview.heading('work_shift',text='Work Shift')
    employee_treeview.heading('address',text='Address')
    employee_treeview.heading('obj',text='Date of Joining')
    employee_treeview.heading('salary',text='Salary')
    employee_treeview.heading('usertype',text='User Type')

    employee_treeview.column('empid',width=60)
    employee_treeview.column('name',width=140)
    employee_treeview.column('email',width=180)
    employee_treeview.column('gender',width=180)
    employee_treeview.column('contact',width=100)
    employee_treeview.column('dob',width=100)
    employee_treeview.column('employement_type',width=120)
    employee_treeview.column('education',width=120)       
    employee_treeview.column('work_shift',width=100)
    employee_treeview.column('address',width=200)
    employee_treeview.column('obj',width=100)
    employee_treeview.column('salary',width=140)
    employee_treeview.column('usertype',width=120)   

    #3.  ###########################################################
    # creating all inventory section for employment in  Menaga Employee Detail window

    detail_frame = Frame(employee_frame,bg='white' )
    detail_frame.place(x=20, y=280)


    empid_label = Label(detail_frame,text='EmpId',font=('times new roman', 12),bg='white')
    empid_label.grid(row=0,column=0,padx=20,pady=10,sticky='w')
    empid_entry = Entry(detail_frame,font=('times new roman', 12),bg='lightyellow')
    empid_entry.grid(row=0,column=1,padx=20,pady=10)


    name_label = Label(detail_frame,text='Name',font=('times new roman', 12),bg='white')
    name_label.grid(row=0,column=2,padx=20,pady=10,sticky='w')
    name_entry = Entry(detail_frame,font=('times new roman', 12),bg='lightyellow')
    name_entry.grid(row=0,column=3,padx=20,pady=10)


    email_label = Label(detail_frame,text='Email',font=('times new roman', 12),bg='white')
    email_label.grid(row=0,column=4,padx=20,pady=10,sticky='w')
    email_entry = Entry(detail_frame,font=('times new roman', 12),bg='lightyellow')
    email_entry.grid(row=0,column=5,padx=20,pady=10)


    gender_label = Label(detail_frame,text='Gender',font=('times new roman', 12),bg='white')
    gender_label.grid(row=1,column=0,padx=20,pady=10,sticky='w')
    gender_combobox=ttk.Combobox(detail_frame,values=('Male','Female'),font=('times new roman', 12),width=18,state='readonly')
    gender_combobox.set('Select Gender')
    gender_combobox.grid(row=1,column=1)

    dob_label = Label(detail_frame,text='Date of Birth',font=('times new roman', 12),bg='white')
    dob_label.grid(row=1,column=2,padx=20,pady=10,sticky='w')
    dob_date_entry=DateEntry(detail_frame,width=18,font=('times new roman', 12),state='readonly',date_pattern='dd/mm/yyyy')
    dob_date_entry.grid(row=1,column=3)

    
    contact_label = Label(detail_frame,text='Contact',font=('times new roman', 12),bg='white')
    contact_label.grid(row=1,column=4,padx=20,pady=10,sticky='w')
    contact_entry = Entry(detail_frame,font=('times new roman', 12),bg='lightyellow')
    contact_entry.grid(row=1,column=5,padx=20,pady=10)


    employment_type_label = Label(detail_frame,text='Employment Type',font=('times new roman', 12),bg='white')
    employment_type_label.grid(row=2,column=0,padx=20,pady=10,sticky='w')
    employment_type_combobox=ttk.Combobox(detail_frame,values=('Full Time','Part Time','Casual','Contract','Intern'),font=('times new roman', 12),width=18,state='readonly')
    employment_type_combobox.set('Select Type')
    employment_type_combobox.grid(row=2,column=1)


    education_label = Label(detail_frame,text='Education',font=('times new roman', 12),bg='white')
    education_label.grid(row=2,column=2,padx=20,pady=10,sticky='w')
    education_options=["B.Tech","B.Com","M.Tech","M.Com",'B.Sc',"M.Sc",'BBA',"MBA","LLB","LLM","B.Arch","M.Arch"]
    education_combobox=ttk.Combobox(detail_frame,values=education_options,font=('times new roman', 12),width=18,state='readonly')
    education_combobox.set('Select Education')
    education_combobox.grid(row=2,column=3)


    work_shift_label = Label(detail_frame,text='Work Shift',font=('times new roman', 12),bg='white')
    work_shift_label.grid(row=2,column=4,padx=20,pady=10,sticky='w')
    work_shift_combobox=ttk.Combobox(detail_frame,values=('Morning','Evening','Night'),font=('times new roman', 12),width=18,state='readonly')
    work_shift_combobox.set('Select Work Shift')
    work_shift_combobox.grid(row=2,column=5)


    address_label = Label(detail_frame,text='Address',font=('times new roman', 12),bg='white')
    address_label.grid(row=3,column=0,padx=20,pady=10,sticky='w')
    address_text=Text(detail_frame,width=20,height=3,font=('times new roman', 12),bg='lightyellow')
    address_text.grid(row=3,column=1,rowspan=2)


    doj_label = Label(detail_frame,text='Date of Joining',font=('times new roman', 12),bg='white')
    doj_label.grid(row=3,column=2,padx=20,pady=10,sticky='w')
    doj_date_entry=DateEntry(detail_frame,width=18,font=('times new roman', 12),state='readonly',date_pattern='dd/mm/yyyy')
    doj_date_entry.grid(row=3,column=3)


    usertype_label = Label(detail_frame,text='User type',font=('times new roman', 12),bg='white')
    usertype_label.grid(row=4,column=2,padx=20,pady=10,sticky='w')
    usertype_combobox=ttk.Combobox(detail_frame,values=('Admin','Employee'),font=('times new roman', 12),width=18,state='readonly')
    usertype_combobox.set('Select User Type')
    usertype_combobox.grid(row=4,column=3)    


    salary_label = Label(detail_frame,text='Salary',font=('times new roman', 12),bg='white')
    salary_label.grid(row=3,column=4,padx=20,pady=10,sticky='w')
    salary_entry = Entry(detail_frame,font=('times new roman', 12),bg='lightyellow')
    salary_entry.grid(row=3,column=5,padx=20,pady=10)


    password_label = Label(detail_frame,text='Password',font=('times new roman', 12),bg='white')
    password_label.grid(row=4,column=4,padx=20,pady=10,sticky='w')
    password_entry = Entry(detail_frame,font=('times new roman', 12),bg='lightyellow')
    password_entry.grid(row=4,column=5,padx=20,pady=10)

    #3.  ###########################################################
    #creating bottom buttons of manage employee detail section

    button_frame=Frame(employee_frame,bg='white')
    button_frame.place(x=200,y=520)

    add_button =Button(button_frame,text='Add',font=("times new roman",12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    add_button.grid(row=0,column=0,padx=20)

    update_button =Button(button_frame,text='Update',font=("times new roman",12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    update_button.grid(row=0,column=1,padx=20)

    delete_button =Button(button_frame,text='Delete',font=("times new roman",12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    delete_button.grid(row=0,column=2,padx=20)

    clear_button =Button(button_frame,text='Clear',font=("times new roman",12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    clear_button.grid(row=0,column=3,padx=20)




#============================================================================
#GUI part
window=Tk()
window.title('Dashboard')

window.geometry('1270x668+0+0') # window position fixid
window.resizable(0,0)
window.config(bg="white")

#============================================================================
# creating title of inventory management system

bg_image = PhotoImage(file="E:/python projects/inventory management system/images/inventory.png")
titleLabel =Label(window,image=bg_image,compound=LEFT,text="Inventory Management System",font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor='w',padx=20)
titleLabel.place(x=0,y=0,relwidth=1)

logoutButton = Button(window,text='Logout',font=('times new roman',20,'bold'),fg='#010c48')
logoutButton.place(x=1100 ,y=10)

subtitleLabel=Label(window,text="Welcome Admin\t\t Date: 04-05-2025\t\t Time: 14:54 pm",font=("times new roman",15),bg='#4d636d',fg='white')
subtitleLabel.place(x=0,y=70,relwidth=1)

# creating Left frame on inventory dashboard
#============================================================================

leftFrame =Frame(window)
leftFrame.place(x=0 ,y=182,width=200,height=555)

logoImage =PhotoImage(file="E:/python projects/inventory management system/images/checklist.png")
imageLabel =Label(leftFrame,image=logoImage)
imageLabel.pack()

# menu label for all buttons of employee,supplier,catergory,product,sales,exit
#============================================================================

menuLabel = Label(leftFrame,text='Menu',font=('times new roman',20),bg='#009688')
menuLabel.pack(fill=X )

employee_icon=PhotoImage(file="E:/python projects/inventory management system/images/staff.png")
employee_button = Button(leftFrame,image=employee_icon,compound=LEFT,text=' Employees',font=('times new roman',20,'bold'),anchor='w',padx=10,command=employee_form)
employee_button.pack(fill=X)

supplier_icon=PhotoImage(file="E:/python projects/inventory management system/images/supplier.png")
supplier_button = Button(leftFrame,image=supplier_icon,compound=LEFT,text=' Supplier',font=('times new roman',20,'bold'),anchor='w',padx=10)
supplier_button.pack(fill=X)

categories_icon=PhotoImage(file="E:/python projects/inventory management system/images/categories.png")
categories_button = Button(leftFrame,image=categories_icon,compound=LEFT,text=' Category',font=('times new roman',20,'bold'),anchor='w',padx=10)
categories_button.pack(fill=X)

products_icon=PhotoImage(file="E:/python projects/inventory management system/images/product.png")
products_button = Button(leftFrame,image=products_icon,compound=LEFT,text=' Product',font=('times new roman',20,'bold'),anchor='w',padx=10)
products_button.pack(fill=X)

sales_icon=PhotoImage(file="E:/python projects/inventory management system/images/sales.png")
sales_button = Button(leftFrame,image=sales_icon,compound=LEFT,text=' Sales',font=('times new roman',20,'bold'),anchor='w',padx=10)
sales_button.pack(fill=X)

exit_icon=PhotoImage(file="E:/python projects/inventory management system/images/exit.png")
exit_button = Button(leftFrame,image=exit_icon,compound=LEFT,text=' Exit',font=('times new roman',20,'bold'),anchor='w',padx=10)
exit_button.pack(fill=X)

# creating a frame for totall employees icon,text,count show
#============================================================================

emp_frame=Frame(window,bg="#2C3E50",bd=3,relief=RIDGE)
emp_frame.place(x=400,y=125,height=170,width=280)
# for employee icon
total_emp_icon = PhotoImage(file="E:/python projects/inventory management system/images/allemployees.png")
total_emp_icon_label=Label(emp_frame,image=total_emp_icon,bg="#2C3E50")
total_emp_icon_label.pack(pady=10)
# for employee text
total_emp_label=Label(emp_frame,text='Total Employees',bg="#2C3E50",fg="white",font=("times new roman",15,'bold'))
total_emp_label.pack()
# for employee count
total_emp_count_label=Label(emp_frame,text='0',bg="#2C3E50",fg="white",font=("times new roman",30,'bold'))
total_emp_count_label.pack()

# creating a frame for totall supplier icon,text,count show
#============================================================================


sub_frame=Frame(window,bg="#8E44AD",bd=3,relief=RIDGE)
sub_frame.place(x=800,y=125,height=170,width=280)

total_sub_icon = PhotoImage(file="E:/python projects/inventory management system/images/totalsupplier.png")
total_sub_icon_label=Label(sub_frame,image=total_sub_icon,bg="#8E44AD")
total_sub_icon_label.pack(pady=10)

total_sub_label=Label(sub_frame,text='Total Suppliers',bg="#8E44AD",fg="white",font=("times new roman",15,'bold'))
total_sub_label.pack()

total_sub_count_label=Label(sub_frame,text='0',bg="#8E44AD",fg="white",font=("times new roman",30,'bold'))
total_sub_count_label.pack()



# creating a frame for totall categores icon,text,count show
#============================================================================

cat_frame=Frame(window,bg="#27AE60",bd=3,relief=RIDGE)
cat_frame.place(x=400,y=310,height=170,width=280)
# for category icon
total_cat_icon = PhotoImage(file="E:/python projects/inventory management system/images/totalcategory.png")
total_cat_icon_label=Label(cat_frame,image=total_cat_icon,bg="#27AE60")
total_cat_icon_label.pack(pady=10)
# for category text
total_cat_label=Label(cat_frame,text='Total Categories',bg="#27AE60",fg="white",font=("times new roman",15,'bold'))
total_cat_label.pack()
# for category count
total_cat_count_label=Label(cat_frame,text='0',bg="#27AE60",fg="white",font=("times new roman",30,'bold'))
total_cat_count_label.pack()

# creating a frame for totall products icon,text,count show
#============================================================================

prod_frame=Frame(window,bg="#5F9EA0",bd=3,relief=RIDGE)
prod_frame.place(x=800,y=310,height=170,width=280)
# for products icon

total_prod_icon = PhotoImage(file="E:/python projects/inventory management system/images/totalproduct.png")
total_prod_icon_label=Label(prod_frame,image=total_prod_icon,bg="#5F9EA0")
total_prod_icon_label.pack(pady=10)
# for products text

total_prod_label=Label(prod_frame,text='Total Products',bg="#5F9EA0",fg="white",font=("times new roman",15,'bold'))
total_prod_label.pack()
# for products count

total_prod_count_label=Label(prod_frame,text='0',bg="#5F9EA0",fg="white",font=("times new roman",30,'bold'))
total_prod_count_label.pack()


# creating a frame for totall Sales icon,text,count show
#============================================================================

sales_frame=Frame(window,bg="#E74C3C",bd=3,relief=RIDGE)
sales_frame.place(x=600,y=495,height=170,width=280)

# for Sales icon

total_sales_icon = PhotoImage(file="E:/python projects/inventory management system/images/totalsales.png")
total_sales_icon_label=Label(sales_frame,image=total_sales_icon,bg="#E74C3C")
total_sales_icon_label.pack(pady=10)

# for Sales text

total_sales_label=Label(sales_frame,text='Total Sales',bg="#E74C3C",fg="white",font=("times new roman",15,'bold'))
total_sales_label.pack()

# for Sales count

total_sales_count_label=Label(sales_frame,text='0',bg="#E74C3C",fg="white",font=("times new roman",30,'bold'))
total_sales_count_label.pack()


window.mainloop()





