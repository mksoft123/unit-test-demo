// // // pipeline {
// // //     agent any

// // //     stages {
// // //         stage('Clone Repository') {
// // //             steps {
// // //                 git 'https://github.com/mksoft123/unit-test-demo.git'
// // //             }
// // //         }

// // //         stage('Build Docker Image') {
// // //             steps {
// // //                 script {
// // //                     // Build the Docker image
// // //                     sh 'docker build -t my-python-app .'
// // //                 }
// // //             }
// // //         }

// // //         stage('Run Tests') {
// // //             steps {
// // //                 script {
// // //                     // Run tests within the Docker container with PYTHONPATH set
// // //                     sh 'docker run --rm -e PYTHONPATH=/app my-python-app pytest -v /app/tests/test_crud.py'
// // //                 }
// // //             }
// // //         }




// // //         stage('Deploy') {
// // //             when {
// // //                 expression { currentBuild.result == null } // Only deploy if tests passed
// // //             }
// // //             steps {
// // //                 script {
// // //                     // Run the application with Docker socket mounted
// // //                     sh 'docker run -d -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock my-python-app'
// // //                 }
// // //             }
// // //         }
// // //     }

// // //     post {
// // //         success {
// // //             echo 'Deployment successful!'
// // //         }
// // //         failure {
// // //             echo 'Deployment failed!'
// // //         }
// // //     }
// // // }

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
//                     try {
//                         sh 'docker run --rm --link local-mongo:mongo -e MONGO_URI=mongodb://root:root@mongo:27017/mydb?authSource=admin -e PYTHONPATH=/app my-python-app pytest -v /app/tests/test_crud.py'
//                     } catch (Exception e) {
//                         error "Tests failed: ${e.getMessage()}"
//                     }
//                 }
//             }
//         }

//         stage('Deploy') {
//             when {
//                 expression { currentBuild.result == null } // Only deploy if tests passed
//             }
//             steps {
//                 script {
//                     try {
//                         // Change the port if necessary
//                         sh 'docker run -d -p 8081:8080 -v /var/run/docker.sock:/var/run/docker.sock my-python-app'
//                     } catch (Exception e) {
//                         error "Deployment failed: ${e.getMessage()}"
//                     }
//                 }
//             }
//         }
//     }

//     post {
//         success {
//             echo 'Deployment successful!'
//         }
//         failure {
//             echo 'Deployment failed! Check logs for details.'
//         }
//         always {
//             script {
//                 // Print out relevant logs for debugging if necessary
//                 echo "Current build status: ${currentBuild.result}"
//             }
//         }
//     }
// }


//         // Uncomment this block to clean up remaining containers if needed
//         // always {
//         //     script {
//         //         // Cleanup any remaining Docker containers
//         //         sh 'docker ps -a -q | xargs docker rm -f || true'
//         //     }
//         // }
//     }
// }

// // pipeline {
// //     agent any

// //     stages {
// //         stage('Clone Repository') {
// //             steps {
// //                 git 'https://github.com/mksoft123/unit-test-demo.git'
// //             }
// //         }

// //         stage('Build Docker Image') {
// //             steps {
// //                 script {
// //                     // Check if the image already exists
// //                     def imageExists = sh(script: "docker images -q my-python-app", returnStdout: true).trim()

// //                     if (!imageExists) {
// //                         // Build the Docker image if it doesn't exist
// //                         sh 'docker build -t my-python-app .'
// //                     } else {
// //                         echo "Docker image 'my-python-app' already exists. Skipping build."
// //                     }
// //                 }
// //             }
// //         }

// //         stage('Run Tests') {
// //             steps {
// //                 script {
// //                     // Run the tests and capture the output
// //                     def testResult = sh(script: 'docker run --rm --link local-mongo:mongo -e MONGO_URI=mongodb://root:root@mongo:27017/mydb?authSource=admin -e PYTHONPATH=/app my-python-app pytest -v /app/tests/test_crud.py', returnStatus: true)
                    
// //                     // Check if tests passed
// //                     if (testResult != 0) {
// //                         error("Tests failed. Please check the output for details.")
// //                     }
// //                 }
// //             }
// //         }

// //         stage('Deploy') {
// //             when {
// //                 expression { currentBuild.result == null } // Only deploy if tests passed
// //             }
// //             steps {
// //                 script {
// //                     // Check if the container is already running
// //                     def existingContainer = sh(script: "docker ps -q -f name=my-python-app", returnStdout: true).trim()
                    
// //                     if (existingContainer) {
// //                         echo "Container 'my-python-app' is already running. Skipping deployment."
// //                     } else {
// //                         // Run the application using the existing image
// //                         sh 'docker run -d -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock --name my-python-app my-python-app'
// //                     }
// //                 }
// //             }
// //         }
// //     }

// //     post {
// //         success {
// //             echo 'Deployment successful!'
// //         }
// //         failure {
// //             echo 'Deployment failed due to an error in the pipeline.'
// //         }
// //         always {
// //             script {
// //                 if (currentBuild.result == 'FAILURE') {
// //                     echo 'Tests failed. Please review the console output above for details.'
// //                 }
// //             }
// //         }
// //     }
// // }

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
                    sh 'docker run --rm --link local-mongo:mongo -e MONGO_URI=mongodb://root:root@mongo:27017/mydb?authSource=admin -e PYTHONPATH=/app my-python-app pytest -v /app/tests/test_crud.py'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    def containerName = "my-python-app-container"

                    // Stop and remove the existing container if it exists
                    def running = sh(script: "docker ps -q -f name=${containerName}", returnStdout: true).trim()
                    if (running) {
                        sh "docker stop ${containerName}"
                        sh "docker rm ${containerName}"
                    }

                    // Run a new container with the updated image
                    sh "docker run -d --name ${containerName} -p 8081:8080 -v /var/run/docker.sock:/var/run/docker.sock my-python-app"
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed! Check logs for details.'
        }
        always {
            echo "Current build status: ${currentBuild.result}"
        }
    }
}

