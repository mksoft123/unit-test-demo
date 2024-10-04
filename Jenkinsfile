pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/mksoft123/unit-test-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t my-python-app .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests within the Docker container
                    sh 'docker run --rm -v $(pwd):/app my-python-app pytest -v /app/tests/test_crud.py'
                }
            }
        }


        stage('Deploy') {
            when {
                expression { currentBuild.result == null } // Only deploy if tests passed
            }
            steps {
                script {
                    // Run the application with Docker socket mounted
                    sh 'docker run -d -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock my-python-app'
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
