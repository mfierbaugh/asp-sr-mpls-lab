# Features 

Features in this playbook:
 - Segment Routing using ISIS or OSPF
 - Transport Independant Loop Free Alternate (TI-LFA)
 - Flexable Algorithm
 - Core [QOS](Qos.md)

# Usage

This project is a full CI/CD pipline for configuration management. All configuration changes should be made by logging an issue then merging the changes to the Development branch then Test branch.

WARNING - this is a full commit replace and will restore the Converged SDN Transport configuration.

# Setup

Start by updating the host field to mach your enviroment.
.
..
...

# Run playbooks directly



To run the playbook without committing changes:

    ansible-playbook -i hosts.yml lab_master_playbook.yml -e "commit_changes=0"

To run the playbook committing the changes:

    ansible-playbook -i hosts.yml clab_master_playbook.yml -e "commit_changes=1"
