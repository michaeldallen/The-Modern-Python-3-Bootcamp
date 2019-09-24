pipeline {
    agent { 
        dockerfile true
    }
    stages {
        stage ('init') {
            steps {
                slackSend color: 'good', message: "start ${JOB_NAME} on ${HOSTNAME}: https://github.com/michaeldallen/The-Modern-Python-3-Bootcamp/commit/${GIT_COMMIT}"
            }
        }
        stage('sanity-check') {
            steps {
                sh 'id'
                sh 'pwd'
                sh 'env | sort'
                sh 'find . -name .git -prune -o -print'    
                sh 'python3 -V'
                sh 'make'
            }
        }
        stage('pytest') {
            steps {
                sh "make pytest"
            }
        }
        
    }
    post {
        success {
            slackSend color: 'good', message: "finish on ${HOSTNAME}: success: ${JOB_NAME}"
        }
        failure {
            slackSend color: 'danger', message: "finish on ${HOSTNAME}: failure: finished ${JOB_NAME}"
        }
    }
}
