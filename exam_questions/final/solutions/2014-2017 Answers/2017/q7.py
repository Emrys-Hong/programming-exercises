class MyTask(object):
    def __init__(self, deadline, duration):
        self.deadline = deadline
        self.duration = duration
        
    def __str__(self):
        return 'T(%d,%d)' %(self.deadline, self.duration)

def procrastination(assignments):
	start_times = {} # dictionary to keep track of the latest start time for a particular deadline
	for task in assignments:
		deadline = task.deadline
		duration = task.duration

		# If deadline already exists, decrease the start time for it
		if deadline in start_times:
			start_times[deadline] -= duration
		else:
			# If it doesn't exist, initialize the start time for this task as deadline - duration
			start_times[deadline] = deadline - duration

	# Iterate through the deadlines, find the actual start time after taking into account of all tasks

	actual_start_time = None # Initialize as None to begin with

	# Get deadlines sorted in descending order
	deadlines = sorted(start_times.keys(), reverse=True)

	for deadline in deadlines:
		current_start_time = start_times[deadline] # get the latest start time for this task
		duration = deadline - current_start_time # duration required for this task

		# If actual start time not initialized, set it as this deadline
		if actual_start_time == None:
			actual_start_time = current_start_time
		# If the current actual start time is after the current deadline, set it to be the start time for this task
		elif actual_start_time > current_start_time:
			actual_start_time = current_start_time
		# If start time is before or same as the start time for this task, decrease it by this task's duration to finish everything
		elif actual_start_time <= current_start_time:
			actual_start_time -= duration

	# If actual start time is negative, set it as -1
	actual_start_time = max(actual_start_time, -1)
	return actual_start_time

assignments = [ MyTask(9,1), MyTask(9,2), MyTask(7,1) ]
print procrastination(assignments)

assignments1 = [ MyTask(3,2), MyTask(3,2) ]
print procrastination(assignments1)

assignments2 = [ MyTask(9,1), MyTask(9,2), MyTask(4,3) ]
print procrastination(assignments2)

assignments3 = [MyTask(14,10), MyTask(33,2), MyTask(5,3), MyTask(14,1), MyTask(10,2)]
print procrastination(assignments3)


