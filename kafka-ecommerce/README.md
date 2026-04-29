### Basic Instruction

**To start fastApi server run below command**
```shell
uvicorn app.main:app --reload --port 8000
```
**To test the api you can test both command line and postmane**

**For postmane content body and url is below**

```shell
POST http://127.0.0.1:8000/orders
{
  "user_id": "user_12345",
  "items": [
    {
      "product": "Wireless Headphones",
      "quantity": 1,
      "price": 89.99
    },
    {
      "product": "USB Cable",
      "quantity": 2,
      "price": 9.99
    }
  ],
  "total_amount": 109.97
}
```

**For command line test**

```shell 
curl -X POST http://127.0.0.1:8000/orders/ \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user_123",
    "items": [
      {"product": "Laptop Stand", "quantity": 1, "price": 49.99}
    ],
    "total_amount": 49.99
  }'

```