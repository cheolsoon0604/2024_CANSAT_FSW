import time

def Time_Init() :
    start_time = time.monotonic_ns()

def Time_Return():
    ns_time = time.time_ns() % 1000000000
    ms_time = ns_time // 1000000

    timestamp = time.time()
    local_time = time.localtime(timestamp)
    formatted = time.strftime("%Y%m%d_%H%M%S", local_time)

    return formatted + str(ms_time)

def Process_Time() : # TODO : Process Time Return 함수 구현
    return