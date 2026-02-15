pipeline {

    agent any

    environment {
        IMAGE_NAME = "colorado_motor_vechile"
        KUBECONFIG = "/var/jenkins_home/.kube/config"
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
                sh '''
                kubectl get nodes
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image inside Minikube Docker daemon..."
                sh '''
                eval $(minikube docker-env)
                docker build -t $IMAGE_NAME .
                docker images | grep $IMAGE_NAME
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying application to Kubernetes..."
                sh '''
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                '''
            }
        }

        stage('Wait for Pods') {
            steps {
                echo "Waiting for pods to become ready..."
                sh '''
                sleep 10
                kubectl get pods
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                echo "Deployment status:"
                sh '''
                kubectl get deployment
                kubectl get pods
                kubectl get services
                '''
            }
        }

    }

    post {

        success {
            echo "Pipeline completed successfully. Application deployed."
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
