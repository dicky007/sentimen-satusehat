import pandas as pd

def load_slang_dictionary(filepath):
    # 1. Baca file Excel menggunakan pandas
    df = pd.read_excel(filepath)
    
    # 2. Hapus baris yang kosong/NaN jika ada
    df = df.dropna()
    
    # 3. Ambil kolom 1 (slang) dan kolom 2 (baku), lalu bersihkan spasi
    slang_dict = dict(zip(
        df.iloc[:, 0].astype(str).str.strip(), 
        df.iloc[:, 1].astype(str).str.strip()
    ))
    
    return slang_dict
#import re
#import pandas

#def load_slang_dictionary(filepath):
 #   clear_slangs = []
 #   with open(filepath, "r", encoding="utf-8", errors="replace") as slangs:
  #      for newlines in slangs:
  ##          strip_re = newlines.strip("\n")
    #        split = re.split(r'[:]', strip_re)
  #          clear_slangs.append(split)

  #  slangs = [[k.strip(), v.strip()] for k, v in clear_slangs]
  #  return {key: values for key, values in slangs}
