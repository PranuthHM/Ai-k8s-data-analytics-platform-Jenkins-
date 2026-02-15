pipeline {

    agent any

    environment {
        IMAGE_NAME = "colorado_motor_vechile"
    }

    stages {

        stage('Clone') {
            steps {
                echo "Cloning repository..."
                git branch: 'main', url: 'https://github.com/PranuthHM/ai-k8s-data-analytics-platform.git'
            }
        }

        stage('Verify Kubernetes Connection') {
            steps {
                echo "Checking Kubernetes cluster access..."
                sh 'kubectl get nodes'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes..."
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }

        stage('Verify Deployment') {
            steps {
                echo "Verifying deployment..."
                sh 'kubectl get pods'
                sh 'kubectl get services'
            }
        }

    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs."
        }
    }

}



// pipeline {
//     agent any

//     environment {
//         IMAGE_NAME = "colorado_motor_vechile"
//     }

//     stages {

//         stage('Clean Workspace') {
//             steps {
//                 deleteDir()
//             }
//         }

//         stage('Clone Repository') {
//             steps {
//                 git branch: 'main' , url: 'https://github.com/PranuthHM/ai-k8s-data-analytics-platform.git'
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 sh 'docker build -t coloraedo .'
//             }
//         }

//         stage('Deploy to Kubernetes') {
//             steps {
//                 sh 'kubectl apply -f deployment.yaml'
//                 sh 'kubectl apply -f service.yaml'
//             }
//         }

//         stage('Verify Deployment') {
//             steps {
//                 sh 'kubectl get pods'
//                 sh 'kubectl get services'
//             }
//         }

//     }
// }
