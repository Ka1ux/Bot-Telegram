# 📦 Telegram Media Uploader Bot

Este projeto é um **bot para Telegram** que edita imagens e vídeos (adicionando marca d'água com o link do canal/grupo), organiza os arquivos em pastas temporárias e faz o **upload automático** para chats do Telegram.

---

## 🚀 Funcionalidades
- ✅ Adiciona **watermark** em imagens (`.jpg, .png, .gif, ...`)
- ✅ Insere **texto sobreposto** em vídeos (`.mp4, .avi, .mov, ...`)
- ✅ Suporte a **imagens, vídeos e áudios**
- ✅ Faz upload em **grupos/chats do Telegram**
- ✅ Apaga arquivos temporários automaticamente após o envio
- ✅ Exibe logs com **emojis aleatórios**

---

## 🛠️ Tecnologias utilizadas
- [Python 3](https://www.python.org/)
- [Pillow](https://pypi.org/project/Pillow/) → edição de imagens
- [MoviePy](https://zulko.github.io/moviepy/) → edição de vídeos
- [python-telegram-bot](https://python-telegram-bot.org/) → integração com o Telegram
- [ImageMagick](https://imagemagick.org/script/download.php) → requerido pelo MoviePy para renderização de textos em vídeos

---

## 📂 Estrutura de Pastas
```
📁 projeto/
 ┣ 📁 files/       # Pasta onde você coloca imagens e vídeos originais
 ┣ 📁 to_send/     # Pasta temporária criada automaticamente
 ┣ 📄 bot.py       # Script principal
 ┣ 📄 requirements.txt
 ┗ 📄 README.md
```

---

## ⚙️ Instalação

Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```

Crie e ative um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

No Windows, instale o **ImageMagick** e adicione ao PATH:  
👉 [Download aqui](https://imagemagick.org/script/download.php#windows)

---

## 🔑 Configuração
Edite no código:
```python
channel_link = "t.me/seu_canal"   # Link do grupo/canal
token_bot = "SEU_TOKEN_AQUI"      # Token do bot gerado no BotFather
```

E adicione os **chat_id** dos grupos:
```python
if str(select) == "1":
    chat_id = "-123456789"
```

---

## ▶️ Execução
Coloque os arquivos que deseja editar na pasta `files/` e rode:
```bash
python bot.py
```

O bot irá:
1. Editar imagens/vídeos adicionando a marca d'água
2. Mover os arquivos editados para `to_send/`
3. Enviar automaticamente para o grupo do Telegram escolhido
4. Apagar os arquivos temporários

---

## 📝 Exemplo de uso
- `files/fotos/` → contém imagens  
- `files/videos/` → contém vídeos  

Resultado após execução:
- `to_send/fotos/PASTA_GRUPOxxxxx.jpg`
- `to_send/videos/PASTA_GRUPOyyyyy.mp4`  
➡️ enviados para o Telegram com watermark.

---

## 📜 Licença
Este projeto é de uso livre para fins de estudo e automação.  
Sinta-se à vontade para modificar e melhorar 🚀
