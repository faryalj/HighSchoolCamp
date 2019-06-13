"""
title: data_structures_practice
author: Faryal
date: 2019-06-13 11:33
"""

import random
def shake_ball():
    responses = ["Yes definitely", "As I see it, yes", "Ask again later", "Cannot predict now", "Don't count on it",
                 "Very doubtful"]
    input("Ask a question about your future?")
    return random.choice(responses)

