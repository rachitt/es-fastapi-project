
# FastAPI Project

This repository contains a project that demonstrates the integration of **Elasticsearch** with **FastAPI**, a modern Python web framework. The project enables the creation, indexing, and querying of documents in Elasticsearch through a FastAPI-based RESTful API.


## Project Overview

This project allows users to perform CRUD operations on documents stored in Elasticsearch using FastAPI. It demonstrates how to efficiently connect to an Elasticsearch cluster and perform document indexing, searching, updating, and deleting via an API.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/rachitt/es-fastapi-project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd es-fastapi-project
   ```

3. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. Ensure you have an Elasticsearch cluster running locally or accessible via a network.

## Dependencies

Ensure you have the following dependencies installed:
- **FastAPI**
- **Elasticsearch-py**
- **Uvicorn** (for running the FastAPI server)

Install project dependencies via:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
2. Access the API documentation by navigating to `http://127.0.0.1:8000/docs`.

3. Use the Swagger UI to test the API endpoints.

## API Endpoints

- `GET /documents/{id}`: Retrieve a document by ID.
- `POST /documents/`: Create a new document and index it in Elasticsearch.
- `PUT /documents/{id}`: Update an existing document by ID.
- `DELETE /documents/{id}`: Delete a document by ID.
- `GET /search/`: Search for documents in Elasticsearch based on query parameters.

## Contributing

Contributions are welcome! Please fork this repository, create a new branch, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
