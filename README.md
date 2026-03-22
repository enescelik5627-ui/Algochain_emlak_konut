# AI Destekli Manyetik Sensör Tabanlı Akıllı Bina Enerji ve Altyapı Analitiği

## 📌 Proje Tanımı

Bu proje, binalardaki elektriksel ve mekanik sistemlerin davranışını **temassız manyetik sensörler** ile ölçerek, elde edilen veriyi **yapay zekâ ile analiz eden** ve anlamlı metriklere dönüştüren bir akıllı bina analitik platformudur.

Amaç:

- Binaları veri üreten sistemlere dönüştürmek  
- Enerji tüketimini optimize etmek  
- Arıza risklerini önceden tespit etmek  
- Sürdürülebilirlik ve ESG skorları üretmek  

---
---

## 🔍 Sistem Donanım Görselleri

Bu projede geliştirilen cihazın PCB tasarımı, devre şeması ve donanım mimarisi aşağıda sunulmaktadır.

---

## 🧩 PCB Tasarımı

<p align="center">
  <img src="b.png" width="700">
</p>

---

## ⚙️ PCB Yerleşim (Routing)

<p align="center">
  <img src="d.png" width="700">
</p>

---

## 🔬 Devre Şeması

<p align="center">
  <img src="c.png" width="900">
</p>

---

## 🧠 Donanım Modeli (3D)

<p align="center">
  <img src="a.png" width="600">
</p>

## 🚨 Problem Tanımı

Günümüzde büyük konut projelerinde:

- Enerji tüketimi kontrol edilemez  
- Sistemler gerçek zamanlı izlenmez  
- Arızalar geç fark edilir  
- Enerji kayıpları tespit edilemez  

Özellikle:

- HVAC (klima sistemleri)  
- pompalar  
- asansör motorları  

gibi sistemler sürekli çalışmasına rağmen **veri üretmez**.

---



## 💡 Çözüm

Bu sistem, elektrik akımının oluşturduğu **manyetik alanı temassız olarak ölçerek**:

- enerji tüketimini hesaplar  
- cihaz davranışını analiz eder  
- sistem sağlığını değerlendirir  

ve bu verileri **AI ile anlamlandırır**.

---

## ⚙️ Sistem Mimarisi

```text
[Manyetik Sensörler]
        ↓
[Analog Front-End Devre]
        ↓
[ADC (Analog → Dijital)]
        ↓
[Mikrodenetleyici (ESP32)]
        ↓
[Veri İletimi (WiFi / LoRa / Bluetooth)]
        ↓
[AI Analiz + Dashboard]
