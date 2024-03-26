#!/usr/bin/env python3
"""
Module for task 8
"""

import pymongo


def list_all(mongo_collection):
    """ function that lists all
    documents in a collection
    """
    if not mongo_collection:
        return []
    doc = mongo_collection.find()
    return [post for post in doc]
