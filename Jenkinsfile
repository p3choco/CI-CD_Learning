pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/p3choco/CI-CD_Learning.git', branch: 'master'
            }
        }
        stage('Test & Build User Service') {
            steps {
                dir('user-service') {
                    sh 'pip install -r requirements.txt'
                    sh 'pytest tests/ --maxfail=1 --disable-warnings'
                    sh 'docker build -t user-service:latest .'
                }
            }
        }
        stage('Test & Build Order Service') {
            steps {
                dir('order-service') {
                    sh 'pip install -r requirements.txt'
                    sh 'pytest tests/ --maxfail=1 --disable-warnings'
                    sh 'docker build -t order-service:latest .'
                }
            }
        }
        stage('Push Docker Images') {
            steps {
                script {
                    sh 'docker login -u $DOCKER_USER -p $DOCKER_PASS'
                    sh 'docker tag user-service:latest $DOCKER_USER/user-service:latest'
                    sh 'docker push $DOCKER_USER/user-service:latest'

                    sh 'docker tag order-service:latest $DOCKER_USER/order-service:latest'
                    sh 'docker push $DOCKER_USER/order-service:latest'
                }
            }
        }
    }
}
