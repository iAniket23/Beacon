import psutil

def get_running_apps():
    running_apps = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Get process name
            process_name = proc.info['name']
            running_apps.append(process_name)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return running_apps

if __name__ == "__main__":
    running_apps = get_running_apps()
    if running_apps:
        print("Running Applications:")
        for app in running_apps:
            print(app)
    else:
        print("No running applications found.")
