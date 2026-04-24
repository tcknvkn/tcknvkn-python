# tcknvkn (Python)

`tcknvkn`, Türkiye Cumhuriyeti Kimlik Numarası (TCKN) ve Vergi Kimlik Numarası (VKN) doğrulaması için geliştirilmiş hafif bir Python kütüphanesidir.

Bu paket yalnızca algoritmik/format doğrulaması yapar; resmi kurum sorgusu yapmaz.

## Kurulum

```bash
pip install tcknvkn
```

## Hızlı başlangıç

```python
from tcknvkn import (
    validate_tckn,
    validate_multiple_tckn,
    validate_vkn,
    validate_multiple_vkn,
)

tekil_tckn = validate_tckn("10000000146")
print(tekil_tckn.valid)   # True
print(tekil_tckn.errors)  # []

tekil_vkn = validate_vkn("1000036109")
print(tekil_vkn.valid)    # True

sonuclar = validate_multiple_tckn(["10000000146", "10000000145", "11111111111"])
for sonuc in sonuclar:
    print(sonuc.value, sonuc.valid, sonuc.errors)
```

## API özeti

- `validate_tckn(value: str) -> ValidationResult`
- `validate_multiple_tckn(values: list[str]) -> list[ValidationResult]`
- `validate_vkn(value: str) -> ValidationResult`
- `validate_multiple_vkn(values: list[str]) -> list[ValidationResult]`

## ValidationResult

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class ValidationResult:
    valid: bool
    value: str
    errors: list[str]
```

## Test çalıştırma

```bash
python -m unittest discover -s tests
```

## İlgili bağlantılar

- Kütüphaneler merkezi: https://www.tcknvkn.com/kutuphaneler
- Python kütüphane sayfası: https://www.tcknvkn.com/kutuphaneler/python
- https://www.tcknvkn.com/tc-uret
- https://www.tcknvkn.com/tc-no-uret
- https://www.tcknvkn.com/tc-uretici
- https://tcknvkn.com/tckn-uret
- https://www.tcknvkn.com/vergi-no-uret
- https://www.tcknvkn.com/vergi-no-uretici
- https://tcknvkn.com/vkn-uret

## Lisans

MIT
