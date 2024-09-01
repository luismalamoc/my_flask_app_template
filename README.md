
# My Flask Application Template

This project is a modular Flask application with a clean separation of concerns, using dependency injection via the `injector` library. It includes namespaces to group related routes, and it leverages SQLAlchemy for the data layer and Pydantic for data validation and serialization.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Extending the Application](#extending-the-application)
- [Docker usage](#docker-usage)

## Project Structure

```
my_flask_app/
├── app.py
├── config/
│   ├── __init__.py
│   ├── development.py
│   ├── production.py
│   └── testing.py
├── application_context/
│   ├── __init__.py
│   └── injector.py
├── resources/
│   ├── __init__.py
│   └── user_resource.py
├── services/
│   ├── __init__.py
│   └── user_service.py
├── repositories/
│   ├── __init__.py
│   ├── base.py
│   └── user_repository.py
├── schemas/
│   ├── __init__.py
│   └── user_schema.py
├── mappers/
│   ├── __init__.py
│   └── user_mapper.py
├── models/
│   ├── __init__.py
│   └── user.py
├── requirements.txt
└── .env
```

### Directories

- **config/**: Contains configuration files for different environments (development, production, testing).
- **application_context/**: Manages dependency injection using the `injector` library.
- **resources/**: Contains classes that handle HTTP requests, grouped by functionality (e.g., `UserResource`).
- **services/**: Contains business logic (e.g., `UserService`).
- **repositories/**: Contains SQLAlchemy models and repositories for database interaction (e.g., `UserRepository`).
- **schemas/**: Contains Pydantic schemas for data validation and serialization (e.g., `UserSchema`).
- **mappers/**: Contains mappers that convert SQLAlchemy models to Pydantic schemas (e.g., `UserMapper`).
- **models/**: Contains SQLAlchemy models (e.g., `User`).

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/my-flask-app.git
   cd my-flask-app
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root of the project and add your environment-specific variables, such as `DATABASE_URI`.

   Example:
   ```
   DATABASE_URI=sqlite:///dev.db
   ```

## Configuration

Configuration files are located in the `config/` directory. You can modify these files according to your environment (development, production, testing).

- **development.py**: Configuration for development environment.
- **production.py**: Configuration for production environment.
- **testing.py**: Configuration for testing environment.

## Running the Application

1. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```

2. **Run the Flask application**:
   ```bash
   python app.py
   ```

   The application will be available at `http://localhost:5000`.

## Usage

### Endpoints

- **GET /users/\<int:user_id\>**: Retrieve user details by ID.

### Example Request

```bash
curl http://localhost:5000/users/1
```

### Response

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

## Extending the Application

### Adding New Features

1. **Create a new resource** in the `resources/` directory.
2. **Define the business logic** in the `services/` directory.
3. **Create or update the repository** in the `data_layer/` directory.
4. **Create or update Pydantic schemas** in the `schemas/` directory.
5. **Map models to schemas** in the `mappers/` directory.
6. **Register routes** in the `app.py` file by extending the namespace concept.

### Example

To add a new feature (e.g., managing posts):

1. Create `post_resource.py` in `resources/`.
2. Create `post_service.py` in `services/`.
3. Create `post_repository.py` in `data_layer/`.
4. Create `post_schema.py` in `schemas/`.
5. Create `post_mapper.py` in `mappers/`.
6. Register the new routes in `app.py`.

## Docker usage

```
docker build -t my-flask-app .

docker run -p 5000:5000 my-flask-app
```

## Contributing

Feel free to submit issues, fork the repository, and send pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
