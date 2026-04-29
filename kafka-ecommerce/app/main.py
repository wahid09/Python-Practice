# app/main.py
from fastapi import FastAPI, HTTPException, BackgroundTasks
from app.models import Order
from app.producer import produce_order
from app.consumer import start_background_consumer
from app.admin import create_topic_if_not_exists  # ← New import

app = FastAPI(title="E-commerce Kafka API")


@app.on_event("startup")
async def startup_event():
    print("🚀 Starting E-commerce Kafka API...")

    # Create topic if it doesn't exist
    create_topic_if_not_exists()

    # Start Kafka consumer in background
    start_background_consumer()


@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down application...")


@app.post("/orders/", status_code=201)
async def create_order(order: Order, background_tasks: BackgroundTasks):
    try:
        background_tasks.add_task(produce_order, order)
        return {
            "message": "Order received and sent to Kafka",
            "order_id": str(order.order_id)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {"message": "E-commerce Kafka + FastAPI is running 🚀"}