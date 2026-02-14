pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                bat 'git clone https://github.com/PranuthHM/ai-k8s-data-analytics-platform.git'
            }
        }

        stage('Enter Project Directory') {
            steps {
                dir('ai-k8s-data-analytics-platform') {
                    bat 'docker build -t colorado_motor_vechile .'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                dir('ai-k8s-data-analytics-platform') {
                    bat 'kubectl apply -f deployment.yaml'
                    bat 'kubectl apply -f service.yaml'
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'kubectl get pods'
                bat 'kubectl get services'
            }
        }

    }
}
