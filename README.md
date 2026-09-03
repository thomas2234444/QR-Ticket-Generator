🎟️ QR Ticket Generator

A Python-based personalized ticket generator that reads guest information from an Excel file, generates a unique WhatsApp confirmation QR code for each guest, adds the guest's name to a predefined ticket template, and exports the finished tickets as PNG images.

✨ Features
📊 Reads guest names automatically from an Excel file.
🎟️ Generates a personalized ticket for every guest.
👤 Adds the guest's name directly to the ticket design.
📱 Generates a unique QR code for each guest.
💬 QR code opens WhatsApp with a pre-filled attendance confirmation message.
🖼️ Uses a custom ticket template/image.
📁 Automatically creates an output folder for generated tickets.
🔤 Supports custom fonts for ticket names.
⚡ Generates tickets for all guests automatically with a single command.
🛠️ Technologies Used
Python 3
Pandas – Reading guest information from Excel
QRCode – Generating QR codes
Pillow (PIL) – Editing ticket images and adding text
OpenPyXL – Excel file support through Pandas
urllib.parse – Encoding WhatsApp messages
📂 Project Structure
QR-Ticket-Generator/
│
├── main.py
├── guests.xlsx
├── Dump Ticket.png
├── ArefRuqaa-Regular.ttf
├── tickets/
│   ├── Ahmed.png
│   ├── John.png
│   ├── Maria.png
│   └── ...
│
├── requirements.txt
└── README.md
File Description
File / Folder	Description
main.py	Main Python script
guests.xlsx	Excel file containing guest names
Dump Ticket.png	Ticket design/template
ArefRuqaa-Regular.ttf	Custom font used for guest names
tickets/	Generated personalized tickets
requirements.txt	Required Python packages
README.md	Project documentation
📊 Excel File Format

The script expects an Excel file named:

guests.xlsx

The Excel file must contain a column named:

Name
Example
Name
Ahmed Mohamed
John Smith
Maria George
Thomas Amir

The script will automatically generate one ticket for every row.

⚙️ Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/QR-Ticket-Generator.git

Navigate into the project:

cd QR-Ticket-Generator
2. Create a virtual environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt

If you don't have a requirements.txt file yet, you can install the packages manually:

pip install pandas qrcode[pil] openpyxl pillow
🚀 Usage

Make sure the following files are inside the project folder:

main.py
guests.xlsx
Dump Ticket.png
ArefRuqaa-Regular.ttf

Then run:

python main.py

The program will:

Read the guest names from guests.xlsx.
Load the ticket template.
Generate a WhatsApp confirmation message for each guest.
Create a QR code containing the WhatsApp link.
Add the guest's name to the ticket.
Add the QR code to the ticket.
Save the finished ticket inside the tickets folder.
📱 How the QR Code Works

For every guest, the program creates a personalized WhatsApp message.

For example, if the guest's name is:

Ahmed Mohamed

The generated message will be:

أنا Ahmed Mohamed و بأكد حضوري

The message is URL-encoded and converted into a WhatsApp link:

https://wa.me/PHONE_NUMBER?text=...

The link is then converted into a QR code.

When the guest scans the QR code, WhatsApp opens with the confirmation message already written.

🎨 Customization
Change the WhatsApp Number

Inside main.py, change:

phone_number = "+201000000000"

to the destination WhatsApp number.

Use the international format without spaces.

For example:

phone_number = "+201234567890"
Change the Font

The project currently uses:

font_path = "ArefRuqaa-Regular.ttf"

You can replace it with another .ttf font:

font_path = "YourFont.ttf"

Make sure the font file exists in the project directory.

Change Font Size

Guest name:

font = ImageFont.truetype(font_path, 55)

Details:

small_font = ImageFont.truetype(font_path, 35)

Increase or decrease these values depending on your ticket design.

Change Guest Name Position

The guest name is currently placed at:

draw.text(
    (300, 350),
    name,
    fill="#E0DCD8",
    font=font
)

The coordinates:

(300, 350)
 ↑     ↑
 X     Y

You can change them to position the name anywhere on the ticket.

Change QR Code Size

The QR code is resized to:

qr = qr.resize((120, 120))

For example:

qr = qr.resize((150, 150))
Change QR Code Position

The QR code is currently placed at:

ticket.paste(qr, (185, 880))

Change the coordinates to move it:

ticket.paste(qr, (200, 850))
📤 Output

After running the program, the generated tickets will be stored automatically in:

tickets/

Example:

tickets/
├── Ahmed Mohamed.png
├── John Smith.png
├── Maria George.png
└── Thomas Amir.png

Each ticket contains:

👤 Guest name
🎟️ Ticket design
📱 WhatsApp confirmation QR code
🔒 Security & Privacy

The project uses guest names from the Excel file to generate personalized tickets.

Important

Do not upload real guest information to a public GitHub repository.

Add the following to .gitignore:

guests.xlsx
tickets/
venv/
__pycache__/
*.pyc

This prevents private guest data and generated tickets from being committed accidentally.

📄 Recommended requirements.txt

Create a file named:

requirements.txt

and add:

pandas
qrcode[pil]
openpyxl
Pillow

Then anyone can install the project's dependencies using:

pip install -r requirements.txt
🧠 How It Works
              guests.xlsx
                   │
                   ▼
             Read Guest Data
                   │
                   ▼
            Get Guest Name
                   │
          ┌────────┴────────┐
          ▼                 ▼
   Create WhatsApp      Load Ticket
       Message            Template
          │                 │
          ▼                 │
     Generate QR            │
          │                 │
          └────────┬────────┘
                   ▼
            Add Guest Name
                   │
                   ▼
             Add QR Code
                   │
                   ▼
             Save Ticket
                   │
                   ▼
              tickets/
💡 Possible Future Improvements

Some useful improvements that could be added:

Export tickets as PDF.

Generate unique ticket IDs.

Add guest email/phone fields.

Add QR codes containing ticket IDs.

Validate Excel data before processing.

Handle duplicate guest names.

Automatically center long guest names.

Automatically resize text based on name length.

Add multiple Excel columns to the ticket.

Create a graphical user interface (GUI).

Add a progress bar.

Generate a ZIP file containing all tickets.

Add database support.

Add ticket verification through an API.

🤝 Contributing

Contributions are welcome!

Fork the repository.
Create a new branch:
git checkout -b feature/new-feature
Make your changes.
Commit your changes:
git commit -m "Add new feature"
Push the branch:
git push origin feature/new-feature
Open a Pull Request.
📜 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Thomas Amir

If you found this project useful, consider giving the repository a ⭐ on GitHub.

⭐ Project Summary

A simple automated ticket-generation system built with Python that transforms an Excel guest list into personalized event tickets with WhatsApp confirmation QR codes.
