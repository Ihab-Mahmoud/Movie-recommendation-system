import customtkinter as ctk # Modern arayüzler oluşturmak için
import pandas as pd # Veri dosyalarını okumak ve işlemek için
import difflib # Benzer metinleri bulmak için
from tkinter import StringVar, END # Giriş alanlarını kontrol etmek için
from sklearn.feature_extraction.text import TfidfVectorizer # Metni sayılara dönüştürmek için
from sklearn.metrics.pairwise import cosine_similarity # Metinler arası benzerliği ölçmek için

# Görünüm modunu ve varsayılan renk temasını ayarla
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class MovieRecommendationApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Pencereyi yapılandır
        self.title("🎞️ Film Öneri Sistemi")
        self.geometry("800x600")
        self.minsize(600, 400)
        
        # Öneri sistemini başlat
        self.initialize_recommendation_system()
        
        # Ana konteyneri oluştur
        self.main_container = ctk.CTkFrame(self)
        self.main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Başlık
        self.title_label = ctk.CTkLabel(
            self.main_container,
            text="🎞️ Film Öneri Sistemi",
            font=("Segoe UI", 28, "bold")
        )
        self.title_label.pack(pady=(20, 30))
        
        # Arama çerçevesi


        self.search_frame = ctk.CTkFrame(self.main_container)
        self.search_frame.pack(fill="x", padx=40, pady=(0, 20),)

        self.search_label = ctk.CTkLabel(self.search_frame, text="🎬 Lütfen favori filminizin adını girin:", anchor="w")
        self.search_label.pack(fill="x", padx=10, pady=(0, 5))

        # Otomatik tamamlamalı arama girişi

        self.search_var = StringVar()
        self.search_entry = ctk.CTkEntry(
            self.search_frame,
            textvariable=self.search_var,
            placeholder_text="Film adı giriniz...",
            font=("Segoe UI", 14),
            height=40,
            width=400
        )
        self.search_entry.pack(side="left", padx=(0, 10), fill="x", expand=True)
        
        # Otomatik tamamlama işlevini bağla
        self.search_var.trace("w", self.update_autocomplete)
        
        # Düğmeler
        self.search_button = ctk.CTkButton(
            self.search_frame,
            text="🔍 Önerileri Getir",
            font=("Segoe UI", 14, "bold"),
            height=40,
            command=self.get_recommendations
        )
        self.search_button.pack(side="left", padx=(0, 10))
        
        self.clear_button = ctk.CTkButton(
            self.search_frame,
            text="🧹 Temizle",
            font=("Segoe UI", 14),
            height=40,
            fg_color="#e0e0e0",
            text_color="#333333",
            hover_color="#d0d0d0",
            command=self.clear_all
        )
        self.clear_button.pack(side="left")
        
        # Sonuç alanı
        self.results_frame = ctk.CTkFrame(self.main_container)
        self.results_frame.pack(fill="both", expand=True, padx=40, pady=(0, 20))
        
        self.results_text = ctk.CTkTextbox(
            self.results_frame,
            font=("Segoe UI", 14),
            wrap="word",
            height=300
        )
        self.results_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Otomatik tamamlama liste kutusu
        self.autocomplete_listbox = None
        
    def initialize_recommendation_system(self):
        """Film öneri sistemini başlat"""
        try:
            # Film verilerini yükle
            self.movies_data = pd.read_csv('movies.csv')
            
            # İlgili özellikleri seç
            selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
            
            # Boş (null) değerleri boş string ile değiştir
            for feature in selected_features:
                self.movies_data[feature] = self.movies_data[feature].fillna('')
            
            # Özellikleri birleştir
            self.movies_data['combined_features'] = self.movies_data[selected_features].apply(
                lambda x: ' '.join(x), axis=1
            )
            
            # Metni özellik vektörlerine dönüştür
            self.vectorizer = TfidfVectorizer()
            self.feature_vectors = self.vectorizer.fit_transform(self.movies_data['combined_features'])
            
            # Benzerlik matrisini hesapla
            self.similarity = cosine_similarity(self.feature_vectors)
            
            # Tüm film adlarının listesini al
            self.movie_titles = self.movies_data['title'].tolist()
            
        except Exception as e:
            print(f"Öneri sistemi başlatılırken hata oluştu: {e}")
            self.movie_titles = []
    
    def update_autocomplete(self, *args):
        """Kullanıcı yazdıkça otomatik tamamlama önerilerini güncelle"""
        search_text = self.search_var.get().lower()
        if not search_text:
            self.hide_autocomplete()
            return
            
        matches = difflib.get_close_matches(search_text, self.movie_titles, n=5, cutoff=0.3)
        
        if matches:
            self.show_autocomplete(matches)
        else:
            self.hide_autocomplete()
    
    def show_autocomplete(self, matches):
        """Otomatik tamamlama önerilerini göster"""
        self.hide_autocomplete()
        
        x = self.search_entry.winfo_rootx()
        y = self.search_entry.winfo_rooty() + self.search_entry.winfo_height()
        
        self.autocomplete_listbox = ctk.CTkToplevel(self)
        self.autocomplete_listbox.wm_overrideredirect(True)
        self.autocomplete_listbox.geometry(f"+{x}+{y}")
        
        for match in matches:
            btn = ctk.CTkButton(
                self.autocomplete_listbox,
                text=match,
                command=lambda m=match: self.select_autocomplete(m),
                fg_color="transparent",
                text_color="#333333",
                hover_color="#e0e0e0",
                anchor="w",
                height=30
            )
            btn.pack(fill="x", padx=1, pady=1)
    
    def hide_autocomplete(self):
        """Otomatik tamamlama önerilerini gizle"""
        if self.autocomplete_listbox:
            self.autocomplete_listbox.destroy()
            self.autocomplete_listbox = None
    
    def select_autocomplete(self, movie):
        """Otomatik tamamlamadan seçimi işle"""
        self.search_var.set(movie)
        self.hide_autocomplete()
    
    def get_recommendations(self):
        """Aramaya göre film önerilerini al"""
        movie_name = self.search_var.get().strip()
        if not movie_name:
            self.show_results("Lütfen bir film adı giriniz.")
            return
        
        try:
            # Film adı için en yakın eşleşmeyi bul
            find_close_match = difflib.get_close_matches(movie_name, self.movie_titles)
            if not find_close_match:
                self.show_results("Üzgünüz, bu film için öneri bulunamadı.")
                return
                
            close_match = find_close_match[0]
            
            # Filmin indeksini bul
            index_of_movie = self.movies_data[self.movies_data.title == close_match].index[0]
            
            # Benzerlik puanlarını al
            similarity_score = list(enumerate(self.similarity[index_of_movie]))
            
            # Filmleri benzerlik skoruna göre sırala
            sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
            
            # Sonuçları hazırla
            results = f"'{close_match}' filmi için öneriler:\n\n"
            for i, movie in enumerate(sorted_similar_movies[1:31], 1):  # Skip first (same movie)
                index = movie[0]
                title = self.movies_data.iloc[index]['title']
                results += f"{i}. {title}\n"
                
            self.show_results(results)
            
        except Exception as e:
            self.show_results(f"Bir hata oluştu: {str(e)}")
    
    def show_results(self, text):
        """Sonuçları metin alanında göster"""
        self.results_text.delete("1.0", END)
        self.results_text.insert("1.0", text)
    
    def clear_all(self):
        """Arama ve sonuçları temizle"""
        self.search_var.set("")
        self.show_results("")
        self.hide_autocomplete()

if __name__ == "__main__":
    app = MovieRecommendationApp()
    app.mainloop() 