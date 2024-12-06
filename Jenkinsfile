pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'C:\\Users\\shewa\\AppData\\Local\\Programs\\Python\\Python312\\python.exe --version'
      }
    }
    stage('hello') {
      steps {
        bat 'C:\\Users\\shewa\\AppData\\Local\\Programs\\Python\\Python312\\python.exe hello.py'
      }
    }
  }
}
