

'''
from mermaid import Mermaid
import os

def load_diagram_config():
    diagram = os.getenv('MODULE_DIAGRAM', '')
    if not diagram:
        with open('config/diagrams.yaml') as f:
            # Load from YAML
            diagram = yaml.safe_load(f)
    return diagram

def render_module_diagram():
    diagram = load_diagram_config()
    return Mermaid(diagram).render()
'''