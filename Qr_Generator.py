import pandas as pd
import qrcode
import os
from urllib.parse import quote
from PIL import Image, ImageDraw, ImageFont



# ==============================
# إعدادات أساسية
# ==============================

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ملف الاكسيل
excel_file = os.path.join(BASE_DIR, "guests.xlsx")
template_file = os.path.join(BASE_DIR, "Dump Ticket.png")
# صورة التذكرة
output_folder = os.path.join(BASE_DIR, "tickets")

# رقم الواتساب اللي هتوصل عليه الرسائل
phone_number = "+201000000000"  # استبدل هذا بالرقم الفعلي




# فولدر حفظ التذاكر
# إنشاء الفولدر لو مش موجود
os.makedirs(output_folder, exist_ok=True)

# ==============================
# قراءة ملف Excel
# ==============================

df = pd.read_excel(excel_file)

# ==============================
# تحميل تصميم التذكرة
# ==============================

template = Image.open(template_file)

# ==============================
# الخطوط
# ==============================

# لو عندك خط مخصص حطه هنا
# مثال:

# font_path = "Amiri-Bold.ttf"

font_path = "ArefRuqaa-Regular.ttf"

# خط الاسم
font = ImageFont.truetype(font_path, 55)

# خط التفاصيل
small_font = ImageFont.truetype(font_path, 35)

# ==============================
# Loop على كل شخص
# ==============================

for index, row in df.iterrows():

    # البيانات من الاكسيل   
    name = str(row['Name'])    # ==============================
    # إنشاء رسالة واتساب
    # ==============================

    message = f"أنا {name} و بأكد حضوري "

    encoded_message = quote(message)

    whatsapp_link = (
        f"https://wa.me/{phone_number}?text={encoded_message}"
    )

    # ==============================
    # إنشاء QR
    # ==============================

    qr = qrcode.make(whatsapp_link)

    # حجم الـ QR
    qr = qr.resize((120, 120))

    # ==============================
    # نسخ التيمبلت
    # ==============================

    ticket = template.copy()

    draw = ImageDraw.Draw(ticket)

    # ==============================
    # كتابة الاسم
    # ==============================

    draw.text(
        (300, 350),
        name,
        fill="#E0DCD8",
        font=font
    )



    # ==============================
    # إضافة QR أسفل الشمال
    # ==============================

    ticket.paste(qr, (185, 880))

    # ==============================
    # حفظ التذكرة
    # ==============================

    save_path = os.path.join(
        output_folder,
        f"{name}.png"
    )

    ticket.save(save_path)

    print(f"Created ticket for {name}")

print("===================================")
print("All tickets created successfully!")
print("===================================")
 