echo 'maneesh'
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/mksoft123/unit-test-demo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run pytest and capture the exit status
                    def testResult = sh(script: 'pytest tests/', returnStatus: true)
                    if (testResult != 0) {
                        currentBuild.result = 'FAILURE' // Mark the build as failure
                        error("Tests failed with exit code: ${testResult}")
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
