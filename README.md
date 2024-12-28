# Proyek Analisis Data: bike-sharing-dataset

**Nama:** Rizki Romdhoni  

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda pada sistem berbagi sepeda. Analisis dilakukan untuk menjawab beberapa pertanyaan bisnis, seperti:
- Bagaimana cuaca memengaruhi jumlah penyewaan sepeda?
- Berapa persen peningkatan penyewaan sepeda pada akhir pekan dibandingkan hari kerja?
- Bisakah kita mengidentifikasi jam-jam puncak penyewaan sepeda setiap hari?
- Bagaimana tren penyewaan sepeda berubah dari tahun 2011 ke 2012?

## Data
Dataset yang digunakan dalam proyek ini terdiri dari dua bagian:
- `day.csv`: Data penyewaan sepeda harian, termasuk total penyewaan, kondisi cuaca, dan hari libur.
- `hour.csv`: Data penyewaan sepeda per jam.

## Library yang Digunakan
- pandas
- numpy
- matplotlib
- seaborn
- datetime

## Cara Menjalankan Proyek di Lokal
1. Clone repositori ini:
   ```bash
   git clone https://github.com/RizkiRdm/bike-sharing-analytict.git
   cd bike-sharing-analytict
   ```

2. Buat dan aktifkan virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # Untuk pengguna Windows: env\Scripts\activate
   ```

3. Instal semua dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

5. Buka file `Proyek_Analisis_Data.ipynb` dan jalankan setiap sel untuk melihat hasil analisis.

---

Feel free to edit and adjust as needed.
