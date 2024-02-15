pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
     stage('build') {
      steps {
        script{
          sh 'python -m pip install --upgrade pip'
          sh 'pip install -r requirements.txt'
        }
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 script.py'
      }
    }
  }
}
