# import re


# def clean_label(value):

#     value = str(value).strip()

#     value = re.sub(
#         r'[^a-zA-Z0-9]',
#         '_',
#         value
#     )

#     if value[0].isdigit():
#         value="_"+value

#     return value


# def generate_labels(
#     property_name,
#     value,
#     pbn=False
# ):

#     if value is None:
#         return []

#     value=str(value).strip()

#     # tahun
#     if property_name in ["birth", "death", "year"]:

#         if pbn:
#             return [f"year_{value}"]

#         if property_name == "year":
#             return [f"year_{value}"]

#         if property_name == "birth":
#             return [f"birth_{value}"]

#         if property_name == "death":
#             return [f"death_{value}"]


#     # multiple value
#     separators=[",",";"]

#     values=[value]

#     for sep in separators:

#         if sep in value:

#             values=[
#                 v.strip()
#                 for v in value.split(sep)
#                 if v.strip()
#             ]

#             break


#     # kalau dipisah spasi khusus category
#     if property_name=="category":

#         values=value.split()


#     return [
#         clean_label(v)
#         for v in values
#     ]

import re

# def generate_labels(value, prefix=""):
#     clean_val = clean_label(value)
#     # Jika ada prefix, gabungkan dengan underscore, jika tidak, hanya value saja
#     if prefix:
#         return [f"{prefix}{clean_val}"]
#     return [clean_val]

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
        
    # Hapus underscore di awal atau akhir jika ada (opsional tapi disarankan)
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