# Smart Content Recommendation and Generation Platform

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)

- Learn how to create it on [YouTube](https://youtu.be/Jn1O3SL1jO0)

The **Smart Content Recommendation and Generation Platform** is a Django-based web application that leverages the **Ollama API** to generate and recommend content. It provides features like AI-powered content generation, summarization, and tag-based recommendations. Users can register, authenticate, and manage their generated content seamlessly.

---

## Features

- **User Authentication**: Secure JWT-based authentication for user registration and login.
- **Content Generation**: Generate high-quality blog posts or articles using the Ollama API.
- **Content Summarization**: Summarize long articles or blog posts into concise text.
- **Tag-Based Recommendations**: Get recommendations for similar content based on tags.
- **Pagination**: Paginated list of user-generated content for better usability.
- **Error Handling**: Robust error handling for API requests and Ollama integration.

---

## Tech Stack

- **Backend**: Django, Django Rest Framework (DRF)
- **AI Integration**: Ollama (Llama 3.2 model)
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: SQLite (can be replaced with PostgreSQL or MySQL)
- **Pagination**: DRF's built-in pagination

---

## Installation

### Prerequisites

- Python 3.12+
- Pip (Python package manager)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:KNehe/smart_content_platform.git
   cd smart-content-platform
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the API**:
   - The API will be available at `http://localhost:8000/api/`.

---

## API Endpoints

### Authentication
- **Register User**:
  - `POST /api/register/`
  - Request Body:
    ```json
    {
      "username": "testuser",
      "password": "testpass123",
      "email": "test@example.com"
    }
    ```

- **Login (Get JWT Token)**:
  - `POST /api/token/`
  - Request Body:
    ```json
    {
      "username": "testuser",
      "password": "testpass123"
    }
    ```

- **Refresh JWT Token**:
  - `POST /api/token/refresh/`
  - Request Body:
    ```json
    {
      "refresh": "your-refresh-token"
    }
    ```

### Content Management
- **Generate Content**:
  - `POST /api/generate-content/`
  - Request Body:
    ```json
    {
      "topic": "Quantum Computing"
    }
    ```

- **Summarize Content**:
  - `POST /api/summarize-content/`
  - Request Body:
    ```json
    {
      "text": "A long article about climate change..."
    }
    ```

- **List User Content**:
  - `GET /api/user-content/`

- **Get Recommendations**:
  - `GET /api/recommendations/<content_id>/`

---

## Usage Example

1. **Register a User**:
   ```bash
   curl -X POST http://localhost:8000/api/register/ \
        -H "Content-Type: application/json" \
        -d '{"username": "testuser", "password": "testpass123", "email": "test@example.com"}'
   ```

2. **Login and Get JWT Token**:
   ```bash
   curl -X POST http://localhost:8000/api/token/ \
        -H "Content-Type: application/json" \
        -d '{"username": "testuser", "password": "testpass123"}'
   ```

3. **Generate Content**:
   ```bash
   curl -X POST http://localhost:8000/api/generate-content/ \
        -H "Authorization: Bearer YOUR_JWT_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{"topic": "Artificial Intelligence"}'
   ```

4. **Get Recommendations**:
   ```bash
   curl -X GET http://localhost:8000/api/recommendations/1/ \
        -H "Authorization: Bearer YOUR_JWT_TOKEN"
   ```

---

## Project Structure

```
smart-content-platform/
├── content/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── services.py
│   ├── urls.py
│   └── views.py
├── smart_content_platform/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Django](https://www.djangoproject.com/) for the backend framework.
- [Ollama](https://ollama.com/) for the AI-powered content generation.
- [DRF](https://www.django-rest-framework.org/) for building RESTful APIs.