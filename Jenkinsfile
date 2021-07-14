pipeline {
    agent any
    stages {
        stage('Configure machines') {
            steps{
                sh "cat ansible-playbook.yaml"
                sh "~/.local/bin/ansible-playbook -i inventory.yaml ansible-playbook.yaml"
            }
        }
        stage('Build containers'){
            steps{
                sh "docker-compose -d up --build"
            }
        }
        stage('Test'){
            steps{
                sh "echo 'testing'"
            }
        }
        stage('Push Containers'){
            steps {
            sh "docker-compose push"
            }
        }
        stage('Pull to swarm'){
            steps {
            sh "scp /home/Steven/python-project2/docker-compose.yaml Steven@swarm-manager:/home/Steven/docker-compose.yaml"
            sh "ssh Steven@swarm-manager && docker stack deploy --compose-file docker-compose.yaml app_stack"
            }
        }
    }
}