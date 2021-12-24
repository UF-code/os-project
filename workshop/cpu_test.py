import psutil, time

cpu_count =  psutil.cpu_count()
print(cpu_count)
cpu_freq =  psutil.cpu_freq()
print(cpu_freq)
cpu_stats =  psutil.cpu_stats()
print(cpu_stats)
cpu_times =  psutil.cpu_times()
print(cpu_times)
cpu_times_percent =  psutil.cpu_times_percent()
print(cpu_times)

while True:
    # time.sleep(0.01)
    print("*"*20)
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    # print(cpu_percent)
    print(f"CPU_AVG_1 = {sum(cpu_percent)/len(cpu_percent)}")
    print("*"*20)
    cpu_percent_1 = psutil.cpu_percent(interval=1)
    print(f"CPU_AVG_2 = {cpu_percent_1}")
    
