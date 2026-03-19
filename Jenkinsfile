pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/PranuthHM/Ai-k8s-data-analytics-platform-Jenkins-.git'
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

        stage('Build Docker Image') {
            steps {
                sh '''
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

        stage('Verify Deployment') {
            steps {
                sh 'kubectl get pods'
            }
        }
    }
}