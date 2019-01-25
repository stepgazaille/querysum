allow_gpu_growth = True
per_process_gpu_memory_fraction = None

if per_process_gpu_memory_fraction is None:
    print("allow_gpu_growth is", allow_gpu_growth)
else:
    print("per_process_gpu_memory_fraction is", per_process_gpu_memory_fraction)


per_process_gpu_memory_fraction = 0.1
if per_process_gpu_memory_fraction is None:
    print("allow_gpu_growth is", allow_gpu_growth)
else:
    print("per_process_gpu_memory_fraction is", per_process_gpu_memory_fraction)


if per_process_gpu_memory_fraction is not None and allow_gpu_growth:
    raise ValueError("allow_gpu_growth must be False if per_process_gpu_memory_fraction is set")


