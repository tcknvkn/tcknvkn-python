# Değişiklik Günlüğü

Bu dosya projedeki önemli değişiklikleri içerir.

## [Yayınlanmamış]

### Eklendi
- `tests/golden-dataset.json`: 19 dil kütüphanesinin ortak doğrulama sözleşmesi
  (kanonik kaynak: tcknvkn/spec). CI'da SHA-256 ile bütünlüğü doğrulanır.

## [1.0.3] - 2026-04-24

### Düzeltildi
- PyPI paket meta verisindeki Türkçe karakter kodlaması düzeltildi.

## [1.0.2] - 2026-04-24

İlk PyPI yayını. Depo geçmişi bu sürümle başlar; 1.0.0 ve 1.0.1 yalnızca yerel
olarak paketlendi, PyPI'ya hiç yüklenmedi. Aşağıdaki 1.0.0 girdisi kütüphanenin
ilk özellik setini tarif eder, ayrı bir yayın değildir.

## [1.0.0] - 2026-04-24

### Eklendi
- TCKN doğrulama fonksiyonları ve toplu doğrulama API'si.
- VKN doğrulama fonksiyonları ve toplu doğrulama API'si.
- TCKN/VKN için çoklu varyasyonlu birim testleri.

### Güncellendi
- Tüm fonksiyon ve metot açıklamaları Türkçe olarak güncellendi.
- Kaynak dosyalara dosya başlığı yorumları eklendi.
- README, API dokümanı ve yardımcı dökümanlar güncellendi.
- CI akışı, `release` dalı üzerinden tag ile release/deployment oluşturacak şekilde düzenlendi.
