
# 🎞️ Film Öneri Sistemi

🎞️ Film Öneri Sistemi, kullanıcıların favori filmlerine benzer yapımları kolayca keşfetmesini sağlar. Python ile geliştirilen bu akıllı uygulama, modern bir arayüz sunarken `TF-IDF` ve `cosine similarity` teknikleriyle içerik bazlı öneriler üretir.


## 🚀 Özellikler

- 🎨 Modern kullanıcı arayüzü (CustomTkinter ile)
- 🔍 Film adına göre otomatik tamamlama (autocomplete)
- 🎬 TF-IDF tabanlı içerik filtreleme öneri sistemi
- 🧠 En yakın eşleşmeye göre 30 film önerisi
- 📋 Film adı, yönetmen ve çıkış tarihi ile öneri kartları
- 🧹 Arama ve sonuçları temizleme özelliği

## 🛠️ Kullanılan Teknolojiler

- `Python`
- `customtkinter` – Modern arayüz
- `pandas` – Veri okuma ve işleme
- `sklearn` – TF-IDF ve cosine similarity
- `difflib` – Yaklaşık eşleşme bulma
- `tkinter.StringVar` – Arayüz kontrolü

## 📂 Dosya Yapısı

```
📁 proje/
│
├── movies.csv                  # Film verilerini içeren CSV dosyası
├── main.py                     # Uygulama ana dosyası
└── README.md                   # Bu döküman
```

## 🧪 Gerekli Veri Formatı (`movies.csv`)

Aşağıdaki sütunları içermelidir:

- `title` – Filmin adı
- `genres` – Tür(ler)
- `keywords` – Anahtar kelimeler
- `tagline` – Kısa açıklama
- `cast` – Oyuncular
- `director` – Yönetmen
- `release_date` – Yayın tarihi

### Örnek:

```csv
title,genres,keywords,tagline,cast,director,release_date
Inception,Action Sci-Fi,dream heist,"Your mind is the scene of the crime","Leonardo DiCaprio",Christopher Nolan,2010
```

## ▶️ Uygulamayı Başlatma

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install pandas scikit-learn customtkinter
   ```

2. Uygulamayı çalıştırın:
   ```bash
   python main.py
   ```

## 📸 Görseller

![Python](https://github.com/user-attachments/assets/304c255d-a90d-4ff4-8af4-b5be19269eb5)


## 📌 Notlar

- `movies.csv` dosyasının aynı klasörde bulunması gerekir.
- `release_date` gibi opsiyonel alanlar veri setinizde yoksa, kodda ilgili yerleri düzenleyebilirsiniz.
- Daha fazla özellik eklemek isterseniz: kategoriye göre filtreleme, IMDb puanı gibi alanları da kullanabilirsiniz.

## 👨‍💻 Geliştirici

- **Ihab Mahmoud**  
- E-posta: _032190090@ogr.uludag.edu.tr_  
- **ABDULRUHMAN KATIA**  
- E-posta: _032290149@ogr.uludag.edu.tr_  
- **MOHAMAD NOUR ALMASRI**  
- E-posta: _032390142@ogr.uludag.edu.tr_  

---

Film severler için kişiselleştirilmiş önerilerle daha iyi bir izleme deneyimi! 🎬🍿
