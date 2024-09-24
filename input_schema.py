INPUT_SCHEMA = {
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["A cat holding a sign that says hello world"]
    },
     "workflow": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["https://github.com/inferless/ComfyUI-Inferless-template/raw/main/workflows/sd1-5_workflow.json"]
    },
    "negative_prompt": {
        'datatype': 'STRING',
        'required': False,
        'shape': [1],
        'example': ["blurry, illustration, toy, clay, low quality, flag, nasa, mission patch"]
    }
}
