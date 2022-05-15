pipeline {
  agent any
  options {
    buildDiscarder(logRotator(numToKeepStr: '10')) // Retain history on the last 10 builds
    timestamps() // Append timestamps to each line
    timeout(time: 20, unit: 'MINUTES') // Set a timeout on the total execution time of the job
  }
  stages {  // Define the individual processes, or stages, of your CI pipeline
    stage('Checkout') { // Checkout (git clone ...) the projects repository
      steps {
        checkout scm
      }
    }
    stage('Setup') { // Install any dependencies you need to perform testing
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh """
          pip install -r requirements.txt
          """
        }
      }
    }
    stage('Unit Testing') { // Perform unit testing
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh """
          python3 -m pytest
          """
        }
      }
    }
  }
}