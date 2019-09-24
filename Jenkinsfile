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
        
        stage('build') {
            steps {
                sh 'make docker.build'
            }
        }
        stage('publish') {
            steps {
                sh 'docker tag m2c-jenkins-${DPKG_ARCH} michaeldallen/m2c-jenkins-${DPKG_ARCH}'
                withDockerRegistry([ credentialsId: "michaeldallen-at-dockerhub", url: "" ]) {
                    sh 'docker push michaeldallen/m2c-jenkins-${DPKG_ARCH}'
                }
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
