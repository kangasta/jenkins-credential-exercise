pipeline {
    agent any
    stages {
        stage("Load dockerfile") {
            steps {
                git 'https://gist.github.com/1011d8c3d0e84b4ed914bdf66380bc02.git'
            }
        }
        stage("Test") {
            agent { dockerfile { reuseNode true } }
            steps {
                sh "robot -d robot_output --nostatusrc ."
            }
        }
    }
}
