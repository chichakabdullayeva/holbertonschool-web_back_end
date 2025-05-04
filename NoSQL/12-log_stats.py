#!/usr/bin/env python3
"""
Module to provide statistics about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Total log count
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Method counts
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status check count
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

