pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright') {
            steps {
                bat 'python -m playwright install'
            }
        }

        stage('Run tests') {
            steps {
                bat 'python -m pytest -m smoke --html=report.html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html',
                         allowEmptyArchive: true
        }
    }
}