#!/usr/bin/python3
'''DEfines the Review class that inherits from BaseModel.'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Represents a  user's review.'''
    place_id = ''
    user_id = ''
    text = ''
