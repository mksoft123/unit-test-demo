pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run pytest and capture the result
                    def result = sh(script: 'pytest tests/', returnStatus: true)
                    // Check the exit code of pytest
                    if (result != 0) {
                        currentBuild.result = 'FAILURE' // Mark the build as failed
                        error("Tests failed with exit code: ${result}") // Stop the pipeline
                    } else {
                        echo "Tests passed successfully!"
                    }
                }
            }
        }
        stage('Build Artifacts') {
            steps {
                echo 'Building artifacts...'
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying to environment..."
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
        }
        success {
            echo 'Build succeeded. Ready for deployment.'
        }
        failure {
            echo 'Build failed. Deployment aborted.'
        }
    }
}
