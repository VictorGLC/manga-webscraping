import os
import requests
from bs4 import BeautifulSoup
import time

BASE_PATH = r"D:\Mangas\NomeDoManga"
BASE_URL = "https://mugiwarasoficial.com/manga/nome-do-manga/capitulo-{chapter}/p/{page}"

# headers para o site nao bloquear a requisiçao
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Referer": "https://mugiwarasoficial.com/"
}

def download_manga_page(chapter, page, chapter_folder):
    url = BASE_URL.format(chapter=chapter, page=page)
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            return False
        
        soup = BeautifulSoup(response.text, 'html.parser')

        # o seletor busca qualquer tag img que contenha 'image-' no id
        img_tag = soup.find('img', id=lambda x: x and x.startswith('image-'))

        img_url = img_tag.get('data-src') or img_tag.get('src').strip()

        # define o nome do arquivo
        extension = img_url.split('.')[-1].split('?')[0] # pega .jpg ou .png
        filename = os.path.join(chapter_folder, f"{page:02d}.{extension}")

        # baixa a imagem
        img_data = requests.get(img_url, headers=HEADERS).content
        with open(filename, 'wb') as handler:
            handler.write(img_data)
        
        print(f"Capítulo {chapter} - Página {page}: Baixada com sucesso.")
        return True

    except Exception as e:
        print(f"Erro ao processar página {page} do capítulo {chapter}: {e}")
        return False

def main():
    start_chap = 1
    end_chap = 50

    print(f"Iniciando download do capitulo {start_chap} ao {end_chap}...")

    for chapter in range(start_chap, end_chap + 1):
        # cria a pasta do capítulo
        chapter_folder = os.path.join(BASE_PATH, f"Capitulo {chapter}")
        os.makedirs(chapter_folder, exist_ok=True)
        
        page = 1
        while True:
            success = download_manga_page(chapter, page, chapter_folder)
            
            if not success: # falha se o capitulo acabar ou nao existir
                print(f"Fim do Capítulo {chapter}.")
                break
            
            page += 1
            time.sleep(0.5) # pausa para evitar banimento por IP

    print("Processo concluído!")

if __name__ == "__main__":
    main()