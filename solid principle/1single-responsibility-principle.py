# The Single Responsibility Principle states that a class should have only one reason to change, meaning it should only have one job or responsibility.
import time

class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    def generate(self):
        return  f"\nGenerating report at {time.time()}\ntitle: {self.title}\ncontent:{self.content},"
    
class ReportSaver:
    def save_to_file(self, report, filename):
        with open(filename, "w") as file:
            file.write(report.generate())
        print(f"Report saved to {filename}")
        
        
        
report = Report("Title1","content")
reportsaver = ReportSaver()
reportsaver.save_to_file(report,"report.txt")




# Class 1: Handles invoice data
class Invoice:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items  # List of tuples: (item_name, price)

    def calculate_total(self):
        return sum(price for _, price in self.items)

# Class 2: Handles printing the invoice
class InvoicePrinter:
    def print_invoice(self, invoice):
        print(f"Customer: {invoice.customer}")
        for item, price in invoice.items:
            print(f" - {item}: ${price}")
        print(f"Total: ${invoice.calculate_total()}")

# Class 3: Handles saving the invoice to a file
class InvoiceSaver:
    def save_to_file(self, invoice, filename):
        with open(filename, 'w') as file:
            file.write(f"Customer: {invoice.customer}\n")
            for item, price in invoice.items:
                file.write(f"{item}: ${price}\n")
            file.write(f"Total: ${invoice.calculate_total()}\n")
        print(f"Invoice saved to {filename}")

# 🧪 Usage
invoice = Invoice("Ram Bahadur", [("Laptop", 1200), ("Mouse", 25)])
printer = InvoicePrinter()
saver = InvoiceSaver()

printer.print_invoice(invoice)
saver.save_to_file(invoice, "invoice.txt")
