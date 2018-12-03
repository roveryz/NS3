from ctypes import CDLL

ns3core = CDLL("../build/lib/libns3module_core.so")

ret = ns3core.Simulator.Now()

print(ret)

pass