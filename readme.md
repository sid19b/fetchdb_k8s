# 🚀 Audit Management Full-Stack Application (Kubernetes-based)

This project is a full-stack **Audit Management** web application deployed on **Kubernetes**, built with:

- **Frontend:** React + Nginx  
- **Backend:** FastAPI (Python)  
- **Database:** PostgreSQL  
- **Kubernetes Services:** ClusterIP, Ingress, ConfigMap, Secret  
- **Environment:** Kind (local Kubernetes cluster)

The app demonstrates how a microservice-based web application can be deployed, scaled, and managed using Kubernetes — exactly like it would be in a real production environment (e.g., AWS EKS).

---

## 🧩 Architecture Overview

```plaintext
                   ┌──────────────────────────────────┐
                   │        Ingress Controller         │
                   │ (Nginx Ingress, Routes traffic)   │
                   └──────────────┬───────────────────┘
                                  │
                    ┌─────────────┴───────────────┐
                    │                             │
        ┌───────────▼──────────┐       ┌──────────▼──────────┐
        │  Frontend Service    │       │   Backend Service   │
        │ (React + Nginx, 80)  │       │ (FastAPI, 8000)     │
        └───────────┬──────────┘       └──────────┬──────────┘
                    │                             │
                    │                             ▼
                    │                 ┌──────────────────────┐
                    │                 │   PostgreSQL DB       │
                    │                 │ (Persistent Volume)   │
                    │                 └──────────────────────┘
                    │
        ┌───────────▼────────────┐
        │        User            │
        │  http(s)://myapp.local │
        └────────────────────────┘
