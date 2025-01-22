pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Fetch code from the Git repository
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image
                sh 'docker-compose build'
            }
        }

        stage('Run Application') {
            steps {
                // Start the application container
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            // Clean up containers after the build
            sh 'docker-compose down'
        }
    }
}
