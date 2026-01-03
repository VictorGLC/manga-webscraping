import os
import requests
from bs4 import BeautifulSoup

BASE_PATH = r"D:\Mangas\NomeManga"
BASE_URL = "https://mangalivre.blog/manga/nome-manga"

# headers para o site nao bloquear a requisiçao
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Referer": "https://mangalivre.blog"
}

session = requests.Session() # continua a sessao da requisicao
session.headers.update(HEADERS)

def download_manga_chapter(url_chapter, chapter_folder):
    try:
        response = session.get(url_chapter)
        soup = BeautifulSoup(response.text, 'html.parser')
        divs_img = soup.find_all('div', id=lambda x: x and x.startswith('page-'))
        
        if not divs_img:
            print("Nenhuma imagem encontrada no capítulo.")
            return

        page = 1
        for div in divs_img:
            img_tag = div.find('img')
            img_url = img_tag.get('src').strip()

            extension = img_url.split('.')[-1].split('?')[0] # pega .jpg ou .png
            img_data = requests.get(img_url, headers=HEADERS).content
            filename = os.path.join(chapter_folder, f"{page:02d}.{extension}")

            with open(filename, 'wb') as handler:
                handler.write(img_data)

            page+=1

    except Exception as e:
        print(f"Erro ao processar capítulo {url_chapter}: {e}")
    
def get_chapters(url_manga):
    response = session.get(url_manga)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    chapters = {}
    chapter_links = soup.find_all('a', class_='chapter-link')

    for link in chapter_links:
        chapter_number = link.text.strip().split()[1].strip(":")  # extrai o número do capítulo
        chapters[chapter_number] = link['href']
    
    return chapters

def main():
    start_chap, end_chap = 68, 69

    print(f"Iniciando download do capitulo {start_chap} ao {end_chap}...")
    chapters = get_chapters(BASE_URL)

    for chapter in range(start_chap, end_chap + 1):
        # cria a pasta do capítulo
        chapter_folder = os.path.join(BASE_PATH, f"Capitulo {chapter}")
        os.makedirs(chapter_folder, exist_ok=True)

        download_manga_chapter(chapters[str(chapter)], chapter_folder)

    print("Processo concluído!")

if __name__ == "__main__":
    main()