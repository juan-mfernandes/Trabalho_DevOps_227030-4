pipeline {
	agent any
	environment {
		IMAGE_NAME = "trabalhodevops-main-flask"
	}
	stages {
		stage("Baixar código do git...") {
			steps {
				checkout scm // #1 - Clona o repositório configurado na pipeline
			}
		}
		stage("Configura o ambiente..."){ 
			steps{
				sh 'python3 -m venv venv'//#2 - Cria o ambiente virtual para rodar arquivos .py
				sh './venv/bin/pip install -r flask/requirements.txt' //#2 - Instala dependências necessárias presentes no arquivo requirements.txt
			}
		}
		stage("Build da aplicação..."){
			steps{
				sh 'docker-compose build' //#4 - Cria a imagens Docker para todos os serviços presentes no arquivo docker-compose.yml
			}
		}
		stage("Deploy da aplicação..."){
			steps{
				sh 'docker-compose up -d' //#5 - Uso da opção -d ou --detach para subir containers em segundo plano  
			}
		}
		stage("Rodar Testes..."){
			steps{
				sh 'docker exec -it trabalho-devops-flask-1 python test_app.py' //#3 - Busca e executa os teste presentes em arquivos test_ e grava logs do teste em um arquivo xml
			}
		}
		stage("Validação de monitoramento"){
			steps{
				script{
					// #6 - Verifica se os serviços estão disponíveis
					def prometheusStatus = sh(script: "curl -s http://localhost:9090", returnStatus: true)
					def grafanaStatus = sh(script: "curl -s http://localhost:3000", returnStatus: true)

					if(prometheusStatus != 0 || grafanaStatus != 0) {
						error("Monitoramento falhou, Prometheus ou Grafana não estão acessíveis.")
					}
				} 
			}
		}
	}
	post { 
		always {
			junit 'report.xml' // #7 - Publica o resultado dos testes no Jenkins
			cleanWs() // Limpa o worskpace após a execução
		}	
	}

}
