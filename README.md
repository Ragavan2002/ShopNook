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

```bash
.
├── shopnook/              # Main Django app folder
│   ├── migrations/        # Database migrations
│   ├── static/            # Static files (CSS, JS, images)
│   ├── templates/         # HTML templates
│   ├── admin.py           # Admin configuration
│   ├── apps.py            # App configuration
│   ├── models.py          # Data models for the project
│   ├── urls.py            # URL routing for the app
│   └── views.py           # Application logic and views
├── media/                 # Uploaded product images
├── requirements.txt       # Project dependencies
├── manage.py              # Django management script
└── README.md              # This file

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
