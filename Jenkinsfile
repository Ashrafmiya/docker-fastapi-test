pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Deploy Containers') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }

        stage('Verify Services') {
            steps {
                sh '''
                sleep 10
                curl -f http://localhost:8000 || exit 1
                curl -f http://localhost:9090 || exit 1
                curl -f http://localhost:3000 || exit 1
                '''
            }
        }

        stage('Configure Grafana') {
            steps {
                sh '''
                curl -s -X GET http://localhost:3000/api/datasources/name/Prometheus -u admin:admin | grep "Prometheus" || \
                curl -X POST http://localhost:3000/api/datasources \
                  -H "Content-Type: application/json" \
                  -u admin:admin \
                  -d '{"name":"Prometheus","type":"prometheus","url":"http://prometheus:9090","access":"proxy","isDefault":true}'
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed. Check logs for details.'
        }
    }
}
