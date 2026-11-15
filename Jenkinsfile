
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out Calculator project'
                sh 'ls -la'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '.venv/bin/python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t calculator-app:${BUILD_NUMBER} .'
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    docker rm -f calculator || true
                    docker run -d \
                    --name calculator \
                    -p 5001:5001 \
                    --restart unless-stopped \
                    calculator-app:${BUILD_NUMBER}
                '''
            }
        }
    }
}
