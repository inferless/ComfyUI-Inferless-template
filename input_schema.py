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
        'example': ["https://raw.githubusercontent.com/inferless/ComfyUI/main/workflows/txt_2_img.json"]
    },
    "negative_prompt": {
        'datatype': 'STRING',
        'required': False,
        'shape': [1],
        'example': ["blurry, illustration, toy, clay, low quality, flag, nasa, mission patch"]
    }
}
