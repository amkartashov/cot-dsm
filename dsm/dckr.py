import docker

def get_node_info(node):
    info = { 
        "ID": node.attrs['ID'],
        "Hostname": node.attrs['Description']['Hostname'],
        "MemoryBytes": node.attrs['Description']['Resources']['MemoryBytes'],
        "NanoCPUs": node.attrs['Description']['Resources']['NanoCPUs'],
        "Addr": node.attrs['Status']['Addr'],
        "State": node.attrs['Status']['State'],
        "EngineVersion": node.attrs['Description']['Engine']['EngineVersion'],
    }
    nodedc = docker.DockerClient(base_url='tcp://' + info['Addr'] +':2375')
    info['Containers'] = nodedc.info()['Containers']
    info['ContainersRunning'] = nodedc.info()['ContainersRunning']
    return info

def get_nodes():
    client = docker.from_env()
    return [get_node_info(node) for node in client.nodes.list()]

def get_containers():
    return None
