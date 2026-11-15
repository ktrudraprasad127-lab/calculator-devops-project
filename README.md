# calculator-devops-project
# Calculator Web Application – DevOps CI/CD Project

## Project Overview

This project demonstrates an end-to-end DevOps CI/CD pipeline using a Python Flask calculator application.

The application performs addition, subtraction, multiplication, and division on multiple comma-separated numbers.

The project automates dependency installation, testing, Docker image creation, and application deployment using Jenkins.

## Technologies Used

- **Python** – Application development
- **Flask** – Web framework
- **HTML** – User interface
- **Pytest** – Automated testing
- **Git & GitHub** – Version control and source code management
- **Jenkins** – CI/CD automation
- **Docker** – Containerization

## Application Features

- Addition of multiple numbers
- Subtraction of multiple numbers
- Multiplication of multiple numbers
- Division of multiple numbers
- Input validation
- Division-by-zero error handling

## Project Structure

```text
calculator-devops-project/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── README.md
├── .gitignore
├── .dockerignore
│
├── templates/
│   └── index.html
│
└── tests/
    └── test_app.py
```

## CI/CD Pipeline Workflow

The project follows this workflow:

1. **GitHub:** Stores the application source code.
2. **Jenkins Checkout:** Retrieves the latest source code from GitHub.
3. **Install Dependencies:** Installs Python packages using requirements.txt.
4. **Run Tests:** Executes automated tests using Pytest.
5. **Build Docker Image:** Creates a Docker image of the calculator application.
6. **Deploy Application:** Runs the Docker container automatically.

## Jenkins Pipeline Stages

The Jenkins pipeline includes:

- Checkout
- Install Dependencies
- Run Tests
- Build Docker Image
- Deploy Application

## Docker Configuration

Build the Docker image manually:

```bash
docker build -t calculator-app:1.0 .
```

Run the Docker container:

```bash
docker run -d --name calculator -p 5001:5001 calculator-app:1.0
```

Check running containers:

```bash
docker ps
```

Access the application:

http://localhost:5001

## Run the Application Locally

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

## Run Automated Tests

Execute:

```bash
python -m pytest -v
```

The project currently includes six automated tests covering the home page, all four calculator operations, and division by zero.

**Latest Jenkins build:** SUCCESS  
**Automated tests:** 6 PASSED  
**Docker image:** calculator-app:1  
**Container name:** calculator  
**Application port:** 5001

## Repository

GitHub: https://github.com/ktrudraprasad127-lab/calculator-devops-project

## Project Outcome

Successfully implemented an end-to-end CI/CD pipeline that integrates GitHub, Jenkins, Pytest, and Docker to test, build, and deploy a Flask-based calculator application.
Automatic CI/CD triggering is configured using Jenkins Poll SCM.
