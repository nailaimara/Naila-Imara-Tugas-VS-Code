# Import library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Pengumpulan Data
# Membaca data dari file CSV
data = pd.read_csv('data_penjualan.csv')
print("Data Awal:")
print(data)

# Step 2: Data Cleaning
# Memeriksa nilai yang hilang
print("\nMengecek nilai yang hilang:")
print(data.isnull().sum())

# Step 3: Data Transformation
# Mengubah kolom 'Tanggal' menjadi tipe datetime
data['Tanggal'] = pd.to_datetime(data['Tanggal'])

# Menambah kolom 'Bulan' dan 'Tahun'
data['Bulan'] = data['Tanggal'].dt.month
data['Tahun'] = data['Tanggal'].dt.year

# Menampilkan data setelah transformasi
print("\nData Setelah Transformasi:")
print(data)

# Step 4: Exploratory Data Analysis (EDA)
# Statistik Deskriptif
print("\nStatistik Deskriptif:")
print(data.describe())

# Visualisasi pendapatan per produk
plt.figure(figsize=(10, 6))
sns.barplot(x='Produk', y='Pendapatan', data=data, estimator=sum)
plt.title('Total Pendapatan per Produk')
plt.show()

# Visualisasi pendapatan per bulan
plt.figure(figsize=(10, 6))
sns.lineplot(x='Tanggal', y='Pendapatan', data=data, marker='o')
plt.title('Pendapatan Harian')
plt.show()

# Visualisasi distribusi kuantitas
plt.figure(figsize=(10, 6))
sns.histplot(data['Kuantitas'], bins=10, kde=True)
plt.title('Distribusi Kuantitas')
plt.show()
