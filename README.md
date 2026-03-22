# 🧠 Blockchain Destekli Akıllı Giriş ve Doğrulama Ekosistemi

## 📌 Proje Tanımı

Bu proje, geleneksel merkezi güvenlik sistemlerindeki insan hatasını ve veri manipülasyonu risklerini ortadan kaldırmak amacıyla geliştirilmiş, **blockchain tabanlı bir akıllı giriş ve doğrulama platformudur**.

Sistem, güvenlik süreçlerini insan yorumuna değil, **değiştirilemez matematiksel kanıtlara** ve kriptografik kayıtlara dayandırarak yönetir.

### 🎯 Amaç

* Güvenliği merkezi otoritelerden alıp dağıtık bir güven ağına taşımak
* Giriş-çıkış süreçlerini otomatikleştirerek operasyonel verimliliği artırmak
* Veri manipülasyonu ve kayıt silme risklerini matematiksel olarak imkansız hale getirmek
* Site sakinlerine modern ve prestijli bir yaşam standardı sunmak

---

## 🔍 Sistem Donanım Görselleri

Sistemin kalbinde yer alan, kriptografik doğrulama yapan IoT kontrol ünitesinin tasarım detayları aşağıdadır:

### 🧩 PCB Tasarımı

<p align="center">
  <img src="images/b.png" width="700">
</p>

---

### ⚙️ PCB Yerleşim (Routing)

<p align="center">
  <img src="images/d.png" width="700">
</p>

---

### 🔬 Devre Şeması

<p align="center">
  <img src="images/c.png" width="900">
</p>

---

### 🧠 Donanım Modeli (3D)

<p align="center">
  <img src="images/a.png" width="600">
</p>

---

## 🚨 Problem Tanımı

Günümüz site yaşamındaki geleneksel güvenlik yöntemleri ciddi zafiyetler barındırmaktadır:

* **İnsan Faktörü:** Unutkanlık, yetki aşımı ve sahte kimliklerin tespit edilememesi
* **Merkezi Veritabanı Riskleri:** Siber saldırılarda tek nokta çökmesi (Single Point of Failure) ve veri manipülasyonu
* **Operasyonel Karmaşa:** Uzayan bekleme süreleri, manuel misafir kayıtları ve yüksek maliyet

---

## 💡 Çözüm

Bu sistem, güvenliği "zayıf halka" olan insan ve merkezi sunuculardan kurtararak **blockchain mimarisine** emanet eder.

* **Dinamik QR Doğrulama:** Kullanıcılar mobil uygulama üzerinden süreli QR kod üretir
* **Immutable Ledger:** Tüm girişler değiştirilemez şekilde blockchain’e kaydedilir
* **Otonom Onay:** Smart contract ile otomatik doğrulama

---

## ⚙️ Sistem Mimarisi

```text
[Mobil Uygulama (Dinamik QR)]
        ↓
[IoT Geçiş Terminali (QR Okuyucu)]
        ↓
[Blockchain Doğrulama (Smart Contract)]
        ↓
[Merkeziyetsiz Kayıt (Immutable Hash)]
        ↓
[Kapı / Bariyer Kontrol (ESP32 / Röle)]
        ↓
[AI Destekli Yönetici Paneli (Analitik)]
```

---

## 📊 Yönetici Paneli ve Analitik

* **Gerçek Zamanlı Yoğunluk:** Anlık giriş-çıkış takibi
* **Genel Risk Puanı:** Şüpheli aktivitelerin analizi
* **Davranış Analitiği:** Tekrar eden veya anormal giriş denemeleri

---

## 🚀 Gelecek Geliştirmeler

* Mobil uygulama entegrasyonu (iOS / Android)
* NFT tabanlı giriş kimlikleri
* Yüz tanıma destekli doğrulama
* Bulut + edge hibrit mimari

---

## 🛠️ Kullanılan Teknolojiler

* ESP32
* QR Code Scanner
* Blockchain (Ethereum / Solidity)
* IoT Sistemleri
* PCB Tasarım (KiCad / Altium)

---

## 📄 Lisans

MIT License
