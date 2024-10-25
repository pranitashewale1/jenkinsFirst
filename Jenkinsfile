pipeline {
   agent {
       docker {
           image 'python:3.7'
        }
  }
  stages {
    stage('version') {
    agent {
        docker {
            image 'python:3.7'
        }
    }
      steps {
        sh 'python --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python hello.py'
      }
    }
  }
}
