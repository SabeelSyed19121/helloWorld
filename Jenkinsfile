pipeline {
    agent any

    environment {
        // Jenkins credential storing your SonarQube token
        SONAR_TOKEN = credentials('squ_cf5f4992743c915dba55a7f9866422939e80ebe5')
        SONAR_HOST_URL = 'http://localhost:9000'
        PROJECT_KEY = 'hello-world-web'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out source code..."
                git branch: 'main', url: 'https://github.com/your-username/helloWorld.git'
            }
        }

        stage('Start SonarQube (Docker)') {
            steps {
                echo "Starting SonarQube in Docker..."
                sh '''
                    docker rm -f sonarqube || true
                    docker run -d --name sonarqube \
                        -p 9000:9000 \
                        -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true \
                        sonarqube:lts
                    echo "Waiting 30s for SonarQube to start..."
                    sleep 30
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo "Running SonarQube scanner..."
                sh '''
                    # Install sonar-scanner if not installed
                    if ! command -v sonar-scanner &> /dev/null
                    then
                        wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
                        unzip sonar-scanner-cli-5.0.1.3006-linux.zip
                        export PATH=$PATH:$(pwd)/sonar-scanner-5.0.1.3006-linux/bin
                    fi

                    sonar-scanner \
                        -Dsonar.projectKey=${PROJECT_KEY} \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=${SONAR_HOST_URL} \
                        -Dsonar.login=${SONAR_TOKEN}
                '''
            }
        }

        stage('Quality Gate') {
            steps {
                echo "Waiting for SonarQube Quality Gate..."
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }

    post {
        always {
            echo "Stopping SonarQube Docker container..."
            sh 'docker rm -f sonarqube || true'
        }
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}

