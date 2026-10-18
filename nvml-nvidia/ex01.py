from pynvml import *
from pynvml.smi import nvidia_smi

nvmlInit()
print("Driver Version:", nvmlSystemGetDriverVersion())
deviceCount = nvmlDeviceGetCount()
for i in range(deviceCount):
    handle = nvmlDeviceGetHandleByIndex(i)
    print("Device", i, ":", nvmlDeviceGetName(handle))


nvsmi = nvidia_smi.getInstance()
print(nvsmi.DeviceQuery('memory.free, memory.total'))
nvmlShutdown()
