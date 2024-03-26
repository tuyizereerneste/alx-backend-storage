#!/usr/bin/env python3
"""
Module for task 9
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    function that insert documents into a collection
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
