
# Introduction to SR-MPLS Lab
This lab is meant for use with the ASP Containerlab enviornment in Cisco's dcloud.  Please refer to the following (https://github.com/mfierbaugh/asp-containerlab)

## Features 
Features in this playbook:
 - Segment Routing using ISIS or OSPF
 - Transport Independant Loop Free Alternate (TI-LFA)
 - Segment Routing Performance Measurement (SR-PM)
 - Flexable Algorithm
 - Core [QOS](Qos.md)

Configurations are working examples of Cisco Converged SDN Transport (https://xrdocs.io/design/blogs/latest-converged-sdn-transport-ig)

## Usage
This project is a full CI/CD pipline for configuration management. All configuration changes should be made by logging an issue then merging the changes to the Development branch then Test branch.

WARNING - this is a full commit replace and will restore the Converged SDN Transport configuration.

```
./config_lab
```

# Start T-REX 
Once the lab configuration has been committed (config_lab), open a terminal and ssh to each of the trex nodes (trex-1 and trex-2)

## Start the interactive trex console which will make a local connection to the running interactive daemon
```
./trex-console
```

## Start generating some traffic
```
start -f stl/imix.py
```

## To interact with and view statistics for the current stream launch the text-based user interface (tui)
```
tui
```

## Attempt to increase per interface traffic rate to 200mbps (400mbps rx/tx total). Throughput achievable in the Docker environment is dependent primarily on single core\thread CPU performance.
```
update -m 200mbps
```

# Run playbooks directly

To run the playbook without committing changes:

    ansible-playbook -i hosts.yml lab_master_playbook.yml -e "commit_changes=0"

To run the playbook committing the changes:

    ansible-playbook -i hosts.yml lab_master_playbook.yml -e "commit_changes=1"