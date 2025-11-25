import requests
import time
from bs4 import BeautifulSoup
import pandas as pd


URL_BASE = "https://quotes.toscrape.com/"

def raspar_citas(url):
    
    datos_extraidos = []            # Lista para guardar los datos

    time.sleep(2)                   # Pausa para no sobrecargar el servidor

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        respuesta = requests.get(url, headers=headers)              # Simulación de navegador real (buena práctica)

        if respuesta.status_code == 200:                            # Si la respuesta es ok (200) petición exitosa, sigue...
            print(f"Petición exitosa a: {url}")

            soup = BeautifulSoup(respuesta.content, 'html.parser')          # Parsear el contenido HTML

            contenedores_citas = soup.find_all("div", class_='quote')

            if not contenedores_citas:
                print("No se encontraron elementos de la clase 'quote'")
                return datos_extraidos
            
            for contenedor in contenedores_citas:
                
                texto_cita = contenedor.find('span', class_='text').text

                autor = contenedor.find('small', class_='author').text

                tags_lista = []
                tags_container = contenedor.find('div', class_='tags')

                for tag_a in tags_container.find_all('a', class_='tag'):            # Iterar sobre todas las etiquetas <a> dentro del contenedor 'tags'
                    tags_lista.append(tag_a.text)

                datos_extraidos.append({
                    'Cita': texto_cita.strip(),
                    'Autor': autor.strip(),
                    'Etiquetas': ', '.join(tags_lista)      # Unir las etiquetas en una sola cadena
                })

        else:
            print(f"Error al acceder a {url}. Código de estado: {respuesta.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        
    return datos_extraidos

if __name__ == "__main__":
    
    print("--- INICIANDO SCRAPER DE QUOTES.TOSCRAPE.COM ---")
    
    datos_recopilados = raspar_citas(URL_BASE)                  # 1. Recopilar los datos de la primera página

    if datos_recopilados:
        df_citas = pd.DataFrame(datos_recopilados)

        print("Datos recopilados")
        print(df_citas.to_string())                 # Muestra todas las columnas y filas sin truncar

        nombre_archivo = 'citas_famosas.csv'
        df_citas.to_csv(nombre_archivo, index=False, encoding='utf-8')
        print(f"\n✅ Datos guardados con éxito en {nombre_archivo}")
    else:
        print("Scraping finalizado. No se pudieron recopilar datos.")