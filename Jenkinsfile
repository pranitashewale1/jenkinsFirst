pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        python -c "import hello; myscript.my_function()"
      }
    }
  }
}
