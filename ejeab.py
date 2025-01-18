import os
import pandas as pd
import subprocess

print(""" 
    Option1 - NginxServer 
    Option2 - ApacheServer 
    Option3 - ApachePHP
    Option4 - NginxPHP
    Option5 - NodeJS
""")

options = {
    "1": ['ab', '-n', '500', '-c', '10', 'http://127.0.1.1/'],
    "2": ['ab', '-n', '500', '-c', '10', 'http://127.0.1.1/'],
    "3": ['ab', '-n', '500', '-c', '10', 'http://127.0.1.1/index.php'],
    "4": ['ab', '-n', '500', '-c', '10', 'http://127.0.1.1/index.php'],
	"5": ['ab', '-n', '500', '-c', '10', 'http://127.0.0.1:3000/']
}

def save_to_excel(data, server_name):
    file_name = "benchmark_results.xlsx"
    try:
        existing_data = pd.read_excel(file_name)
    except FileNotFoundError:
        existing_data = pd.DataFrame()

    new_data = pd.DataFrame(list(data.items()), columns=["Métrica", "Valor"])
    new_data["Servidor"] = server_name
    combined_data = pd.concat([existing_data, new_data], ignore_index=True)
    combined_data.to_excel(file_name, index=False)
    print(f"Datos del servidor {server_name} añadidos al archivo {file_name}.")

def goBenchmark(num):
    if num in options:
        response = subprocess.run(options[num], text=True, capture_output=True, check=True)
        data = {}
        for line in response.stdout.splitlines():
            if ":" in line:
                extr = line.split(":", 1)
                key = extr[0].strip()
                value = extr[1].strip()
                data[key] = value

        for key, value in data.items():
            print(f"{key}: {value}")
        save_to_excel(data, f"Servidor {num}")
       
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")

select = input("Selecciona una opción para generar el reporte de benchmark: ")
goBenchmark(select)
