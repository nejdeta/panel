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
          sh 'python3 -m pip install --upgrade pip'
          sh 'pip3 install -r requirements.txt'
        }
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 tests/test_check_panel.py'
      }
    }
  }
}