#  ALX Travel App (alx_travel_app)

This is a Django-based backend application for managing travel listings, bookings, and user reviews. The project is part of the **ALX Software Engineering** program and focuses on database modeling, serialization, and data seeding using Django management commands.


##  Project Structure
alx_travel_app/
├── alx_travel_app/ # Django project folder (settings, URLs)
├── listings/ # Main app for listings, bookings, reviews
│ ├── models.py # Database models
│ ├── serializers.py # DRF serializers
│ ├── management/
│ │ └── commands/
│ │ └── seed.py # Seeder script for database
├── db.sqlite3 # Default SQLite database
├── manage.py # Django management entry point
└── README.md

## Features

- Define `Listing`, `Booking`, and `Review` models.
- Implement serializers for `Listing` and `Booking`.
- Create a custom management command to populate the database with sample listings.
- Easy setup with Django and SQLite.

##  Setup Instructions

### 1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/alx_travel_app_0x00.git
cd alx_travel_app_0x00
2. Set Up Virtual Environment

python3 -m venv t_env
source t_env/bin/activate
pip install -r requirements.txt
If you don’t have requirements.txt, install manually:

pip install django djangorestframework
3. Run Migrations
python manage.py makemigrations
python manage.py migrate
4. Seed the Database

python manage.py seed
5. Run the Development Server
python manage.py runserver
 Models Overview
 Listing
title: Title of the listing

description: Detailed description

price_per_night: Price per night

location: City or country

 Booking
listing: ForeignKey to Listing

check_in / check_out: Dates

guest_name: Who booked it

 Review
listing: ForeignKey to Listing

rating: Integer (1–5)

comment: Optional user comment

Seeder Command
The custom command python manage.py seed generates sample listings with dummy data for testing and development purposes.

 Tech Stack
Language: Python 3.8+

Framework: Django 3.x+

Database: SQLite (for development)

Serialization: Django REST Framework

 Contributing
Feel free to fork the repository, make changes, and submit a pull request. All contributions are welcome!

 License
This project is for educational purposes as part of the ALX SE program. No commercial license provided.

 Author
Israel Odafe
ALX SE Program
GitHub: @oodafeisrael

