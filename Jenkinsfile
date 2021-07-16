pipeline {
    agent any
    environment {
        DATABASE_URI="mysql+pymysql://root:TrivialMoose@34.142.119.164:3306/project"//credentials('DATABASE_URI')
        SECRET_KEY=credentials('SECRET_KEY')
    }
    stages {
        stage('Configure machines') {
            steps{
                sh "~/.local/bin/ansible-playbook -i inventory.yaml ansible-playbook.yaml"
            }
        }
        stage('Build containers'){
            steps{
                sh "docker-compose up -d --build"
            }
        }
        stage('Test'){
            steps{
                sh "cd ./flaskapp && pytest --cov=app --cov-report html"
                sh "cd ./sheetmake && pytest --cov=app --cov-report html"
                sh "cd ./skilltag && pytest --cov=app --cov-report html"
                sh "cd ./specialgen && pytest --cov=app --cov-report html"
                archiveArtifacts artifacts: 'flaskapp/htmlcov/, specialgen/htmlcov/, skilltag/htmlcov/, sheetmake/htmlcov/', followSymlinks: false
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
            sh "ssh jenkins@swarm-manager 'docker stack deploy --compose-file docker-compose.yaml app_stack'"
            }
        }
    }
}