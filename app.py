import subprocess
import os
import uuid
from comfy_utils import run_comfyui_in_background, check_comfyui, load_workflow, prompt_update_workflow, send_comfyui_request, get_img_file_path, image_to_base64, stop_server_on_port, is_comfyui_running

class InferlessPythonModel:
    def initialize(self):
        self.directory_path = os.getenv('NFS_VOLUME')
        if not os.path.exists(self.directory_path+"/ComfyUI"):
            subprocess.run(["wget", "https://github.com/inferless/ComfyUI-Inferless-template/raw/main/build.sh"])
            subprocess.run(["bash", "build.sh"], check=True)
          
        self._data_dir = self.directory_path+"/workflows"
        self.server_address = "127.0.0.1:8188"
        self.client_id = str(uuid.uuid4())
        
        if is_comfyui_running(self.server_address):
            stop_server_on_port(8188)    
        run_comfyui_in_background()
        self.ws = check_comfyui(self.server_address,self.client_id)

    def infer(self, inputs):
        workflow_name = inputs.get("workflow_name")
        prompt = inputs.get("prompt")
        negative_prompt = inputs.get("negative_prompt")
        
        workflow = load_workflow(self.directory_path,workflow_name)
        prompt = prompt_update_workflow(workflow_name,workflow,prompt)
        prompt_id = send_comfyui_request(self.ws, prompt, self.server_address,self.client_id)
        file_path = get_img_file_path(self.server_address,prompt_id)
        image_base64 = image_to_base64(file_path)
        
        return {"generated_image_base64":image_base64}
    
    def finalize(self):
        pass
