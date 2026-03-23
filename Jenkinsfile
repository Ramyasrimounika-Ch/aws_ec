pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        USERNAME = "2023bcs0223mounika"
        REG = "2023BCS0223"
        ROLL = "223"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Ramyasrimounika-Ch/aws_ec.git'
            }
        }

        stage('Build Images') {
            steps {
                sh """
                docker build -t $USERNAME/${REG}_${ROLL}_frontend:latest ./frontend
                docker build -t $USERNAME/${REG}_${ROLL}_backend:latest ./backend
                """
            }
        }

        stage('Push to DockerHub') {
            steps {
                sh """
                echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin

                docker push $USERNAME/${REG}_${ROLL}_frontend:latest
                docker push $USERNAME/${REG}_${ROLL}_backend:latest
                """
            }
        }
    }
}
