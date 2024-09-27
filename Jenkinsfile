pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                git 'https://github.com/mksoft123/unit-test-demo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Activate virtual environment if needed
                    sh '''
                    # If using a virtual environment, activate it here
                    # source /path/to/venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    def testResult = sh(script: 'pytest tests/', returnStatus: true)
                    if (testResult != 0) {
                        currentBuild.result = 'FAILURE'
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
