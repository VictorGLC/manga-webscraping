# Manga Downloader

Este projeto é um script de automação em Python desenvolvido para realizar o web scraping de capítulos de mangá diretamente do site Mugiwaras Oficial. O script organiza automaticamente os capítulos em pastas e baixa as páginas em alta resolução.

## Funcionalidades

- Download Automático: Percorre capítulos e páginas de forma sequencial.
- Flexibilidade de Títulos: Permite baixar mangás do site alterando o nome na URL.
- Organização de Arquivos: Cria uma estrutura de pastas baseada no número do capítulo (Capitulo 1, Capitulo 2, etc).
- Prevenção de Bloqueios: Utiliza Headers customizados (User-Agent e Referer) para simular navegação humana e evitar bloqueios do servidor.
- Delay: Intervalo entre requisições para respeitar os limites do servidor.

## Bibliotecas Utilizadas

- Requests: Para realizar as requisições HTTP e baixar os arquivos.
- BeautifulSoup4: Para analisar o HTML e encontrar as tags de imagem.
- OS e Time: Para manipulação de arquivos e controle de tempo.

## Pré-requisitos

Antes de rodar o script, você precisará instalar as bibliotecas necessárias:

```bash
pip install requests beautifulsoup4
```

## Configuração

No arquivo principal, você deve configurar as seguintes variáveis de acordo com sua necessidade:

1. Caminho de Destino:
Altere a variável BASE_PATH para o local onde deseja salvar os mangás.
```python
BASE_PATH = r"D:\Mangas\OnePiece"
```

2. Nome do Mangá e URL:
Você deve ajustar a BASE_URL inserindo o nome do mangá exatamente como ele aparece na URL do site (ex: dandadan, one-piece, boruto).
```python
# Substitua {manga} pelo nome do título no site
BASE_URL = "https://mugiwarasoficial.com/manga/nome-do-manga/capitulo-{chapter}/p/{page}"
```

3. Intervalo de Capítulos:
Na função main(), defina o capítulo inicial e o final:
```python
start_chap = 1
end_chap = 50
```

## Como Usar

1. Certifique-se de que a pasta de destino existe ou que o Python tem permissão para criá-la.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:
```bash
python nome_do_seu_arquivo.py
```
4. O script exibirá o progresso de cada página baixada no console.

## Implementação

- Identificação da Imagem: O script busca por tags img cujo ID comece com image-, padrão utilizado pelo leitor do site.
- Critério de Parada: O script incrementa as páginas (p/1, p/2, etc). Quando o site retorna um erro ou a tag de imagem não é encontrada, o script entende que o capítulo chegou ao fim e pula para o próximo.

## Aviso

Este script foi criado para fins de estudo e uso pessoal. O web scraping deve ser feito com responsabilidade.
- Não sobrecarregue os servidores.
- Respeite os termos de serviço do site.
- Não utilize este código para fins comerciais ou distribuição de conteúdo protegido por direitos autorais.

--- 

**Desenvolvido para organizar e facilitar a leitura offline de mangás.**