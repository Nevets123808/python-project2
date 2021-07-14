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
                sh "sudo docker-compose up -d --build"
            }
        }
        stage('Test'){
            steps{
                sh "echo 'testing'"
            }
        }
        stage('Push Containers'){
            steps {
            sh "sudo docker-compose push"
            }
        }
        stage('Pull to swarm'){
            steps {
            sh "scp ${workspace}/docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml"
            sh """ssh jenkins@swarm-manager
            sudo docker stack deploy --compose-file docker-compose.yaml app_stack"""
            }
        }
    }
}