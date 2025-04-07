# PhiMart

PhiMart is an e-commerce API built with Django REST Framework (DRF). It provides a robust backend system for building e-commerce applications with comprehensive features including user authentication, product management, cart functionality, order processing, and more.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [API Endpoints](#api-endpoints)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Development](#development)
- [Authentication](#authentication)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**: Secure JWT-based authentication system
- **Product Management**: Complete CRUD operations for products
- **Categories**: Organized product categorization
- **Shopping Cart**: User-specific cart management
- **Order Processing**: Create and manage orders
- **Checkout System**: Streamlined checkout process
- **User Profiles**: User information management
- **Reviews & Ratings**: Product review system
- **Search Functionality**: Advanced product search

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Documentation**: Swagger/OpenAPI

## API Endpoints

### Authentication
- `POST /api/auth/register/`: Register a new user
- `POST /api/auth/login/`: Login and receive JWT tokens
- `POST /api/auth/refresh/`: Refresh JWT token
- `POST /api/auth/logout/`: Logout and invalidate token

### Users
- `GET /api/users/me/`: Get current user profile
- `PUT /api/users/me/`: Update user profile
- `GET /api/users/{id}/`: Get specific user details (admin only)

### Products
- `GET /api/products/`: List all products with pagination
- `POST /api/products/`: Create new product (admin only)
- `GET /api/products/{id}/`: Get product details
- `PUT /api/products/{id}/`: Update product (admin only)
- `DELETE /api/products/{id}/`: Delete product (admin only)
- `GET /api/products/featured/`: Get featured products

### Categories
- `GET /api/categories/`: List all categories
- `POST /api/categories/`: Create new category (admin only)
- `GET /api/categories/{id}/`: Get category details
- `PUT /api/categories/{id}/`: Update category (admin only)
- `DELETE /api/categories/{id}/`: Delete category (admin only)
- `GET /api/categories/{id}/products/`: Get products in a category

### Cart
- `GET /api/cart/`: Get user's cart
- `POST /api/cart/items/`: Add item to cart
- `PUT /api/cart/items/{id}/`: Update cart item
- `DELETE /api/cart/items/{id}/`: Remove item from cart
- `DELETE /api/cart/clear/`: Clear entire cart

### Orders
- `GET /api/orders/`: List user's orders
- `POST /api/orders/`: Create a new order
- `GET /api/orders/{id}/`: Get order details
- `PUT /api/orders/{id}/`: Update order status (admin only)

### Reviews
- `GET /api/products/{id}/reviews/`: Get product reviews
- `POST /api/products/{id}/reviews/`: Add a review
- `PUT /api/reviews/{id}/`: Update user's review
- `DELETE /api/reviews/{id}/`: Delete user's review

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL
- pip

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/dabananda/PhiMart.git
   cd PhiMart
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate # On Windows
   # On Linux: source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables (see [Environment Variables](#environment-variables) section)

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:password@localhost:5432/phimart
ALLOWED_HOSTS=localhost,127.0.0.1
JWT_SECRET_KEY=your_jwt_secret
```

## Development

### Running Tests
```bash
python manage.py test
```

### Code Style
We use Black and isort for code formatting:
```bash
black .
isort .
```

### API Documentation
API documentation is available at `/api/docs/` when the server is running.

## Authentication

PhiMart uses JWT (JSON Web Tokens) for authentication:

1. Register a new user at `/api/auth/register/`
2. Login at `/api/auth/login/` to receive access and refresh tokens
3. Include the access token in the Authorization header for authenticated requests:
   ```
   Authorization: Bearer <your_access_token>
   ```
4. When the access token expires, use the refresh token at `/api/auth/refresh/` to get a new one

## Database Schema

The project includes the following main models:

- **User**: Extended Django User model with additional fields
- **Product**: Core product information including name, description, price
- **Category**: Product categorization
- **Cart** and **CartItem**: Shopping cart functionality
- **Order** and **OrderItem**: Order management
- **Review**: Product reviews and ratings

## Contributing

We welcome contributions to PhiMart! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please make sure your code follows our coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Developed by [Dabananda Mitra](https://github.com/dabananda)

---

<div align="center">
<h1> Dabananda Mitra </h1>
</div>

<div align="center">
  <img src="https://res.cloudinary.com/djz3p8sux/image/upload/v1742125099/dabananda_mitra_formal_Small_1x1_o8uxit.png" width="250" height="250" style="border-radius: 50%">
</div>

<h3 align="center">Software Engineer | Problem Solver | Open Source Enthusiast</h3>

---

### 🌐 Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dabananda) [![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dabananda) [![Twitter](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/dabanandamitra) [![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.om/imdmitra/) [![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/8801304080014) [![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discordapp.com/users/dabanandamitra)

---

### 💻 Online Judge Profiles

[![LeetCode](https://img.shields.io/badge/-LeetCode-FFA116?style=for-the-badge)](https://leetcode.com/u/dabananda/) [![Codeforces](https://img.shields.io/badge/-Codeforces-1F8ACB?style=for-the-badge)](https://codeforces.com/profile/dabananda) [![CodeChef](https://img.shields.io/badge/-CodeChef-5B4638?style=for-the-badge)](https://www.codechef.com/users/dabananda) [![HackerRank](https://img.shields.io/badge/-HackerRank-00EA64?style=for-the-badge)](https://www.hackerrank.com/profile/dabananda) [![CodingNinjas](https://img.shields.io/badge/-Coding_Ninjas-FFA500?style=for-the-badge)](https://www.naukri.com/code360/profile/48a35475-0af2-4d4e-8f26-2d793b64843a) [![UVa](https://img.shields.io/badge/-UVa-00B388?style=for-the-badge)](https://uhunt.onlinejudge.org/id/1167157) [![Beecrowd](https://img.shields.io/badge/-Beecrowd-009688?style=for-the-badge)](https://judge.beecrowd.com/en/profile/467832) [![Vjudge](https://img.shields.io/badge/-Vjudge-8A2BE2?style=for-the-badge)](https://vjudge.net/user/dabanandamitra)