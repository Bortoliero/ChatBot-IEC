pipeline {
    agent any

    stages {
        stage('Preparação do Ambiente') {
            steps {
                bat 'python -m venv venv'
                bat '.\\venv\\Scripts\\pip install -r requisitos.txt'
            }
        }

        stage('Execução do Teste Levenshtein') {
            steps {
                bat '.\\venv\\Scripts\\python -m unittest levenshtein_teste.py'
            }
        }

        stage('Verificação do Arquivo de Perguntas') {
            steps {
                script {
                    if (fileExists('perguntas.txt')) {
                        echo 'Arquivo perguntas.txt encontrado!'
                    } else {
                        error('Arquivo perguntas.txt não encontrado. Interrompendo o pipeline.')
                    }
                }
            }
        }

        stage('Execução do Chatbot') {
            steps {
                bat '.\\venv\\Scripts\\python chat_bot.py'
            }
        }
    }

    environment{
        // PATH = "C:\\Windows\\System32;C:\\Programs\\Python;C:\\Programs\\Python\\Scripts;${env.PATH}"
        PATH = "C:\\Windows\\System32;C:\\Users\\joaoo\\AppData\\Local\\Programs\\Python\\Python310;C:\\Users\\joaoo\\AppData\\Local\\Programs\\Python\\Python310\\Scripts;${env.PATH}"
    }
}
