# number of jobs
n = int(input("Please enter the number of jobs: "))

# read the job details
jobs = []
for i in range(n):
    start_time = int(input("Please enter start time: "))
    end_time = int(input("Please enter end time: "))
    profit = int(input("Please enter profit value: "))
    jobs.append([start_time, end_time, profit])

# sort the jobs in increasing order of their end time
jobs.sort(key = lambda x:x[0])

# iterate through each job and assign it to Anirudh if it doesn't overlap with the current job
max_profit = 0
for job in jobs:
    if job[2] > max_profit:
        max_profit = job[2]
        max_job = job

#Remove the selected job from the jobs list
jobs.remove(max_job)

# calculate the remaining jobs and their profits
number_jobs = len(jobs)
total_earnings = 0
for job in jobs:
    total_earnings += job[2]
    
# print the output
print("Number of jobs left for other employees: ", number_jobs)
print("Total earnings left for other employees: ", total_earnings)
