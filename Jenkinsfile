pipeline {
    agent { 
        dockerfile true
    }
    stages {
        stage('sanity-check') {
            steps {
                sh 'id'
                sh 'pwd'
                sh 'env | sort'
                sh 'find . -name .git -prune -o -print'    
                sh 'python -V'
                sh 'make'
            }
        }
    }
    post {
        success {
            slackSend color: 'good', message: "finish on ${HOSTNAME}: success: michaeldallen/The-Modern-Python-3-Bootcamp"
        }
        failure {
            slackSend color: 'danger', message: "finish on ${HOSTNAME}: failure: finished michaeldallen/The-Modern-Python-3-Bootcamp"
        }
    }
}
