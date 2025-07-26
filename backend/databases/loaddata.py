# backend/database/loaddata.py

import pandas as pd
from config import db

def load_csv_to_mongo(filepath, collection_name):
    df = pd.read_csv(filepath)
    data = df.to_dict(orient='records')

    collection = db[collection_name]
    collection.drop()  # Optional: clear old data
    result = collection.insert_many(data)
    print(f"Inserted {len(result.inserted_ids)} records into '{collection_name}' collection.")

if __name__ == "__main__":
    load_csv_to_mongo("../data/ecommerce_data.csv", "products")
