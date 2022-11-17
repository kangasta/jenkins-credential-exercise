pipeline {
    agent any
    stages {
        stage("Test") {
            agent { dockerfile { reuseNode true } }
            steps {
                sh "robot -N '${env.JOB_BASE_NAME} ${BUILD_DISPLAY_NAME}' -d robot_output --nostatusrc ."
            }
        }
    }
    post {
        success {
            robot outputPath: 'robot_output', onlyCritical: false, passThreshold: 100.0, unstableThreshold: 0.0
        }
    }
}
