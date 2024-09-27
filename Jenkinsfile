pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        
        stage('Check Python Version') {
            steps {
                script {
                    // Check for Python version
                    sh 'python3 --version || python --version'
                }
            }
        }

        stage('Create Virtual Environment') {
            steps {
                script {
                    // Create virtual environment
                    sh 'python3 -m venv venv || python -m venv venv'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests
                    sh 'pytest'
                }
            }
        }

        stage('Build Artifacts') {
            steps {
                script {
                    // Build artifacts
                    sh 'echo "Building artifacts..."'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy application
                    sh 'echo "Deploying..."'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
        }
        failure {
            echo 'Build failed. Deployment aborted.'
        }
    }
}
