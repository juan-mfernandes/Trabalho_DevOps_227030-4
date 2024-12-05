# **Aplicação de Monitoramento e Dashboard**

## **Descrição**
Este projeto é uma aplicação web que utiliza **Flask**, **MariaDB**, **Prometheus** e **Grafana** para monitoramento e análise de dados. O objetivo é fornecer uma visualização clara de métricas da aplicação, como número de acessos, consultas ao banco de dados e uso de memória.

---

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

