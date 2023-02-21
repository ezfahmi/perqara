# perqara

To solve this problem, we can follow the following approach:

Read the input values, i.e. the number of jobs and the job details for each job.
Sort the jobs in increasing order of their end time, so that we can start with the job that ends first.
Keep track of the current job that Anirudh is working on and the total profit earned by Anirudh so far.
Iterate through each job in the sorted list of jobs and check if the job overlaps with the current job that Anirudh is working on. If it doesn't overlap, assign this job to Anirudh and update the current job and total profit. If it overlaps, skip this job as Anirudh can't do overlapping jobs.
At the end, the remaining jobs and their profits can be calculated by subtracting the total profit earned by Anirudh from the sum of profits of all jobs.
