pipeline {
    agent any

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
                    def result = sh(script: 'pytest tests/ --maxfail=1 --disable-warnings -q', returnStatus: true)
                    if (result != 0) {
                        echo 'Tests failed. Review the output above.'
                        error("Tests failed with exit code: ${result}")
                    } else {
                        echo 'All tests passed!'
                    }
                }
            }
        }
        stage('Build Artifacts') {
            steps {
                echo 'Building artifacts...'
                // Add your build commands here
            }
        }
        stage('Deploy') {
            steps {
                script {
                    echo "Deploying to ${params.ENVIRONMENT}..."
                    if (params.ENVIRONMENT == 'production') {
                        echo 'Deploying to Production...'
                    } else {
                        echo "Deploying to ${params.ENVIRONMENT}..."
                    }
                }
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
            echo 'Rolling back to the last stable version...'
            // Add rollback commands here
        }
    }
}
