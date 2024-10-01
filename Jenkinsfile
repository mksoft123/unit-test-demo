pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/mksoft123/unit-test-demo.git'
            }
        }
        stage('Check Environment') {
            steps {
                script {
                    sh 'python3 --version'
                    sh 'docker --version'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def testResult = sh(script: 'python3 -m unittest discover tests', returnStatus: true)
                    if (testResult != 0) {
                        error 'Unit tests failed, aborting build.'
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t my-python-app .'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker run -d --name my-python-app -p 8080:8080 -v $WORKSPACE/data:/app/data my-python-app'
                }
            }
        }
    }
    post {
        always {
            script {
                sh 'docker rm -f my-python-app || true'
            }
            cleanWs()
        }
        success {
            echo 'Build and tests were successful!'
        }
        failure {
            echo 'Build failed, check logs for details.'
        }
    }
}
