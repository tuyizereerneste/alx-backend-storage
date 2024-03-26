#!/usr/bin/env python3
"""
Module for task 10
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    function that update document with a specific
    """
    return mongo_collection.update_many({
            "name": name
        },
        {
            "$set": {
                "topics": topics
            }
        })
