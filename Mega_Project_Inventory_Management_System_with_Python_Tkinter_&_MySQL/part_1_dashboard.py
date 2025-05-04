from tkinter import *
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
employee_button = Button(leftFrame,image=employee_icon,compound=LEFT,text=' Employees',font=('times new roman',20,'bold'),anchor='w',padx=10)
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