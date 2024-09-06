INPUT_SCHEMA = {
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["A cat holding a sign that says hello world"]
    },
     "workflow_name": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["sd1-5_workflow"]
    },
    "negative_prompt": {
        'datatype': 'STRING',
        'required': False,
        'shape': [1],
        'example': ["blurry, illustration, toy, clay, low quality, flag, nasa, mission patch"]
    }
}