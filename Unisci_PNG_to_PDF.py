import os
import re
from PIL import Image

def unisci_png_in_pdf(cartella_immagini, nome_pdf_output):
    # 1. Recupera tutti i file nella cartella
    file_nella_cartella = os.listdir(cartella_immagini)
    
    # 2. Filtra solo i file che finiscono con .png
    png_files = [f for f in file_nella_cartella if f.lower().endswith('.jpg')]
    
    if not png_files:
        print("Nessun file PNG trovato nella cartella specificata.")
        return

    # 3. ORDINAMENTO CORRETTO (Natural Sort)
    # Questa riga estrae il numero dal nome del file per ordinarli come 1, 2... 10, 11... 198
    # Evita l'errore del sorting alfabetico (1, 10, 100, 2...)
    png_files.sort(key=lambda f: int(re.search(r'\d+', f).group()) if re.search(r'\d+', f) else 0)
    
    # Crea i percorsi completi per ogni immagine
    percorsi_immagini = [os.path.join(cartella_immagini, f) for f in png_files]
    
    print(f"Trovate {len(percorsi_immagini)} immagini. Inizio la conversione...")

    # 4. Converti e unisci in PDF
    # I PDF non supportano la trasparenza dei PNG (RGBA), quindi convertiamo tutto in RGB
    lista_immagini_pil = []
    
    # Apriamo la prima immagine (sarà la prima pagina del PDF)
    prima_immagine = Image.open(percorsi_immagini[0]).convert('RGB')
    
    # Apriamo tutte le altre immagini dalla seconda in poi
    for percorso in percorsi_immagini[1:]:
        img = Image.open(percorso).convert('RGB')
        lista_immagini_pil.append(img)
        
    # Salva il tutto nel PDF finale
    prima_immagine.save(nome_pdf_output, save_all=True, append_images=lista_immagini_pil)
    
    print(f"Successo! Il PDF è stato salvato come: {nome_pdf_output}")

# --- CONFIGURAZIONE ---
# Metti "." se lo script si trova nella stessa cartella delle immagini, 
# oppure inserisci il percorso assoluto (es. "C:/Utenti/Nome/Desktop/Immagini")
cartella_target = "." 
pdf_finale = "documento_unito.pdf"

unisci_png_in_pdf(cartella_target, pdf_finale)