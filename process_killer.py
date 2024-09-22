import subprocess

# Lista de nombres de procesos a terminar
processes_to_kill = [
    "vgtray.exe", 
    "CoreSync.exe", 
    '"Adobe Crash Processor.exe"', 
    '"Creative Cloud.exe"', 
    "CCXProcess.exe", 
    '"Adobe Desktop Service.exe"', 
    '"Creative Cloud Helper.exe"', 
    "AdobeIPCBroker.exe", 
    '"Creative Cloud UI Helper.exe"', 
    "AdobeNotificationClient.exe", 
    "PnkBstrA.exe", 
    "PowerToys.exe"
]

# Función para matar un proceso por nombre
def kill_process(process_name):
    try:
        subprocess.run(f'taskkill /IM {process_name} /F', shell=True, check=True)
    except subprocess.CalledProcessError:
        pass  # Silenciar el error y continuar

# Ejecutar el script para matar todos los procesos de la lista
def kill_all_processes():
    for process in processes_to_kill:
        kill_process(process)

# Iniciar la ejecución
kill_all_processes()

