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
                dir('my-microservices') {
                    dir('user-service') {
                        sh '''
                        python3 --version
                        dpkg -l | grep python3.11-venv
                        python3.11 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip --break-system-packages
                        pip3 install --break-system-packages -r requirements.txt
                        pytest tests/ --maxfail=1 --disable-warnings
                        docker build -t user-service:latest .
                        '''
                    }
                }
            }
        }
        stage('Test & Build Order Service') {
            steps {
                dir('my-microservices') {
                    dir('order-service') {
                    sh '''
                    python3.11 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip --break-system-packages
                    pip3 install --break-system-packages -r requirements.txt
                    pytest tests/ --maxfail=1 --disable-warnings
                    docker build -t order-service:latest .
                    '''
                    }
                }
            }
        }
        stage('Push Docker Images') {
            steps {
                withCredentials([string(credentialsId: '6cc4b590-b6e2-4a46-b673-9b272abe41ec', variable: 'DOCKER_TOKEN')]) {
                    script {
                        sh 'echo "$DOCKER_TOKEN" | docker login --username pbednarski --password-stdin'
                        sh 'docker tag user-service:latest pbednarski/user-service:latest'
                        sh 'docker push pbednarski/user-service:latest'
                        sh 'docker tag order-service:latest pbednarski/order-service:latest'
                        sh 'docker push pbednarski/order-service:latest'
                    }
                }
            }
        }
    }
}
