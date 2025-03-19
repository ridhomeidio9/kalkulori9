import streamlit as st

st.title("KALKULORI")
st.write(
    "untuk menghitung kebutuhan kalori harian"
)
import streamlit as st

def hitung_kalori(jenis_kelamin, berat, tinggi, usia, aktivitas):
    if jenis_kelamin == "Laki-laki":
        bmr = 88.36 + (13.4 * berat) + (4.8 * tinggi) - (5.7 * usia)
    else:
        bmr = 447.6 + (9.2 * berat) + (3.1 * tinggi) - (4.3 * usia)
    
    faktor_aktivitas = {
        "Sedentary (Jarang olahraga)": 1.2,  # Tidak berolahraga atau sangat jarang bergerak
        "Lightly active (Olahraga ringan 1-3 hari/minggu)": 1.375,  # Olahraga ringan seperti berjalan atau yoga beberapa kali seminggu
        "Moderately active (Olahraga sedang 3-5 hari/minggu)": 1.55,  # Olahraga sedang seperti jogging atau bersepeda secara rutin
        "Very active (Olahraga berat 6-7 hari/minggu)": 1.725,  # Olahraga intens hampir setiap hari
        "Super active (Atlet atau pekerjaan fisik berat)": 1.9  # Atlet profesional atau pekerja dengan aktivitas fisik sangat tinggi
    }
    
    kalori_harian = bmr * faktor_aktivitas[aktivitas]
    return kalori_harian

def main():
    st.title("Kalkulator Kalori Harian")
    
    jenis_kelamin = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
    berat = st.number_input("Berat Badan (kg)", min_value=1.0, step=0.1)
    tinggi = st.number_input("Tinggi Badan (cm)", min_value=50.0, step=0.1)
    usia = st.number_input("Usia (tahun)", min_value=1, step=1)
    
    aktivitas = st.selectbox("Tingkat Aktivitas", [
        "Sedentary (Jarang olahraga)",
        "Lightly active (Olahraga ringan 1-3 hari/minggu)",
        "Moderately active (Olahraga sedang 3-5 hari/minggu)",
        "Very active (Olahraga berat 6-7 hari/minggu)",
        "Super active (Atlet atau pekerjaan fisik berat)"
    ])
    
    if st.button("Hitung Kalori"):
        kalori = hitung_kalori(jenis_kelamin, berat, tinggi, usia, aktivitas)
        st.success(f"Kebutuhan kalori harian Anda adalah {kalori:.2f} kkal")
        
        st.info("\nTips: \n- Jika ingin menurunkan berat badan, konsumsi lebih sedikit kalori dari kebutuhan harian.\n- Jika ingin menambah berat badan, konsumsi lebih banyak kalori dari kebutuhan harian.\n- Pastikan pola makan seimbang dengan nutrisi yang cukup!")

if __name__ == "__main__":
    main()


