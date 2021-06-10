import GPUtil
from tabulate import tabulate

def gpu_info():
    gpus = GPUtil.getGPUs()

    #headers for formatting output
    headers = ('id','name','load','GPU free mem','GPU used mem', 'GPU total mem','GPU temperature')
    tablefmt = "pretty"
    gpus_list = []

    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f'{round(gpu.load*100)}%'
        gpu_free_memory = f'{gpu.memoryFree}MB'
        gpu_used_memory = f'{gpu.memoryUsed}MB'
        gpu_total_memory = f'{gpu.memoryTotal}MB'
        gpu_temp = f'{gpu.temperature}'

        gpus_list.append((gpu_id,gpu_name,gpu_load,gpu_free_memory,gpu_used_memory,gpu_total_memory,gpu_temp))

        return str(tabulate(gpus_list,headers,tablefmt))


if __name__ == '__main__':
    print(gpu_info())
