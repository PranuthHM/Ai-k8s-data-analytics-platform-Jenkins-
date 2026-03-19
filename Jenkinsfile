pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/PranuthHM/ai-k8s-data-analytics-platform-jenkins-.git'
            }
        }

        stage('Fix Docker Config') {
            steps {
                sh '''
                mkdir -p ~/.docker
                echo '{ "auths": {} }' > ~/.docker/config.json
                '''
            }
        }

        stage('Start Minikube') {
            steps {
                sh '''
                minikube start --driver=docker
                minikube addons enable metrics-server
                '''
            }
        }

        stage('Connect Docker') {
            steps {
                sh '''
                eval $(minikube docker-env)
                docker build -t colorado_motor_vechile .
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                kubectl rollout restart deployment colorado-sales-deployment
                '''
            }
        }

        stage('Show Pods') {
            steps {
                sh 'kubectl get pods'
            }
        }
    }
}