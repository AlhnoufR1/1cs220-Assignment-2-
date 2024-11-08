import unittest
from datetime import date, datetime


# Define classes with specified attributes

class EBook:
    def __init__(self, title: str, author: str, publish_date: date, price: float, genre: str):
        """Initialize the eBook with title, author, publish date, price, and genre."""
        self._title = title
        self._author = author
        self._publish_date = publish_date
        self._price = price
        self._genre = genre

    def __str__(self):
        return (f"Title: {self._title}\nAuthor: {self._author}\nGenre: {self._genre}\n"
                f"Price: ${self._price:.2f}\nPublished: {self._publish_date}\n")


class Customer:
    def __init__(self, name: str, contact_info: str, customer_id: str):
        """Initialize customer attributes with name, contact info, and customer ID."""
        self._name = name
        self._contact_info = contact_info
        self._customer_id = customer_id
        self._orders = []  # Store tuples of (EBook, quantity)

    def add_order(self, ebook, quantity):
        """Add an eBook with a quantity to the customer's orders."""
        self._orders.append((ebook, quantity))

    def __str__(self):
        orders_str = "\n".join(f"{ebook._title} - Qty: {quantity}" for ebook, quantity in self._orders)
        return (f"Customer Name: {self._name}\nContact Info: {self._contact_info}\n"
                f"Customer ID: {self._customer_id}\nOrders:\n{orders_str if orders_str else 'No orders'}\n")


class RegularCustomer(Customer):
    def apply_discount(self):
        return 0.05  # 5% discount for regular customers

    def __str__(self):
        return super().__str__() + "Customer Type: Regular\nDiscount: 5%\n"


class LoyalCustomer(Customer):
    def apply_discount(self):
        return 0.10  # 10% discount for loyal customers

    def __str__(self):
        return super().__str__() + "Customer Type: Loyal\nDiscount: 10%\n"


class ShoppingCart:
    def __init__(self, cart_id: str, customer_id: str):
        """Initialize shopping cart attributes with cart ID, book list, total price, and customer ID."""
        self._cart_id = cart_id
        self._books = []  # Store tuples of (EBook, quantity)
        self._total = 0.0
        self._customer_id = customer_id

    def add_book(self, book, quantity):
        """Add a book with a quantity to the shopping cart and update the total."""
        self._books.append((book, quantity))
        self._total += book._price * quantity

    def __str__(self):
        items_str = "\n".join(f"{book._title} - Qty: {qty} - ${book._price * qty:.2f}" for book, qty in self._books)
        return (f"Shopping Cart ID: {self._cart_id}\nCustomer ID: {self._customer_id}\n"
                f"Items:\n{items_str if items_str else 'No items'}\nTotal: ${self._total:.2f}\n")


class Order:
    def __init__(self, order_id: str, customer: Customer, tax: float, date: date):
        """Initialize order attributes."""
        self._order_id = order_id
        self._customer = customer
        self._tax = tax
        self._date = date

    def __str__(self):
        return (f"Order ID: {self._order_id}\nCustomer: {self._customer._name}\n"
                f"Tax: {self._tax * 100}%\nDate: {self._date}\n")


class Invoice:
    def __init__(self, order: Order, discount: float, vat: float, invoice_id: str):
        """Initialize invoice attributes."""
        self._order = order
        self._discount = discount
        self._vat = vat
        self._invoice_id = invoice_id

    def generate_invoice(self):
        subtotal = sum(book._price * qty for book, qty in self._order._customer._orders)
        discount_amount = subtotal * self._discount
        vat_amount = (subtotal - discount_amount) * self._vat
        total = subtotal - discount_amount + vat_amount
        items_str = "\n".join(f"{book._title} x {qty} @ ${book._price:.2f} = ${book._price * qty:.2f}"
                              for book, qty in self._order._customer._orders)
        return (
            f"INVOICE #{self._invoice_id}\nDate: {self._order._date}\nCustomer ID: {self._order._customer._customer_id}\n"
            f"Items:\n{items_str if items_str else 'No items'}\nSubtotal: ${subtotal:.2f}\n"
            f"Discount: -${discount_amount:.2f}\nVAT ({self._vat * 100}%): ${vat_amount:.2f}\nTotal: ${total:.2f}\n")


class Payment:
    def __init__(self, payment_id: str, total: float, date: date, payment_method: str):
        """Initialize payment attributes."""
        self._payment_id = payment_id
        self._total = total
        self._date = date
        self._payment_method = payment_method

    def __str__(self):
        return (f"Payment ID: {self._payment_id}\nTotal: ${self._total:.2f}\nDate: {self._date}\n"
                f"Payment Method: {self._payment_method}\n")


# Test case with specified books and customers

class TestEBookStore(unittest.TestCase):
    def test_customer_management(self):
        print("Testing Customer Management")
        customer1 = RegularCustomer("Ahmed", "ahmed@example.com", "C001")
        customer2 = LoyalCustomer("Rashed", "rashed@example.com", "C002")

        # Add an order to Ahmed
        book = EBook("The Rings of Saturn", "W.G. Sebald", date(1995, 1, 1), 15.99, "Literature")
        customer1.add_order(book, 1)

        # Display customer details
        print(customer1)
        print(customer2)

    def test_ebook_management(self):
        print("Testing E-Book Management")
        book1 = EBook("The Rings of Saturn", "W.G. Sebald", date(1995, 1, 1), 15.99, "Literature")
        book2 = EBook("Labyrinths: Selected Stories & Other Writings", "Jorge Luis Borges", date(1962, 3, 20), 12.99,
                      "Fiction")
        book3 = EBook("The Hour of the Star", "Clarice Lispector", date(1977, 7, 25), 9.99, "Literature")
        book4 = EBook("Journey to the End of the Night", "Louis-Ferdinand Céline", date(1932, 10, 15), 19.99,
                      "Literature")

        # Display each book's details
        print("Adding e-books to inventory:")
        print(book1)
        print(book2)
        print(book3)
        print(book4)

    def test_shopping_cart(self):
        print("Testing Shopping Cart")
        cart = ShoppingCart("Cart001", "C001")
        book1 = EBook("Labyrinths: Selected Stories & Other Writings", "Jorge Luis Borges", date(1962, 3, 20), 12.99,
                      "Fiction")
        book2 = EBook("The Hour of the Star", "Clarice Lispector", date(1977, 7, 25), 9.99, "Literature")

        # Add books to the cart
        cart.add_book(book1, 2)
        cart.add_book(book2, 3)

        # Display cart details
        print(cart)

    def test_invoice_generation(self):
        print("Testing Invoice Generation")
        customer = LoyalCustomer("Alhnouf", "alhnouf@example.com", "C003")
        order = Order("Order001", customer, 0.1, date(2023, 6, 1))
        book = EBook("Journey to the End of the Night", "Louis-Ferdinand Céline", date(1932, 10, 15), 19.99,
                     "Literature")

        # Add order for the customer
        customer.add_order(book, 2)

        # Generate and display invoice
        invoice = Invoice(order, discount=0.1, vat=0.08, invoice_id="INV001")
        print(invoice.generate_invoice())

    def test_payment(self):
        print("Testing Payment Processing")
        payment = Payment("Pay001", 59.97, date(2023, 7, 1), "Credit Card")
        print(payment)


if __name__ == "__main__":
    unittest.main(verbosity=2)



