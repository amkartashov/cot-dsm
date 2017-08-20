import docker

def get_nodes():
    client = docker.from_env()
    return [get_node_info(node) for node in client.nodes.list()]

def get_containers(node_id):
    client = docker.from_env()
    node = client.nodes.get(node_id)
    nodedc = docker.DockerClient(base_url='tcp://' + node.attrs['Status']['Addr'] +':2375')
    return [get_ct_info(ct) for ct in nodedc.containers.list()]

def get_node_info(node):
    info = { 
        "ID": node.attrs['ID'],
        "short_id": node.short_id,
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

def get_ct_info(ct):
    info = {
        "short_id": ct.short_id,
        "service_name": ct.attrs['Config']['Labels']['com.docker.swarm.service.name'],
        "service_id": ct.attrs['Config']['Labels']['com.docker.swarm.service.id'],
        "task_name": ct.attrs['Config']['Labels']['com.docker.swarm.task.name'],
        "mem_limit": ct.attrs['HostConfig']['Memory'],
        "ioweight": ct.attrs['HostConfig']['BlkioWeight'],
        "cpushares": ct.attrs['HostConfig']['CpuShares'],
        "status": ct.attrs['State']['Status'],
    }
    return info()
