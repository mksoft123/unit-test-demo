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
                    def pythonVersion = sh(script: 'python3 --version', returnStdout: true).trim()
                    echo "Python version: ${pythonVersion}"
                }
            }
        }
        
        stage('Create Virtual Environment') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
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
                    echo 'Building artifacts...'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying application...'
                }
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
            sh 'rm -rf venv' // Optional: remove virtual environment
        }
        failure {
            echo 'Build failed. Deployment aborted.'
        }
    }
    
    options {
        disableConcurrentBuilds() // Optional: prevent concurrent builds
    }
    
    // Optional: run this pipeline only on the master branch
    when {
        branch 'master'
    }
}
