agg = [
    {
        '$group': {
            '_id': 0, 
            'total': {
                '$sum': '$id'
            }
        }
    }
]