// pipeline {
//     agent any

//     stages {
//         stage('Clone Repository') {
//             steps {
//                 git 'https://github.com/mksoft123/unit-test-demo.git'
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 script {
//                     // Build the Docker image
//                     sh 'docker build -t my-python-app .'
//                 }
//             }
//         }

//         stage('Run Tests') {
//             steps {
//                 script {
//                     // Run tests within the Docker container with PYTHONPATH set
//                     sh 'docker run --rm -e PYTHONPATH=/app my-python-app pytest -v /app/tests/test_crud.py'
//                 }
//             }
//         }




//         stage('Deploy') {
//             when {
//                 expression { currentBuild.result == null } // Only deploy if tests passed
//             }
//             steps {
//                 script {
//                     // Run the application with Docker socket mounted
//                     sh 'docker run -d -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock my-python-app'
//                 }
//             }
//         }
//     }

//     post {
//         success {
//             echo 'Deployment successful!'
//         }
//         failure {
//             echo 'Deployment failed!'
//         }
//     }
// }


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
                    // Run tests within the Docker container with PYTHONPATH set
                    sh 'docker run --rm --link local-mongo:mongo -e MONGO_URI=mongodb://uname:passwd@mongo:27017/mydb?authSource=admin -e PYTHONPATH=/app my-python-app pytest -v /app/tests/test_crud.py'
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
        // Uncomment this block to clean up remaining containers if needed
        // always {
        //     script {
        //         // Cleanup any remaining Docker containers
        //         sh 'docker ps -a -q | xargs docker rm -f || true'
        //     }
        // }
    }
}


