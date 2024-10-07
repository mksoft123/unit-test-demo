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

        stage('Start MongoDB') {
            steps {
                script {
                    // Run MongoDB in a Docker container
                    sh 'docker run --name mongo-test -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=root mongo'
                    
                    // Wait for MongoDB to be ready
                    sleep(time: 10, unit: 'SECONDS') // Adjust if needed
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests within the Docker container with PYTHONPATH set
                    sh 'docker run --rm --link mongo-test:mongo -e MONGO_URI=mongodb://root:root@mongo:27017/mydb?authSource=admin -e PYTHONPATH=/app my-python-app pytest -v /app/tests/test_crud.py'
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    // Stop and remove MongoDB container after tests
                    sh 'docker stop mongo-test'
                    sh 'docker rm mongo-test'
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
        // always {
        //     script {
        //         // Cleanup any remaining Docker containers
        //         sh 'docker ps -a -q | xargs docker rm -f || true'
        //     }
        // }
    }
}

