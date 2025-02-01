# backend
Django Multi-Language FAQ API with WYSIWYG Editor

Overview

This project is a Django-based application that allows users to manage frequently asked questions (FAQs) with multi-language support and WYSIWYG (What You See Is What You Get) editor integration. It uses the django-ckeditor for rich-text formatting and googletrans for translating FAQ content to multiple languages. Additionally, this project is containerized with Docker for easy deployment.

Key Features

Multi-language FAQ support with dynamic translations.
WYSIWYG editor for rich-text content in FAQ answers.
Efficient FAQ retrieval via REST API with language selection.
Integrated caching mechanism using Redis for translation data.
Docker support for easy containerization and deployment.
Technologies Used
Backend: Django
Database: SQLite (can be replaced with PostgreSQL in production)
Frontend: Django Admin Interface, CKEditor
Cache: Redis
Translation: googletrans (Google Translate API)
Containerization: Docker
API: REST API for managing FAQs
Version Control: Git
Installation Steps
1. Clone the Repository
First, clone the repository to your local machine:

bash
Copy
Edit

git clone https://github.com/your-username/faq-multilingual-django.git
cd faq-multilingual-django

2. Set Up Virtual Environment (Optional)
Create and activate a Python virtual environment for better dependency management.

bash
Copy
Edit

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Install the required Python dependencies using pip.

bash
Copy
Edit
pip install -r requirements.txt
4. Apply Migrations
Run migrations to set up the database.
bash
Copy
Edit
python manage.py migrate

5. Set Up Static and Media Files
Collect static files and set up media directory.
bash
Copy
Edit
python manage.py collectstatic
6. Run the Development Server
Start the development server to test the app locally.

bash
Copy
Edit
python manage.py runserver
Visit http://127.0.0.1:8000 to view the app.

Running with Docker

1. Build the Docker Image
   
Build the Docker image using Docker Compose.
bash
Copy
Edit
docker-compose build
3. Start the Docker Container
   
Run the container and start the application.

bash
Copy
Edit
docker-compose up
This will start the application in a container, and you can access it at http://localhost:8000.

3. Stopping the Docker Container
   
When you're done, you can stop the container with:
bash
Copy
Edit
docker-compose down
API Usage
The application exposes a REST API to manage FAQs. You can interact with the API using curl, Postman, or any HTTP client.

1. Fetch All FAQs (Default Language - English)
   
bash
Copy
Edit
curl http://localhost:8000/api/faqs/

3. Fetch FAQs in Hindi
bash
Copy
Edit
curl http://localhost:8000/api/faqs/?lang=hi

5. Fetch FAQs in Bengali
bash
Copy
Edit
curl http://localhost:8000/api/faqs/?lang=bn

7. Add a New FAQ
To add a new FAQ, make a POST request to the /api/faqs/ endpoint with the following data:
json
Copy
Edit

{
  "question": "What is Docker?",
  "answer": "<p>Docker is a platform for developing, shipping, and running applications.</p>",
  "question_hi": "डॉकर क्या है?",
  "question_bn": "ডকার কি?"
}

Admin Panel

The Django admin panel allows you to manage the FAQs easily.

1. Access the Admin Panel
To access the Django admin panel, navigate to http://127.0.0.1:8000/admin and log in with the superuser credentials.

3. Create a Superuser (If not created)
If you haven't created a superuser, run:

bash
Copy
Edit
python manage.py createsuperuser
Follow the prompts to set up a superuser.

Caching Mechanism
The application uses Redis to cache translations. This improves performance when multiple users request the same FAQ in different languages.

1. Install Redis
If running locally (without Docker), you need to have Redis installed. Download Redis and start the Redis server.
Alternatively, Redis can be run inside a Docker container:
bash
Copy
Edit
docker run -p 6379:6379 redis
Testing
The project includes unit tests for API functionality and model methods.

1. Run Unit Tests
   
Run the tests with:
bash
Copy
Edit
pytest

3. Check for Code Quality
   
The project follows PEP8 conventions. Use flake8 to check the code quality:
bash
Copy
Edit
flake8 .
Contributing
We welcome contributions to this project! Here's how you can contribute:

Fork the repository.

Create a new branch for your feature or bugfix.

Make your changes and commit them with clear, concise messages.

Push your changes to your fork.

Open a pull request.

Commit Message Guidelines

feat: Add multilingual FAQ model

fix: Improve translation caching

docs: Update README with API examples
