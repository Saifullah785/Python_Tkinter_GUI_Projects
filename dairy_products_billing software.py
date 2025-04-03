import tkinter as tk
from tkinter import ttk, messagebox
import csv
import datetime

class DairyBillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" Pak Dairy Products Billing Software")
        self.root.geometry("900x600")
        self.root.configure(bg="#1a64de")  # Light green background

        # Variables
        self.products = {"Milk": 160, "Ghee": 2200, "Butter": 1600, "Cream": 1200, "Koya": 850}
        self.bill_items = []
        self.product_vars = {product: tk.IntVar() for product in self.products.keys()}

        # Main Frames
        self.create_main_frames()
        
        # UI Components
        self.create_billing_ui()
        self.create_customer_ui()
        self.create_button_section()

    def create_main_frames(self):
         style = ttk.Style()
         style.configure("TFrame", background="#1a64de")  # Set your desired background color

         self.main_frame = ttk.Frame(self.root, padding=10, style="TFrame")
         self.main_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

         self.billing_frame = ttk.Frame(self.main_frame, padding=10, style="TFrame")
         self.billing_frame.grid(row=0, column=0, sticky="nsew")

         self.customer_frame = ttk.Frame(self.main_frame, padding=10, style="TFrame")
         self.customer_frame.grid(row=0, column=1, sticky="nsew")

         self.button_frame = ttk.Frame(self.root, padding=10, style="TFrame")
         self.button_frame.grid(row=2, column=1, sticky="ew")

   
    # def create_main_frames(self):
    #     self.main_frame = ttk.Frame(self.root, padding=10)
    #     self.main_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

    #     self.billing_frame = ttk.Frame(self.main_frame, padding=10)
    #     self.billing_frame.grid(row=0, column=0, sticky="nsew")

    #     self.customer_frame = ttk.Frame(self.main_frame, padding=10)
    #     self.customer_frame.grid(row=0, column=1, sticky="nsew")

    #     self.button_frame = ttk.Frame(self.root, padding=10)
    #     self.button_frame.grid(row=2, column=1, sticky="ew")

    def create_billing_ui(self):
        ttk.Label(self.billing_frame, text="Billing Section", font=("Arial", 14, "bold"), background="#dff0d8").pack()
        
        for product, price in self.products.items():
            frame = ttk.Frame(self.billing_frame)
            frame.pack(fill=tk.X, padx=5, pady=2)
            ttk.Label(frame, text=f"{product} ({price} per unit):", background="#dff0d8").pack(side=tk.LEFT)
            entry = ttk.Entry(frame, textvariable=self.product_vars[product], width=10, background="white")
            entry.pack(side=tk.RIGHT)
        
        self.bill_text = tk.Text(self.billing_frame, height=15, width=50, background="white")
        self.bill_text.pack(pady=5)
    
    def create_customer_ui(self):
        ttk.Label(self.customer_frame, text="Customer Records", font=("Arial", 14, "bold"), background="#dff0d8").pack()
        
        ttk.Label(self.customer_frame, text="Customer ID:", background="#dff0d8").pack()
        self.customer_id_var = tk.StringVar()
        ttk.Entry(self.customer_frame, textvariable=self.customer_id_var, background="white").pack()
        
        ttk.Label(self.customer_frame, text="Customer Name:", background="#dff0d8").pack()
        self.customer_name_var = tk.StringVar()
        ttk.Entry(self.customer_frame, textvariable=self.customer_name_var, background="white").pack()
        
        ttk.Label(self.customer_frame, text="Phone Number:", background="#dff0d8").pack()
        self.customer_phone_var = tk.StringVar()
        ttk.Entry(self.customer_frame, textvariable=self.customer_phone_var, background="white").pack()
        
        self.customer_text = tk.Text(self.customer_frame, height=10, width=40, background="white")
        self.customer_text.pack()
    
    def create_button_section(self):
        ttk.Button(self.button_frame, text="Add to Bill", command=self.add_to_bill).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Generate Bill", command=self.generate_bill).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Total", command=self.calculate_total).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Save Record", command=self.save_record).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Clear Bill", command=self.clear_bill).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Search Record", command=self.search_customer).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Exit", command=self.root.quit).pack(side=tk.LEFT, padx=5)
    
    def add_to_bill(self):
        self.bill_items.clear()
        self.bill_text.delete(1.0, tk.END)
        for product, var in self.product_vars.items():
            quantity = var.get()
            if quantity > 0:
                price = self.products[product] * quantity
                self.bill_items.append((product, quantity, price))
                self.bill_text.insert(tk.END, f"{product} x {quantity} = {price}\n")
    
    def generate_bill(self):
        total = sum(item[2] for item in self.bill_items)
        self.bill_text.insert(tk.END, f"\nTotal: {total}\n")

    def calculate_total(self):
        total = sum(item[2] for item in self.bill_items)
        messagebox.showinfo("Total Amount", f"Total Bill Amount: {total}")
    
    def save_record(self):
        if not self.customer_id_var.get() or not self.customer_name_var.get() or not self.customer_phone_var.get():
            messagebox.showwarning("Warning", "Please enter customer details before saving.")
            return
        
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = [date_time, self.customer_id_var.get(), self.customer_name_var.get(), self.customer_phone_var.get()]
        product_quantities = [self.product_vars[product].get() for product in self.products.keys()]
        total_products = sum(product_quantities)
        
        record.extend(product_quantities)
        record.append(total_products)
        
        with open("records.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(record)
        
        messagebox.showinfo("Success", "Record saved successfully!")
    
    def search_customer(self):
        customer_id = self.customer_id_var.get()
        with open("records.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[1] == customer_id:
                    self.customer_name_var.set(row[2])
                    self.customer_phone_var.set(row[3])
                    messagebox.showinfo("Found", "Customer record found!")
                    return
        messagebox.showwarning("Not Found", "Customer not found!")
    
    def clear_bill(self):
        self.bill_items.clear()
        self.bill_text.delete(1.0, tk.END)
        for var in self.product_vars.values():
            var.set(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = DairyBillingApp(root)
    root.mainloop()
