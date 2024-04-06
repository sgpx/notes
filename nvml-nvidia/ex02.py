import pynvml as p

p.nvmlInit()
print("Driver Version:", p.nvmlSystemGetDriverVersion())
deviceCount = p.nvmlDeviceGetCount()
for i in range(deviceCount):
    handle = p.nvmlDeviceGetHandleByIndex(i)
    print("Device", i, ":", p.nvmlDeviceGetName(handle))
    print("fans", p.nvmlDeviceGetNumFans(handle))
    print("gpu cores", p.nvmlDeviceGetNumGpuCores(handle))
    print("fan speed", p)
p.nvmlShutdown()
