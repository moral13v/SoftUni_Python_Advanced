jobs = [int(x) for x in input().split(", ")]
needed_job_index = int(input())
needed_job = jobs[needed_job_index]

jobs_until_target = [x for x in jobs if x <= needed_job]
clock_cycles = sum(jobs_until_target)

print(clock_cycles)