# 🚀 AI-Driven Containerized Data Analytics Platform with Kubernetes Resource Monitoring  
### Case Study: Colorado Motor Vehicle Sales Data Analysis

---

## 📌 Project Overview

This project implements an AI-driven containerized data analytics platform deployed on Kubernetes with real-time resource monitoring and prediction. The system analyzes Colorado motor vehicle sales data, performs exploratory data analysis (EDA), and forecasts future sales using the ARIMA model. The application is containerized using Docker and deployed using Kubernetes (Minikube) on a local Linux environment.

Additionally, the system integrates Kubernetes Metrics Server to collect real-time CPU and memory usage of running pods. An AI-based monitoring module predicts future CPU usage trends based on real-time metrics, demonstrating intelligent resource monitoring capability.

This project demonstrates real-world DevOps, Cloud Computing, Containerization, Kubernetes orchestration, and AI-based resource monitoring concepts without requiring any paid cloud platform.

---

## 🧠 Key Features

- Interactive Data Analytics Dashboard using Streamlit  
- Exploratory Data Analysis with visualizations  
- ARIMA-based time series forecasting  
- Docker containerized application  
- Kubernetes deployment with multiple replicas  
- Real-time CPU and memory monitoring using Kubernetes metrics-server  
- AI-based CPU usage prediction simulation  
- Scalable cloud-native architecture  
- Fully deployable on local Linux environment without cloud cost  

---

## 🏗️ System Architecture

User Browser → Streamlit Dashboard → Docker Container → Kubernetes Deployment (Minikube) → Multiple Pods → Metrics Server → AI Monitoring Module

---

## 🛠️ Technologies Used

Programming Language: Python 3.8  
Data Analytics: Pandas, NumPy, Seaborn, Matplotlib  
Forecasting: Statsmodels (ARIMA)  
Web Framework: Streamlit  
Containerization: Docker  
Container Orchestration: Kubernetes (Minikube)  
Monitoring: Kubernetes Metrics Server  
Operating System: Linux (Ubuntu / WSL Ubuntu)

---

## 📂 Project Structure

Final_Project/

app.py  
Dockerfile  
deployment.yaml  
service.yaml  
requirements.txt  
colorado_motor_vehicle_sales.csv  
main.ipynb  
README.md  

---

## ⚙️ Prerequisites Installation (Linux / Ubuntu / WSL)

### Install Docker

sudo apt update  
sudo apt install docker.io -y  
sudo systemctl start docker  
sudo systemctl enable docker  

Verify Docker installation:

docker --version  

---

### Install kubectl

curl -LO https://dl.k8s.io/release/v1.29.0/bin/linux/amd64/kubectl  
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl  

Verify:

kubectl version --client  

---

### Install Minikube

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64  
sudo install minikube-linux-amd64 /usr/local/bin/minikube  

Verify:

minikube version  

---

## 🚀 Complete Deployment Steps (Start to End)

### Step 1: Navigate to Project Folder

cd /path/to/Final_Project  

Example:

cd /mnt/p/MTech/Final_Project  

---

### Step 2: Start Kubernetes Cluster

minikube start --driver=docker  

Enable Metrics Server:

minikube addons enable metrics-server  

---

### Step 3: Configure Docker Environment

eval $(minikube docker-env)  

---

### Step 4: Build Docker Image

docker build -t colorado_motor_vechile .  

Verify image:

docker images  

---

### Step 5: Deploy Application to Kubernetes

kubectl apply -f deployment.yaml  
kubectl apply -f service.yaml  

Verify pods:

kubectl get pods  

Verify services:

kubectl get services  

---

### Step 6: Grant Kubernetes Permissions (Required for AI Monitoring)

kubectl create clusterrolebinding default-admin-binding --clusterrole=cluster-admin --serviceaccount=default:default --dry-run=client -o yaml | kubectl apply -f -  

Restart deployment:

kubectl rollout restart deployment colorado-sales-deployment  

---

### Step 7: Copy Kubernetes Config to Pods (Required for AI Monitoring)

for pod in $(kubectl get pods -o name | cut -d/ -f2); do kubectl exec -it $pod -- mkdir -p /root/.kube; kubectl cp ~/.kube/config $pod:/root/.kube/config; done  

---

### Step 8: Launch Application

minikube service colorado-sales-service  

Application will open automatically in browser:

http://127.0.0.1:XXXXX  

---

## 📊 Application Modules

Overview Module  
Displays total sales, average sales, dataset preview, and trend visualization.

EDA Module  
Shows statistical analysis, sales distribution, and correlation heatmap.

County Analysis Module  
Displays county-wise sales comparison and trend analysis.

Forecasting Module  
Uses ARIMA model to predict future motor vehicle sales.

AI Monitoring Module  
Shows real-time CPU and memory usage of Kubernetes pods and predicts CPU usage trends.

---

## 📡 Kubernetes Monitoring Commands

View running pods:

kubectl get pods  

View CPU and memory usage:

kubectl top pods  

View services:

kubectl get services  

---

## 🛑 Stop System After Use

minikube stop  

---

## ▶️ Restart System Later (Presentation or Reuse)

cd /mnt/p/MTech/Final_Project  

minikube start --driver=docker  

eval $(minikube docker-env)  

docker build -t colorado_motor_vechile .  

kubectl apply -f deployment.yaml  

kubectl apply -f service.yaml  

kubectl rollout restart deployment colorado-sales-deployment  

for pod in $(kubectl get pods -o name | cut -d/ -f2); do kubectl exec -it $pod -- mkdir -p /root/.kube; kubectl cp ~/.kube/config $pod:/root/.kube/config; done  

minikube service colorado-sales-service  

---

## 🤖 AI Monitoring Explanation

The system collects real-time CPU and memory usage using Kubernetes metrics-server.

Command used internally:

kubectl top pods  

AI prediction logic simulates future CPU usage using simple prediction:

Predicted CPU = Current CPU × 1.15  

This demonstrates intelligent resource monitoring capability.

---

## 🎓 Academic Value

This project demonstrates:

Docker containerization  
Kubernetes deployment and orchestration  
Cloud-native architecture  
Real-time resource monitoring  
AI-based resource prediction  
DevOps workflow implementation  

Suitable for:

M.Tech Final Year Project  
DevOps Portfolio  
Cloud Computing Portfolio  

---

## 💼 Resume Project Description

AI-Driven Containerized Data Analytics Platform with Kubernetes Resource Monitoring  

Developed a containerized data analytics platform using Docker and Kubernetes. Implemented real-time resource monitoring using Kubernetes metrics-server and integrated AI-based CPU usage prediction simulation. Built interactive dashboard using Streamlit and deployed scalable microservice architecture locally using Minikube.

---

## 👨‍💻 Author

Pranuth Manjunath  
M.Tech Student  
Cloud Computing and DevOps Enthusiast  

---

## 📜 License

This project is developed for academic and educational purposes.

---

## ⭐ Acknowledgements

Kubernetes Documentation  
Docker Documentation  
Streamlit Documentation  
Statsmodels Library  
Minikube Documentation  

