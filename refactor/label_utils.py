import re


def clean_label(value):
    # Pastikan string dan buang spasi
    value = str(value).strip()
    # Ganti karakter non-alfanumerik dengan underscore
    value = re.sub(r'[^a-zA-Z0-9]', '_', value)
    
    # Hapus underscore ganda menjadi satu (e.g., 'year__2009' jadi 'year_2009')
    value = re.sub(r'_+', '_', value)
    
    # Jika diawali angka, tambahkan underscore di depan
    if value and value[0].isdigit():
        value = "_" + value
        
    # Hapus underscore di awal atau akhir jika ada
    return value.strip('_')


def generate_labels(value, prefix=""):
    clean_val = clean_label(value)
    
    if prefix:
        # Hapus underscore di akhir prefix agar tidak double saat digabung
        clean_prefix = prefix.rstrip('_')
        # Hasilnya: "year" + "_" + "2009" = "year_2009"
        return [f"{clean_prefix}_{clean_val}"]
    
    return [clean_val]

def get_label_config(prop):
    print(f"Mengonfigurasi properti: {prop}")
    is_numeric = input("Apakah properti ini numeric? (y/n): ").lower() == 'y'
    
    if is_numeric:
        # 2.a. Jika numeric, langsung minta prefix
        prefix = input(f"Masukkan prefix untuk {prop} (contoh: year_): ")
        return {"prefix": prefix, "is_numeric": True}
    else:
        # 2.b. Jika bukan numeric, tanya dulu apakah mau pakai prefix
        use_prefix = input("Apakah ingin menggunakan prefix? (y/n): ").lower() == 'y'
        if use_prefix:
            prefix = input(f"Masukkan prefix untuk {prop} (contoh: category_): ")
            return {"prefix": prefix, "is_numeric": False}
        else:
            # Tidak pakai prefix, hanya value saja
            return {"prefix": "", "is_numeric": False}