import requests
import os
import yaml
import json

# Carregar o arquivo de configuração bundle.yaml
with open('bundle.yaml', 'r') as file:
    bundle_config = yaml.safe_load(file)

notebook_paths = [f"/Workspace/Repos/Development/databricks-dlt/{notebook['path']}" for notebook in bundle_config['assets']['notebooks']]

# Parâmetros do Job
job_name = "Run DLT SQL Scripts"

# Configuração do Cluster
cluster_spec = {
    "num_workers": 2,
    "spark_version": "7.3.x-scala2.12",
    "node_type_id": "i3.xlarge",
    "autotermination_minutes": 60
}

# Função para criar uma tarefa de notebook
def create_notebook_task(notebook_path):
    return {
        "name": f"Task for {os.path.basename(notebook_path)}",
        "new_cluster": cluster_spec,
        "notebook_task": {
            "notebook_path": notebook_path
        }
    }

# Configuração do Job
job_config = {
    "name": job_name,
    "tasks": [create_notebook_task(path) for path in notebook_paths]
}

# URL da API do Databricks
url = f"https://{os.getenv('DATABRICKS_HOST')}/api/2.0/jobs/create"

# Headers da Requisição
headers = {
    "Authorization": f"Bearer {os.getenv('DATABRICKS_TOKEN')}",
    "Content-Type": "application/json"
}

# Criação do Job
response = requests.post(url, headers=headers, data=json.dumps(job_config))
print(response.json())
