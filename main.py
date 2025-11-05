import os
import subprocess
import time

print("🚀 Nuvix FullPack iniciado con Pycord slash+prefijo")

# Lista de bots
bots = [
    ("nuvix_ai", "NUVIX_AI_TOKEN"),
    ("nuvix_apps", "NUVIX_APPS_TOKEN"),
    ("nuvix_backup", "NUVIX_BACKUP_TOKEN"),
    ("nuvix_information", "NUVIX_INFORMATION_TOKEN"),
    ("nuvix_invoices", "NUVIX_INVOICES_TOKEN"),
    ("nuvix_machine", "NUVIX_MACHINE_TOKEN"),
    ("nuvix_management", "NUVIX_MANAGEMENT_TOKEN"),
    ("nuvix_sanctions", "NUVIX_SANCTIONS_TOKEN"),
    ("nuvix_system", "NUVIX_SYSTEM_TOKEN"),
    ("nuvix_tickets", "NUVIX_TICKETS_TOKEN"),
]

processes = []

for folder, token_var in bots:
    token = os.getenv(token_var)
    if not token:
        print(f"⚠️ Skipping {folder} — no token found for {token_var}")
        continue

    bot_path = os.path.join(os.getcwd(), folder, "bot.py")
    print(f"✅ Launching {folder} ...")
    p = subprocess.Popen(["python", bot_path])
    processes.append(p)
    time.sleep(1.5)

print("\n✨ All bots launched successfully!")

# 🔁 Mantener instancia activa (muy importante para Render)
try:
    while True:
        time.sleep(3600)
except KeyboardInterrupt:
    print("\n🛑 Stopping all bots...")
    for p in processes:
        p.terminate()
    print("✅ All bots stopped cleanly.")
