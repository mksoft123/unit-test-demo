pipeline {
    agent any

    // Parameters for the pipeline
    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: 'Branch to build')
        choice(name: 'ENVIRONMENT', choices: ['development', 'staging', 'production'], description: 'Deployment environment')
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    def result = sh(script: 'pytest tests/', returnStatus: true)
                    if (result != 0) {
                        error("Tests failed with exit code: ${result}")
                    }
                }
            }
        }
        stage('Build Artifacts') {
            steps {
                // Example: Build Docker image or package application
                echo 'Building artifacts...'
                // Add your build commands here (e.g., docker build)
            }
        }
        stage('Deploy') {
            steps {
                script {
                    echo "Deploying to ${params.ENVIRONMENT}..."
                    // Add deployment commands based on environment
                    if (params.ENVIRONMENT == 'production') {
                        // Example: Deploy to production
                        echo 'Deploying to Production...'
                    } else {
                        // Example: Deploy to staging or development
                        echo "Deploying to ${params.ENVIRONMENT}..."
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Add any cleanup steps here if necessary
        }
        success {
            echo 'Build succeeded. Ready for deployment.'
            // Notify team of success
            // Example: sh 'notify_success.sh'
        }
        failure {
            echo 'Build failed. Deployment aborted.'
            // Notify team of failure
            // Example: sh 'notify_failure.sh'
            // Optionally, rollback if applicable
            echo 'Rolling back to the last stable version...'
            // Add rollback commands here
        }
    }
}
