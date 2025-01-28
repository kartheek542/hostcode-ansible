#! /usr/bin/python3

import json

inventory = open("./hostcode-inventory.ini", 'w')
terraform_outputs = json.loads(open("./terraform-output.json").read())

if "kube_master_public_ip" in terraform_outputs:
    inventory.write("[kubernetes_master]\n")
    inventory.write(f"kube_master ansible_host={terraform_outputs['kube_master_public_ip']['value']} ansible_connection=ssh ansible_user=ubuntu ansible_ssh_private_key_file=./aws_terraform_key\n")
    inventory.write("\n")

if "kube_slave_public_ip" in terraform_outputs:
    inventory.write("[kubernetes_slaves]\n")
    inventory.write(f"kube_slave_1 ansible_host={terraform_outputs['kube_slave_public_ip']['value'][0]} ansible_connection=ssh ansible_user=ubuntu ansible_ssh_private_key_file=./aws_terraform_key\n")
    # inventory.write(f"kube_slave_2 ansible_host={terraform_outputs['kube_slave_public_ip']['value'][1]} ansible_connection=ssh ansible_user=ubuntu ansible_ssh_private_key_file=./aws_terraform_key\n")
    inventory.write("\n")

if "reactjs_public_ip" in terraform_outputs:
    inventory.write("[reactjs_servers]\n")
    inventory.write(f"react_server_1 ansible_host={terraform_outputs['reactjs_public_ip']['value']} ansible_connection=ssh ansible_user=ubuntu ansible_ssh_private_key_file=./aws_terraform_key\n")
    inventory.write("\n")

if "nodejs_public_ip" in terraform_outputs:
    inventory.write("[nodejs_servers]\n")
    inventory.write(f"node_server_1 ansible_host={terraform_outputs['nodejs_public_ip']['value']} ansible_connection=ssh ansible_user=ubuntu ansible_ssh_private_key_file=./aws_terraform_key\n")
    inventory.write("\n")

inventory.close()
