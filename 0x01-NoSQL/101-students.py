#!/usr/bin/env python3
"""
Module for task 101
"""


def top_students(mongo_collection):
    """ function that finds average score and
    sorts the students by score
    """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
