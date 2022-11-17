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
    post {
        success {
            robot outputPath: 'robot_output', onlyCritical: false, passThreshold: 100.0, unstableThreshold: 0.0
        }
    }
}
