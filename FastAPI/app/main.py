from fastapi import FastAPI,HTTPException

app=FastAPI()

@app.get("/")
def root():
    return{"message":"Welcome to FastAPI"}

@app.get("/product/{id}")
def get_product(id:int):
    product=["movie","laptop"]
    return product[id] if product[id] else  HTTPException(status_code=404, detail="No product found ")