pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code from repository...'
                // Fetch code from the Git repository
                checkout scm
            }
        }

        stage('Build and Start Containers') {
            steps {
                echo 'Building and starting Docker containers...'
                // Build and start all services in docker-compose.yml
                sh 'docker-compose up -d --build'
            }
        }

        stage('Verify FastAPI Application') {
            steps {
                echo 'Verifying the FastAPI application is running...'
                // Check if FastAPI is running
                sh '''
                sleep 10
                curl -X GET http://localhost:8000 || exit 1
                '''
            }
        }

        stage('Verify Prometheus') {
            steps {
                echo 'Verifying Prometheus is running...'
                // Check if Prometheus is running
                sh '''
                curl -X GET http://localhost:9090 || exit 1
                '''
            }
        }

        stage('Verify Grafana') {
            steps {
                echo 'Verifying Grafana is running...'
                // Check if Grafana is running
                sh '''
                curl -X GET http://localhost:3000 || exit 1
                '''
            }
        }

        stage('Post Deployment Configuration') {
            steps {
                echo 'Configuring Prometheus as Grafana data source...'
                // Add Prometheus as a data source in Grafana via Grafana HTTP API
                sh '''
                curl -X POST http://localhost:3000/api/datasources \
                -H "Content-Type: application/json" \
                -u admin:admin \
                -d '{
                    "name": "Prometheus",
                    "type": "prometheus",
                    "url": "http://prometheus:9090",
                    "access": "proxy",
                    "isDefault": true
                }'
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment pipeline executed successfully. Application and monitoring tools are running.'
        }

        failure {
            echo 'Deployment pipeline failed. Check logs for details.'
        }
    }
}
