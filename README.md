Project Name: Fully functional online store

Description:

Description:
A Django-based web application featuring an online store environment with HTML and Tailwind CSS for frontend styling. It utilizes SQL databases to enable dynamic product management functionalities, including product creation and deletion. The platform also integrates user authentication mechanisms for secure login and registration processes. Additionally, functional contact forms are implemented to facilitate communication between users and administrators for inquiries and support.

Installation:

Clone the repository to your local machine:

git clone https://github.com/your_username/project_name.git
Navigate to the project directory:


cd project_name ("prototype1" in my case)
Set up a virtual environment:


venv\Scripts\activate
Install the project dependencies:


pip install -r requirements.txt
(which should contain: 
Django==3.2.9
mysqlclient==2.0.3
django-bootstrap4==3.0.1
django-crispy-forms==1.12.0 )

How to Run:

Navigate to the project directory:


cd project_name (again "prototype1" in my case)
Run the Django development server:


python manage.py runserver

Database Setup:

Create a MySQL database:


CREATE DATABASE mydata;
USE mydata;
Initialize the database tables:


python manage.py makemigrations
python manage.py migrate

SQL Code:

For database initialization:


CREATE DATABASE mydata;
USE mydata;
For viewing contact forms and user information:



SELECT Email, Subject, Message FROM prototype1_contact;
SELECT Email, Username, Password FROM auth_user;

For product creation and modification:



CREATE TABLE prototype1_product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    description TEXT,
    image VARCHAR(255)
);
Example product insertion:


SELECT * FROM prototype1_product;
INSERT INTO mydata.prototype1_product (name, price, description, image) 
VALUES ('macbook', 599.99, 'laptop apple new', 'laptop.JPG');

Project Structure
project_name/: Main project directory
manage.py: Django management script
project_name/: Django project settings and configuration
app_name/: Django app directory
templates/: HTML templates directory
static/: Static files directory
media/: Media files directory (uploads, images, etc.)

Contributions: I built the project on my own although i do not own any of the images.

Database aspect(MySQL Workbench):
![Capture](https://github.com/alexander-drg/testing_grounds/assets/114608225/54add96e-1528-41d3-86f6-a4d3d16f3dd8)

Main website page (while logged-in):
![screencapture-127-0-0-1-8000-2024-04-28-16_23_41](https://github.com/alexander-drg/testing_grounds/assets/114608225/48d0049e-0a85-4314-a237-cd959ed844f9)

Account creation section:
![screencapture-127-0-0-1-8000-register-2024-04-28-16_20_13](https://github.com/alexander-drg/testing_grounds/assets/114608225/c0649d5d-0796-4dc0-9453-0eeee2531a2c)

Account credentials (after log-in): 
![screencapture-127-0-0-1-8000-signout-2024-04-28-16_24_01](https://github.com/alexander-drg/testing_grounds/assets/114608225/b9abcbf4-553d-4367-a22d-bbc54e91c895)
