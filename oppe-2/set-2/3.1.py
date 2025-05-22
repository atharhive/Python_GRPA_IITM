
def get_call_counts(call_logs):
    call_counts = {}
    for log in call_logs:
        if log['name'] not in call_counts:
            call_counts[log['name']] = 0
        call_counts[log['name']] += 1
    return call_counts

def get_total_call_durations(call_logs):
    total_durations = {}
    for log in call_logs:
        if log['name'] not in total_durations:
            total_durations[log['name']] = 0
        total_durations[log['name']] += log['duration']
    return total_durations

def most_frequent_caller(call_logs):
    call_counts = get_call_counts(call_logs)
    total_durations = get_total_call_durations(call_logs)
    return max(
        call_counts,
        key=lambda name: (call_counts[name], total_durations[name])
    )


def process_call_logs(call_logs, task):
    
    
        if task == 'get_call_counts':
            return get_call_counts(call_logs)
        elif task == 'get_total_call_durations':
            return get_total_call_durations(call_logs)
        elif task == 'most_frequent_caller':
            return most_frequent_caller(call_logs)
        else:
            raise ValueError("Invalid task provided.")
    
