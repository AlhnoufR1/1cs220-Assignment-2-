# EBook Class
class EBook:
    def __init__(self, title, author, publish_date, price, genre):
        """Initialize the eBook with title, author, publish date, price, and genre."""
        self._title = title
        self._author = author
        self._publish_date = publish_date
        self._price = price
        self._genre = genre

    def getTitle(self):
        return self._title

    def setTitle(self, title):
        self._title = title

    def getAuthor(self):
        return self._author

    def setAuthor(self, author):
        self._author = author

    def getPublishDate(self):
        return self._publish_date

    def setPublishDate(self, date):
        self._publish_date = date

    def getPrice(self):
        return self._price

    def setPrice(self, price):
        self._price = price

    def getGenre(self):
        return self._genre

    def setGenre(self, genre):
        self._genre = genre

    def __str__(self):
        return f"EBook({self._title}, {self._author}, {self._publish_date}, {self._price}, {self._genre})"

# Discount Class
class Discount:
    def __init__(self, bulk_discount, loyalty_discount, discount_id, discount_date):
        """Initialize discount attributes."""
        self._bulk_discount = bulk_discount
        self._loyalty_discount = loyalty_discount
        self._discount_id = discount_id
        self._discount_date = discount_date

    def getBulkDiscount(self):
        return self._bulk_discount

    def setBulkDiscount(self, discount):
        self._bulk_discount = discount

    def getLoyaltyDiscount(self):
        return self._loyalty_discount

    def setLoyaltyDiscount(self, discount):
        self._loyalty_discount = discount

    def apply_bulk_discount(self, quantity):
        """Apply bulk discount based on quantity."""
        return self._bulk_discount if quantity > 10 else 0

    def __str__(self):
        return f"Discount({self._discount_id}, Bulk: {self._bulk_discount}, Loyalty: {self._loyalty_discount})"

# Customer Class
class Customer:
    def __init__(self, name, contact_info, customer_id):
        """Initialize customer attributes."""
        self._name = name
        self._contact_info = contact_info
        self._customer_id = customer_id
        self._orders = []

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def addOrder(self, order):
        self._orders.append(order)

    def __str__(self):
        return f"Customer({self._name}, {self._customer_id})"

# RegularCustomer Class
class RegularCustomer(Customer):
    def apply_discount(self):
        """Apply a 5% discount."""
        return 0.05

    def __str__(self):
        return f"RegularCustomer({self._name}, Discount: 5%)"

# LoyalCustomer Class
class LoyalCustomer(Customer):
    def apply_discount(self):
        """Apply a 10% discount."""
        return 0.10

    def __str__(self):
        return f"LoyalCustomer({self._name}, Discount: 10%)"

# ShoppingCart Class
class ShoppingCart:
    def __init__(self, cart_id, customer_id):
        """Initialize shopping cart attributes."""
        self._cart_id = cart_id
        self._books = []
        self._total = 0.0
        self._customer_id = customer_id

    def addBook(self, book):
        self._books.append(book)
        self._total += book.getPrice()

    def getTotal(self):
        return self._total

    def __str__(self):
        return f"ShoppingCart({self._cart_id}, Total: {self._total})"

# Order Class
class Order:
    def __init__(self, order_id, customer, tax, date):
        """Initialize order attributes."""
        self._order_id = order_id
        self._customer = customer
        self._tax = tax
        self._date = date

    def getOrderDetails(self):
        return f"Order({self._order_id}, Customer: {self._customer.getName()}, Tax: {self._tax}, Date: {self._date})"

    def __str__(self):
        return self.getOrderDetails()

# Invoice Class
class Invoice:
    def __init__(self, order, discount, vat, invoice_id):
        """Initialize invoice attributes."""
        self._order = order
        self._discount = discount
        self._vat = vat
        self._invoice_id = invoice_id

    def generate_invoice(self):
        # Generate invoice details
        total = self._order.getOrderDetails()
        return f"Invoice({self._invoice_id}, Total: {total})"

    def __str__(self):
        return self.generate_invoice()

# Payment Class
class Payment:
    def __init__(self, payment_id, total, date, payment_method):
        """Initialize payment attributes."""
        self._payment_id = payment_id
        self._total = total
        self._date = date
        self._payment_method = payment_method

    def __str__(self):
        return f"Payment({self._payment_id}, Total: {self._total}, Date: {self._date})"
