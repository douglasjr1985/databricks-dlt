import yaml
import shutil
import os

# Carregar o arquivo de configuração bundle.yaml
with open('bundle.yaml', 'r') as file:
    bundle_config = yaml.safe_load(file)

bundle_name = bundle_config['name']
bundle_version = bundle_config['version']
assets = bundle_config['assets']

# Criar a estrutura de diretórios do bundle
bundle_path = f"{bundle_name}_{bundle_version}"
os.makedirs(bundle_path, exist_ok=True)

# Função para copiar arquivos com verificação de existência
def copy_file_with_check(src, dst):
    if not os.path.exists(src):
        print(f"Erro: Arquivo {src} não encontrado.")
        return False
    shutil.copy(src, dst)
    return True

# Copiar os notebooks para o bundle
notebook_dir = os.path.join(bundle_path, 'notebooks')
os.makedirs(notebook_dir, exist_ok=True)
for notebook in assets['notebooks']:
    if not copy_file_with_check(notebook['path'], notebook_dir):
        raise FileNotFoundError(f"Arquivo {notebook['path']} não encontrado.")

# Copiar os arquivos de configuração para o bundle
config_dir = os.path.join(bundle_path, 'configurations')
os.makedirs(config_dir, exist_ok=True)
for config in assets['configurations']:
    if not copy_file_with_check(config['path'], config_dir):
        raise FileNotFoundError(f"Arquivo {config['path']} não encontrado.")

print(f"Bundle {bundle_name} version {bundle_version} created successfully.")
