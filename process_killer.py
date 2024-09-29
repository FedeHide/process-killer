import subprocess

# List of processes to kill
processes_to_kill = [
    # anti-cheats
    "PnkBstrA.exe", 
    "vgtray.exe", 
    # adobe
    '"Adobe Crash Processor.exe"', 
    '"Adobe Desktop Service.exe"', 
    "AdobeIPCBroker.exe", 
    "AdobeNotificationClient.exe",
    "AdobeNotificationHelper.exe",
    "AdobeUpdateService.exe",
    "CCXProcess.exe", 
    "CoreSync.exe", 
    '"Creative Cloud.exe"', 
    '"Creative Cloud Helper.exe"', 
    '"Creative Cloud UI Helper.exe"', 
    # others
    "PowerToys.exe",
    "gamingservices.exe",
    "gamingservices.exe"
    "GamingServicesNet.exe"
]

# Function to kill a process by name
def kill_process(process_name):
    try:
        subprocess.run(f'taskkill /IM {process_name} /F', shell=True, check=True)
    except subprocess.CalledProcessError:
        pass  # Silently handle the error and continue

# Run the script to kill all processes in the list
def kill_all_processes():
    for process in processes_to_kill:
        kill_process(process)

# Start execution
kill_all_processes()

# Wait for user to press any key before exiting
input("Press any key to exit...")
