from dsm import app
from dsm.dckr import get_nodes, get_containers

from flask import render_template

@app.route('/')
def show_nodes():
    return render_template('show_nodes.html', nodes=get_nodes())

@app.route('/node/<id>')
def show_node(id):
    return render_template('show_containers.html',
            containers=get_containers(node_id=id))


