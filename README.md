# **Aplicação Flask de Gerenciamento de Alunos**

## **Descrição**
Este projeto é uma aplicação web que utiliza **Flask**, **MariaDB**, **Prometheus** e **Grafana** para monitoramento e análise de dados. O objetivo é fornecer uma visualização clara de métricas da aplicação, como número de acessos, consultas ao banco de dados e uso de memória.

---
## **Rodando o projeto de forma manual**
## **Requisitos**
Certifique-se de que os seguintes componentes estão instalados no seu ambiente:

- **Docker** e **Docker Compose**
- **Git**

---
## **Configuração do Ambiente**

### **1. Clonar o Repositório**
```bash
git clone git@github.com:juan-mfernandes/Trabalho_DevOps_227030-4.git
cd Trabalho_DevOps_227030-4
```
### **2. Subir o Ambiente com Docker**
```bash
docker-compose up --build
```
### **3. Acessar os componentes**

- Flask API: ```http://localhost:5000```
- Grafana: ```http://localhost:3000```

### **4. Configuração do Dashboard no Grafana**
- Acesse o Grafana em ```http://localhost:3000```
- Faça login (usuário: admin, senha: admin).
- Importe o arquivo JSON de dashboard localizado em grafana/dashboards/mariadb_dashboard.json.
- Certifique-se de que as métricas estão sendo exibidas corretamente:

### **Imagem do Dashboard**

![Dashboard Grafana](/imagem_grafana1.png)

## **Rodando o projeto com Jenkins**
### Requisitos:
- Jenkins instalado e iniciado

### **1. Acesse o ambiente do Jenkins**
- No seu navegador, acesse ```http://localhost:8080``` (a porta 8080 é a porta padrão do Jenkins)
- Realize o Login e siga os passos abaixo para criar e rodar a pipeline através do Jenkinsfile presente no projeto

### **1. Navegue até "New Item" na tela inicial e selecione "Pipeline"**
![Criando a Pipeline](/jenkins1.png)

### **2. Navegue até o rodapé da página de configuração e em "Definition" selecione "Pipeline script form SCM"**
![Definindo SCM](/jenkins2.png)

### **3. Como SCM principal, selecione o "Git" e inclua o caminho deste repositório com a branch "main". Em seguida, salve as alterações**
![Definindo SCM 2](/jenkins3.png)

### **4. Faça a buid do Pipeline**
![Iniciando build do Pipeline](/jenkins4.png)

### **5. Acesse o Grafana**
- No seu navegador, acesse ```http://localhost:3000```
