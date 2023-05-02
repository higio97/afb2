import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID", "#"))
api_hash = os.getenv("API_HASH", "#")
bot_token = os.getenv("BOT_TOKEN", "#")
# =========================================================== #

db_url = os.getenv("DB_URL", "#")
db_name = os.getenv("DB_NAME", "telegram") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.getenv("CHANNEL_1", "#"))
channel_2 = int(os.getenv("CHANNEL_2", "#")) #untuk group comentar user 
channel_3 = int(os.getenv("CHANNEL_3", ""))
channel_log = int(os.getenv("CHANNEL_LOG", "#"))
# =========================================================== #

id_admin = int(os.getenv("ID_ADMIN", "907544310"))
admin_username = os.getenv("ADMIN_USERNAME", "troublescope")
# =========================================================== #

batas_kirim = int(os.getenv("BATAS_KIRIM", 5))
batas_talent = int(os.getenv("BATAS_TALENT", 10))
batas_daddy_sugar = int(os.getenv("BATAS_DADDY_SUGAR", 10))
batas_moansgirl = int(os.getenv("BATAS_MOANSGIRL", 10))
batas_moansboy = int(os.getenv("BATAS_MOANSBOY", 10))
batas_gfrent = int(os.getenv("BATAS_GFRENT", 10))
batas_bfrent = int(os.getenv("BATAS_BFRENT", 10))
# =========================================================== #

biaya_kirim = int(os.getenv("BIAYA_KIRIM", 10))
biaya_talent = int(os.getenv("BIAYA_TALENT", 80))
biaya_daddy_sugar = int(os.getenv("BIAYA_DADDY_SUGAR", 70))
biaya_moansgirl = int(os.getenv("BIAYA_MOANSGIRL", 60))
biaya_moansboy = int(os.getenv("BIAYA_MOANSBOY", 50))
biaya_gfrent = int(os.getenv("BIAYA_GFRENT", 40))
biaya_bfrent = int(os.getenv("BIAYA_BFRENT", 30))
# =========================================================== #

hastag = os.getenv("HASTAG", "#FypGirl #FypBoy #FypAsk #FypStory").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.getenv("PIC_BOY", "https://telegra.ph/file/3686aad6f6385f775b379.jpg")
pic_girl = os.getenv("PIC_GIRL", "https://telegra.ph/file/8dfde5a5e085e78bd17e4.jpg")
pic_nonmember= os.getenv("PIC_NONMEMBER", "https://telegra.ph/file/c8f39a51bb5054433e7e9.jpg")
pic_main = os.getenv("PIC_MAIN", "https://telegra.ph/file/8d7242ca9a11916fcea45.jpg")
topup_link = os.getenv("TOPUP_LINK", "")
# =========================================================== #
pesan_topup = os.getenv("PESAN_TOPUP", f"""
Halo kak.
untuk melakukan Top up coin, gunakan tombol dibawah ⬇️.
kemudian konfirmasi ke admin ya jangan lupa bukti transaksinya 🥰,
jika tidak melakukan konfirmasi ke admin, maka kami anggap sedekah.
"""
)
pesan_join = os.getenv("PESAN_JOIN", "Tidak Dapat Diakses Harap Join Terlebih Dahulu")
start_msg = os.getenv("START_MSG", "Hai {mention} 🌱\n\nSaya adalah Bot Auto Post, Semua Pesan Yang Kamu Kirim Akan Masuk Ke Channel @findyourpartnerbase Secara Anonymous. Untuk Bantuan Ketik /help")

gagalkirim_msg = os.getenv("GAGAL_KIRIM", """
{mention}, Pesan Mu Gagal Terkirim Silahkan Gunakan Hashtag Berikut:
#FypGirl / #FypBoy Untuk cari partner.
#FypAsk Untuk bertanya 
#FypStory Untuk berbagi cerita.
""")
