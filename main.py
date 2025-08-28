import requests, os, sys, random, string, time, shutil, telegram, asyncio
from telegram import InputMediaPhoto, InputMediaVideo
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

###

# pip install pygame
# pip install pillow
# pip install moviepy
# python3 -m pip install python-telegram-bot
# https://imagemagick.org/script/download.php#windows
# https://api.telegram.org/bot6458594445:AAEbjUrS8fM0KlOwxfAMAfbLYFNJeRWI7_U/getUpdates

###

channel_link = "t.me/" # grupo do telegram
token_bot = "" #token do bot
bot = telegram.Bot(token = token_bot)

###

def clear():
    try:
        os.system("cls")
    except:
        os.system("clear")

clear()

print(k)
select = input("\nFazer Upload Para qual Chat?\n[1] Chat \n[2] Chat_2 \n[3] Test Chat\n\nSelecionar: ")

if str(select) == "1":
    chat_id = "-" #ID do chat

if str(select) == "2":
    chat_id = "-" #ID do chat

if str(select) == "3":
    chat_id = "-" #ID do chat

###

itens_in_folder_files = os.listdir(os.path.dirname(sys.argv[0]) + "/files/")
path = os.path.dirname(sys.argv[0])
path_folder = path+"/files/"
itens_in_folder = os.listdir(path_folder)
# itens_in_folder_to_send = os.listdir(os.path.dirname(sys.argv[0]) + "/to_send/")

emoji = ["🥡", "🍱", "🍘", "🍙", "🍚", "🍛", "🍜", "🦪", "🍣", "🍤", "🍥", "🥮", "🍢", "🍦", "🍧", "🍨", "🍩", "🧁", "🍬", "🍭", "🍫", "🍡", "🍼", "🧃", "🍷", "🍸", "🍑", "🍒", "🍓", "🌺 Torne-se VIP: @korean014_bot 🌺"]
image = ['bmp','jpeg','jpg','png','gif','webp','tiff']
video = ['mp4','mov','mkv','avi','webm','3gp','flv', 'wmv', 'mpeg', 'ts']
audio = ['mp3', 'aac', 'ogg', 'wav']
to_log = []
media_group = []
folders= []

###

for i in os.listdir("files/"):
    if "." in i:
        del i
    else:
        os.makedirs(f"to_send/{i}")
        folders.append(i)

###

clear()
print("\n    🌐🌐🌐🌐 Editando Vídeos e/ou Fotos! 🌐🌐🌐🌐    \n\n\n") 

for fold in folders:
    for i in os.listdir(f"{path_folder}{fold}/"):

        id = ("".join(random.choices(string.ascii_letters + string.digits, k=8)))
        after_dot = (i.split(".")[-1]).lower()


        if after_dot in image:
            img = Image.open(f"files/{fold}/{i}")

            image_edited = ImageDraw.Draw(img)
            font = ImageFont.truetype("C:\\Windows\\Fonts\\Arial.ttf" , 30)
            image_edited.text((15, 15), f"{channel_link}", fill=(203, 203, 203), font=font)

            img.save(f'to_send/{fold}/PASTA_GRUPO{id}.{after_dot}')


        else:
            video_0 = VideoFileClip(f"files/{fold}/{i}")

            text = (
                TextClip(f' {channel_link}', fontsize=30, color="rgb(203, 203, 203)")
                .set_duration(video_0.duration)
                .set_position((15,  15))
            )

            composite = CompositeVideoClip([video_0, text])
            composite.fps = video_0.fps
            composite.audio = video_0.audio

            composite.write_videofile(f'to_send/{fold}/PASTA_GRUPO{id}.{after_dot}')



        if after_dot not in video + image:
            shutil.copyfile(f"{path_folder}{fold}{i}", f"{path}/to_send/PASTA_GRUPO{id}.{after_dot}")
    

###



clear()
print("\n    🔼🔼🔼🔼 Vídeos e/ou Fotos Editadas! Hora do Upload! 🔼🔼🔼🔼    \n\n\n") 



async def main():
    for i in folders:
        path_folders = os.listdir(f"to_send/{i}/")
        for n in path_folders:
            emoji_select = random.choice(emoji)

            if after_dot in image:
                print(f"✅ | [{emoji_select}] Ready - {n}")
                media_group.append(InputMediaPhoto(open(f"to_send/{i}/{n}", 'rb')))
            else:
                print(f"✅ | [{emoji_select}] Ready - {n}")
                media_group.append(InputMediaVideo(open(f"to_send/{i}/{n}", 'rb')))

        await asyncio.sleep(1)
        x=await bot.send_media_group(chat_id = chat_id, media = media_group, caption=emoji_select,
                                    write_timeout=300, read_timeout=300, connect_timeout=300)   
        media_group.clear()
        print(f"\n    🚀 [{i}] Upload 🚀\n")


asyncio.run(main())



time.sleep(1)

print("\n    ✅✅✅✅ Upload Finalizado ✅✅✅✅    \n\n\n") 

time.sleep(1)

clear()

time.sleep(0.5)

try:
    for i in os.listdir(os.path.dirname(sys.argv[0]) + "/to_send/"):
        shutil.rmtree(f"to_send/{i}")
        print(f"🔰 | Deleted - {i}")
except:
    print(f"\n❌ | Será Necessário Deletar Manualmente - {i}")

print("\n    🔰🔰🔰🔰 Arquivos Temporarios Deletados! 🔰🔰🔰🔰    \n\n\n") 
print("\n    💖💖💖💖 Fim 💖💖💖💖    \n\n\n")