# Django Multi-Language FAQ API with WYSIWYG Editor

## Overview
This project is a Django-based application designed to manage **Frequently Asked Questions (FAQs)** in multiple languages. It integrates a **WYSIWYG (What You See Is What You Get)** editor for rich-text formatting in FAQ answers, powered by **django-ckeditor**. The application also features **Google Translate** integration via `googletrans` for automatic translation of FAQ content into multiple languages. The project is containerized using **Docker** for seamless deployment and scaling.

## Key Features
- **Multi-language support** for FAQs, allowing dynamic translation of content.
- **WYSIWYG Editor** for FAQ answers, enabling rich-text formatting.
- **Efficient API** to fetch FAQs in different languages.
- **Caching with Redis** to improve translation data retrieval.
- **Dockerized Application** for easy deployment.
  
## Technologies Used
- **Backend**: Django
- **Database**: SQLite (easily replaceable with PostgreSQL in production)
- **Frontend**: Django Admin Interface, CKEditor
- **Cache**: Redis
- **Translation**: `googletrans` (Google Translate API)
- **Containerization**: Docker
- **Version Control**: Git
- **API**: REST API for managing FAQs

---

## Installation Steps

## 1. Clone the Repository
Clone the repository to your local machine:

- **bash**
git clone https://github.com/your-username/faq-multilingual-django.git
cd faq-multilingual-django

## 2. Set Up Virtual Environment (Optional)
For managing dependencies, it is recommended to set up a Python virtual environment.

- **For Windows**:
python -m venv venv
venv\Scripts\activate

- **For macOS/Linux**:
python3 -m venv venv
source venv/bin/activate

## 3. Install Dependencies
Install the required Python packages listed in requirements.txt:

pip install -r requirements.txt

## 4. Apply Migrations
Set up the database by applying the migrations:


python manage.py migrate

## 5. Set Up Static and Media Files
Collect all static files and set up the media directory:


python manage.py collectstatic

## 6. Run the Development Server
Start the development server to run the application locally:

python manage.py runserver
Visit http://127.0.0.1:8000 to view the app.

# Running with Docker

## 1. Build the Docker Image
Use Docker Compose to build the Docker image for the application:

docker-compose build

## 2. Start the Docker Container
Run the container and start the application:


docker-compose up
You can access the application at http://localhost:8000.

## 3. Stopping the Docker Container
To stop the running container:


docker-compose down

# API Usage
The application provides a REST API to manage FAQs. You can interact with the API using curl, Postman, or any HTTP client.

## 1. Fetch All FAQs (Default Language - English)

curl http://localhost:8000/api/faqs/

## 2. Fetch FAQs in Hindi

curl http://localhost:8000/api/faqs/?lang=hi

## 3. Fetch FAQs in Bengali

curl http://localhost:8000/api/faqs/?lang=bn

## 4. Add a New FAQ
To add a new FAQ, make a POST request to the /api/faqs/ endpoint with the following data:


{
  "question": "What is Docker?",
  "answer": "<p>Docker is a platform for developing, shipping, and running applications.</p>",
  "question_hi": "डॉकर क्या है?",
  "question_bn": "ডকার কি?"
}

# Admin Panel
The Django admin interface allows you to manage FAQs easily.

## 1. Access the Admin Panel
Navigate to http://127.0.0.1:8000/admin to log in with your superuser credentials.

## 2. Create a Superuser (If not created)
To create a superuser account for accessing the admin panel, run the following:
python manage.py createsuperuser
Follow the prompts to set up your superuser account.

# Caching Mechanism
The application utilizes Redis to cache translations, improving performance by reducing the need to repeatedly request translations from the API.

## 1. Install Redis
If you're running Redis locally, install and start the Redis server. Alternatively, you can run Redis within a Docker container:

docker run -p 6379:6379 redis


# Testing
The project includes unit tests to verify the functionality of the API and model methods.

## 1. Run Unit Tests
Run the tests using pytest:

pytest

## 2. Check Code Quality
The code adheres to PEP8 conventions. You can check the code quality with flake8:


flake8 .

## Contributing
We welcome contributions to this project! Here's how you can contribute:

## Fork the repository.
Create a new branch for your feature or bugfix.
Make your changes and commit them with clear, concise messages.
Push your changes to your fork.
Open a pull request.
Commit Message Guidelines
feat: Add multilingual FAQ model
fix: Improve translation caching
docs: Update README with API examples
