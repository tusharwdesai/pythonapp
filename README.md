# Microservice Python Application on GCP Kubernetes

## Overview
This repository contains a **microservice-based Python application** consisting of four main components:

- **Frontend** – User-facing web interface  
- **Backend** – Python-based API service  
- **MongoDB** – NoSQL database  
- **Mongo Express** – Web-based MongoDB admin interface  

All components are **containerized using Docker** and **orchestrated using Kubernetes** in a **Google Cloud Platform (GCP)** environment.

---

## Architecture
The application follows a microservices architecture where each service runs in its own Docker container and communicates within a Kubernetes cluster.

---

## Technologies Used
- **Python Flask** (Backend service)
- **Frontend Framework** (Python Flask)
- **MongoDB**
- **Mongo Express**
- **Docker**
- **Kubernetes (GKE)**
- **Google Cloud Platform (GCP)**

---

## Containerization
Each component is packaged as a separate Docker image:

- Frontend container
- Backend container
- MongoDB container
- Mongo Express container

This enables portability, scalability, and independent deployment of services.

---

## Kubernetes Orchestration
The application is deployed on **Google Kubernetes Engine (GKE)** with:

- Kubernetes **Deployments** for each service
- **Services** for internal and external communication
- Environment variables and secrets for configuration
- Scalable and fault-tolerant infrastructure

---

## Features
- Fully containerized microservice architecture
- Scalable deployment on Kubernetes
- Separation of concerns between frontend, backend, and database
- Web-based MongoDB management via Mongo Express

---

## Getting Started
> Prerequisites:
- Docker
- Kubernetes (kubectl)
- GCP account with GKE enabled

Steps to deploy:
1. Build Docker images for all services
2. Push images to a container registry
3. Apply Kubernetes manifests to the GKE cluster
4. Access the frontend via the exposed service

---

## Future Improvements
- CI/CD pipeline integration
- Authentication and authorization
- Logging and monitoring (Prometheus, Grafana)
- Helm charts for deployment
- Secure secrets management

---

## License
This project is licensed under the MIT License.
