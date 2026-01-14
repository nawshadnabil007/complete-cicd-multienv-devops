# DevOps CI/CD Application

A simple Python Flask application for demonstrating CI/CD pipeline with multi-environment deployment.

## Features

- RESTful API with health check endpoint
- Environment-based configuration
- Dockerized application
- Unit tests included

## Endpoints

- `GET /` - Home endpoint with application info
- `GET /health` - Health check endpoint

## Local Development

### Prerequisites
- Python 3.11+
- pip

### Installation
```bash
pip install -r requirements.txt
```

### Running the Application
```bash
cd src
python app.py
```

The application will start on `http://localhost:3000`

## Testing
```bash
cd src
pytest test_app.py
```

## Docker

### Build Image
```bash
docker build -t devops-app:latest .
```

### Run Container
```bash
docker run -p 3000:3000 devops-app:latest
```

## Environment Variables

- `PORT` - Application port (default: 3000)
- `ENVIRONMENT` - Environment name (dev/staging/prod)
- `VERSION` - Application version