pipeline {

    agent any

    environment {
        IMAGE_NAME = "colorado_motor_vechile"
    }

    stages {

        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/PranuthHM/ai-k8s-data-analytics-platform.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'eval $(minikube docker-env)'
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }

        stage('Verify') {
            steps {
                sh 'kubectl get pods'
                sh 'kubectl get services'
            }
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
