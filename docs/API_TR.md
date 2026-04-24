# tcknvkn Python API Dokümantasyonu

Bu doküman, `tcknvkn` paketindeki TCKN ve VKN doğrulama fonksiyonlarını özetler.

## Kurulum

```bash
pip install tcknvkn
```

## Dışa açık API

```python
from tcknvkn import (
    ValidationResult,
    validate_tckn,
    validate_multiple_tckn,
    validate_vkn,
    validate_multiple_vkn,
)
```

## Fonksiyonlar

### `validate_tckn(value: str) -> ValidationResult`

Tek bir TCKN değerini doğrular.

- Rakam dışı karakterleri temizler.
- 11 hane uzunluk kuralını kontrol eder.
- İlk hane ve kontrol basamağı kurallarını doğrular.

### `validate_multiple_tckn(values: list[str]) -> list[ValidationResult]`

TCKN listesi alır ve her değer için doğrulama sonucu döndürür.

### `validate_vkn(value: str) -> ValidationResult`

Tek bir VKN değerini doğrular.

- Rakam dışı karakterleri temizler.
- 10 hane uzunluk kuralını kontrol eder.
- VKN checksum algoritması ile son haneyi doğrular.

### `validate_multiple_vkn(values: list[str]) -> list[ValidationResult]`

VKN listesi alır ve her değer için doğrulama sonucu döndürür.

## ValidationResult

```python
@dataclass(frozen=True)
class ValidationResult:
    valid: bool
    value: str
    errors: list[str]
```

- `valid`: Sonuç geçerliyse `True`
- `value`: Temizlenmiş ve normalize edilmiş değer
- `errors`: Doğrulama hata listesi

## Örnek

```python
from tcknvkn import validate_tckn, validate_vkn

print(validate_tckn("10000000146").valid)
print(validate_vkn("1000036109").valid)
```

## İlgili bağlantılar

- https://www.tcknvkn.com/tc-uret
- https://www.tcknvkn.com/tc-no-uret
- https://www.tcknvkn.com/tc-uretici
- https://tcknvkn.com/tckn-uret
- https://www.tcknvkn.com/vergi-no-uret
- https://www.tcknvkn.com/vergi-no-uretici
- https://tcknvkn.com/vkn-uret
