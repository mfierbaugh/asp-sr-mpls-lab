commands = [
    "show lldp neighbors detail",
    "show ip interface brief",
    "show version",
    "show inventory",
    "show route ipv4",
    "show route ipv6",
    "show mpls forwarding",
    "show bgp neighbors",
    "show isis neighbors",
    "show isis database detail",
]

core_commands = [
    "show lldp neighbors detail",
    "show ip interface brief",
    "show version",
    "show inventory",
    "show route ipv4",
    "show route ipv6",
    "show mpls forwarding",
    "show isis neighbors",
    "show isis database detail",
]

device_commands = {}

device_commands["RBB.ASR9903.20"] = commands
device_commands["RBB.ASR9903.21"] = commands
device_commands["RBB.NCS5504.22"] = commands
device_commands["RBB.NCS5504.23"] = commands
device_commands["RBB.NCS5504.24"] = commands
device_commands["RBB.8201.100"] = core_commands
device_commands["RBB.8201.101"] = core_commands
device_commands["RBB.8201.102"] = core_commands
device_commands["RBB.8201.103"] = core_commands
device_commands["RBB.NCS540.10"] = commands
device_commands["RBB.NCS540.11"] = commands
device_commands["RBB.NCS540.12"] = commands
device_commands["RBB.NCS540.13"] = commands
device_commands["RBB.NCS55A1.14"] = commands
device_commands["RBB.NCS55A1.15"] = commands
device_commands["RBB.NCS55A1.16"] = commands
device_commands["RBB.NCS55A2.25"] = commands
device_commands["RBB.NCS55A2.26"] = commands
device_commands["RBB.vRR-SR-PCE.50"] = commands
device_commands["RBB.vRR-SR-PCE.51"] = commands
device_commands["RBB.vRR-SR-PCE.52"] = commands
device_commands["RBB.vRR-SR-PCE.53"] = commands
device_commands["RBB.vBNG.55"] = commands
device_commands["RBB.cnBNG-UP.60"] = commands
device_commands["RBB.cnBNG-UP.61"] = commands


devices = [
    "RBB.ASR9903.20",
    "RBB.ASR9903.21",
    "RBB.NCS5504.22",
    "RBB.NCS5504.23",
    "RBB.NCS5504.24",
    "RBB.8201.100",
    "RBB.8201.101",
    "RBB.8201.102",
    "RBB.8201.103",
    "RBB.NCS540.10",
    "RBB.NCS540.11",
    "RBB.NCS540.12",
    "RBB.NCS540.13",
    "RBB.NCS55A1.14",
    "RBB.NCS55A1.15",
    "RBB.NCS55A1.16",
    "RBB.NCS55A2.25",
    "RBB.NCS55A2.26",
    "RBB.vRR-SR-PCE.50",
    "RBB.vRR-SR-PCE.51",
    "RBB.vRR-SR-PCE.52",
    "RBB.vRR-SR-PCE.53",
    "RBB.vBNG.55",
    "RBB.cnBNG-UP.60",
    "RBB.cnBNG-UP.61",
]

destinations = [
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
    ["1.1.1.51", "1.1.1.52"],
]
testbed_filename = "testbed.yaml"
