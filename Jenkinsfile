pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                 'docker-compose build'
            }
        }

        stage('Run Application') {
            steps {
                 'docker-compose up -d'
            }
        }
    }

    post {
        always {
             'docker-compose down'
        }
    }
}
