import platform
import psutil

def get_system_information():
    system_info = {}

    # System Information
    system_info['System'] = platform.system()
    system_info['Node Name'] = platform.node()
    system_info['Release'] = platform.release()
    system_info['Version'] = platform.version()
    system_info['Machine'] = platform.machine()
    system_info['Processor'] = platform.processor()

    # CPU Information
    cpu_info = {}
    cpu_info['Physical Cores'] = psutil.cpu_count(logical=False)
    cpu_info['Total Cores'] = psutil.cpu_count(logical=True)
    cpu_info['CPU Frequency'] = psutil.cpu_freq().current
    cpu_info['CPU Usage'] = psutil.cpu_percent()
    system_info['CPU Information'] = cpu_info

    # Memory Information
    mem_info = {}
    mem_info['Total Memory'] = psutil.virtual_memory().total
    mem_info['Available Memory'] = psutil.virtual_memory().available
    mem_info['Used Memory'] = psutil.virtual_memory().used
    mem_info['Memory Percentage'] = psutil.virtual_memory().percent
    system_info['Memory Information'] = mem_info

    # Disk Information
    disk_info = {}
    partitions = psutil.disk_partitions()
    for partition in partitions:
        disk_info[partition.device] = {
            'Mountpoint': partition.mountpoint,
            'File System': partition.fstype,
            'Total Size': psutil.disk_usage(partition.mountpoint).total,
            'Used Space': psutil.disk_usage(partition.mountpoint).used,
            'Free Space': psutil.disk_usage(partition.mountpoint).free,
            'Disk Percentage': psutil.disk_usage(partition.mountpoint).percent
        }
    system_info['Disk Information'] = disk_info

    # Network Information
    net_info = {}
    net_info['Hostname'] = platform.node()
    net_info['IP Address'] = psutil.net_if_addrs()
    system_info['Network Information'] = net_info

    return system_info

# Get the system information
system_information = get_system_information()

# Print the system information
for category, info in system_information.items():
    print(f'{category}:')
    if isinstance(info, dict):
        for key, value in info.items():
            print(f'{key}: {value}')
    else:
        print(info)
    print()
