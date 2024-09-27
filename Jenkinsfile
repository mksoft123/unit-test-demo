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
                    // Capture and log the Python version
                    def pythonVersion = sh(script: 'python3 --version', returnStdout: true).trim()
                    echo "Python version: ${pythonVersion}"
                }
            }
        }
        
        stage('Create Virtual Environment') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv venv'
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    // Activate the virtual environment and install dependencies
                    sh '''
                    source venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    // Run your test suite
                    sh '''
                    source venv/bin/activate
                    pytest
                    '''
                }
            }
        }
        
        stage('Build Artifacts') {
            steps {
                script {
                    // Add your build commands here
                    echo 'Building artifacts...'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    // Add your deployment commands here
                    echo 'Deploying application...'
                }
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
            // Cleanup steps if needed
        }
        failure {
            echo 'Build failed. Deployment aborted.'
        }
    }
}
