#!/usr/bin/env python3
"""
Module for task 11
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    function that find by specific value
    """
    return mongo_collection.find({"topics":  {"$in": [topic]}})
