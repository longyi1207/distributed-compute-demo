# Distributed Computing Demo: Ray vs Celery vs Kafka

This repository contains **three different implementations** of distributed computing using:
- [Ray](https://ray.io/)
- [Celery](https://docs.celeryq.dev/)
- [Kafka](https://kafka.apache.org/)

Each implementation is contained in its respective directory:
- `ray/`
- `celery/`
- `kafka/`

The goal of this project is to implement a demo using each of these frameworks to demonstrate their capabilities and suitability for different use cases.

---

## 🚀 **High-Level Comparison: Ray vs Celery vs Kafka**
Each of these frameworks is designed for **different types of distributed workloads**. Here’s how they compare:

| Framework  | Best Suited For | Task Model | Scalability | Ease of Use | Architecture |
|------------|---------------|------------|-------------|-------------|-------------|
| **Ray**    | Parallel processing, ML workloads, Python-native distributed tasks | Actor-based and task-based | High (auto-scaling workers) | Easy | Head-worker architecture |
| **Celery** | Task queues, background jobs, distributed workers | Task queue-based | Moderate (requires message broker like Redis/RabbitMQ) | Easy | Worker-broker architecture |
| **Kafka**  | Event-driven architectures, real-time data streaming | Publish-subscribe | High (designed for massive-scale streaming) | Moderate | Producer-consumer architecture |

---

## 📌 **Prerequisites**
Before running any of the implementations, ensure you have:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

### 🔹 **How to Run each of the Examples**
```bash
cd <service-directory>
docker-compose up --build
```