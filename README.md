# ShopNook - E-commerce Website

ShopNook is a modern e-commerce web application built with Django. It enables users to browse products, add them to their cart, and download PDF invoices for their orders. Admins can manage products, including setting prices and uploading images.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Uploads and Static Files](#file-uploads-and-static-files)
- [PDF Generation](#pdf-generation)
- [Issues](#issues)
- [Deployment](#deployment)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features
- **User Authentication:** Registration, login, and logout functionality.
- **Product Listings:** View available products and their details.
- **Shopping Cart:** Add products to cart and review orders.
- **Checkout & Billing:** Generate and download PDF bills of orders.
- **Order & Product Management:** Admin can manage orders and products.
  
## Project Structure

shopnook/
├── shopnook/                 # Main Django project folder
│   ├── __init__.py
│   ├── settings.py           # Project settings
│   ├── urls.py               # Project URLs
│   └── wsgi.py               # WSGI configuration
├── shop/                     # Core app for product and order management
│   ├── migrations/           # Database migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Product and order models
│   ├── views.py              # Views for the app
│   ├── urls.py               # App-specific URLs
│   ├── static/shop/          # Static files (CSS, JS)
│   │   ├── style.css         # Basic CSS for styling
│   ├── templates/shop/       # HTML templates
│   │   ├── home.html         # Homepage
│   │   ├── product_list.html # Product listing
│   │   ├── product_detail.html # Product details
│   │   ├── cart.html         # Cart view
│   │   ├── order_confirmation.html # Order confirmation
│   │   ├── bill.html         # PDF Bill template
├── media/                    # Media folder for uploaded product images
├── manage.py                 # Django management script
└── README.md                 # Project documentation


## Getting Started

Follow these instructions to set up the project on your local machine.

### Prerequisites

- Python 3.x
- Django 4.x
- Pip package manager
- Virtual environment (recommended)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/shopnook.git
   cd shopnook
   ```
2.**Create a virtual environment and activate it:**

  ```bash
  python -m venv env
  source env/bin/activate  # On Windows: env\Scripts\activate
  ```
3.**Install the dependencies:**
  ```bash
  pip install -r requirements.txt
  ```
**4.Run migrations:**
```bash
python manage.py migrate
```

**5.Create a superuser (Admin):**
```bash
python manage.py createsuperuser
```
**6.Run the development server:**
```bash
python manage.py runserver
```
**Access the application:**

Visit http://127.0.0.1:8000/ in your browser.
##Project Details
###Models
Product: Stores product details like name, description, price, and image.
OrderItem: Stores individual product orders with quantity.
Order: Tracks the items ordered and the total price.
###Views
User login and creation: Basic user authentication.
Product List: Displays all products.
Product Detail: Shows individual product details.
Cart: Shows the selected product in the cart.
Checkout: Generates a PDF bill for the order.
Order Confirmation: Displays after successful checkout.
