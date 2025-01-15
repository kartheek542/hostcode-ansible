#! /usr/bin/python3

import json

inventory = open("./hostcode-inventory.ini", 'w')
terraform_outputs = json.loads(open("./terraform-output.json").read())

inventory.write("[kubernetes_master]\n")
inventory.write(f"kube_master ansible_host={terraform_outputs['kube_master_public_ip']['value']} ansible_connection=ssh ansible_user=ubuntu\n")
inventory.write("\n")

inventory.write("[kubernetes_slave]\n")
inventory.write(f"kube_slave_1 ansible_host={terraform_outputs['kube_slave_public_ip']['value'][0]} ansible_connection=ssh ansible_user=ubuntu\n")
inventory.write(f"kube_slave_2 ansible_host={terraform_outputs['kube_slave_public_ip']['value'][1]} ansible_connection=ssh ansible_user=ubuntu\n")
inventory.write("\n")

inventory.write("[reactjs_servers]\n")
inventory.write(f"react_server_1 ansible_host={terraform_outputs['reactjs_public_ip']['value']} ansible_connection=ssh ansible_user=ubuntu\n")
inventory.write("\n")

inventory.write("[nodejs_servers]\n")
inventory.write(f"node_server_1 ansible_host={terraform_outputs['nodejs_public_ip']['value']} ansible_connection=ssh ansible_user=ubuntu\n")
inventory.write("\n")

inventory.close()
