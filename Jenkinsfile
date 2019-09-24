pipeline {
    agent { 
        dockerfile true
    }
    stages {
        stage('init') {
            steps {
                slackSend color: 'good', message: "start on ${HOSTNAME}: michaeldallen/m2c-jenkins-${DPKG_ARCH}"           
            }
        }
        stage('sanity-check') {
            steps {
                sh 'id'
                sh 'pwd'
                sh 'env | sort'
                sh 'find . -name .git -prune -o -print'    
                sh 'make'
            }
        }
    }
    post {
        success {
            slackSend color: 'good', message: "finish on ${HOSTNAME}: success: michaeldallen/m2c-jenkins-${DPKG_ARCH}"
        }
        failure {
            slackSend color: 'danger', message: "finish on ${HOSTNAME}: failure: finished michaeldallen/m2c-jenkins-${DPKG_ARCH}"
        }
    }
}
