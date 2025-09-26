
# Shortly

A simple Django-based URL shortener with user authentication and dashboard.

## Features

- User authentication (signup, login, logout)
- Custom short URLs
- Random short URL generation
- Track number of visits per short URL
- Unlimited URL shortening per user
- Delete URLs from your dashboard

## Getting Started

### Prerequisites

- Python 3.8+
- Django (see [requirements.txt](requirements.txt))

### Installation

1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd shortly
 
## Initial Commit

1. Authentication
2. Custom URL
3. Random URL Generation
4. Number Of Visits
5. Unlimited URL Shortening
6. Can Use In Your Project
7. Added Delete
 
2. Install dependencies:
   ```sh
   pip install -r requirements.txt 
   ```

3. Run migrations:
   ```sh
   python manage.py migrate
   ```

4. Start the development server:
   ```sh
   python manage.py runserver
   ```

## Usage
* Sign up for an account.
* Log in to access your dashboard.
* Shorten URLs with custom or random short codes.
* View and manage your URLs and visit counts.
* Delete URLs you no longer need.
      
## Project Structure
* authentication/ – User authentication logic
* urlhandler/ – URL shortening and dashboard logic
* templates/ – HTML templates for the app