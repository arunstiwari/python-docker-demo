node('docker') {

    stage('Cleanup') {
        step([$class: 'WsCleanup'])
    }
    stage('Checkout SCM') {
        checkout scm
    }
    def pythonImage
    stage('build docker image') {
        pythonImage = docker.build("maxsum:build")
    }
    stage('test') {
        pythonImage.inside {
            sh '. /tmp/venv/bin/activate && python -m pytest --junitxml=build/results.xml'
        }
    }
    stage('collect test results') {
        junit 'build/results.xml'
    }
    stage('Sonar Analysis') { 
        def scannerHome = tool 'ADOP SonarScanner'
         withSonarQubeEnv('ADOP Sonar') {
                    sh "${scannerHome}/bin/sonar-scanner"
            }
        
    }
   

}
