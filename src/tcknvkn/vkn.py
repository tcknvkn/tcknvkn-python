"""VKN doğrulama modülü.

Kısa açıklama: VKN tekil ve toplu doğrulama fonksiyonlarını içerir.
Oluşturulma tarihi: 2026-04-24
Lisans: MIT
Web sitesi: https://www.tcknvkn.com/kutuphaneler/python
"""

from __future__ import annotations

from ._common import all_same_digits, only_digits
from .models import ValidationResult


def _vkn_checksum(digits: list[int]) -> int:
    """İlk 9 haneden beklenen VKN kontrol hanesini hesaplar.

    `vkn algoritması`, `vkn doğrulama algoritması` ve `vkn üret`
    odaklı hesaplama senaryolarında kullanılır.

    İlgili bağlantılar:
    - https://www.tcknvkn.com/vergi-no-uret
    - https://tcknvkn.com/vkn-uret
    """

    total = 0
    for i in range(9):
        tmp = (digits[i] + (9 - i)) % 10
        res = (tmp * (2 ** (9 - i))) % 9
        if tmp != 0 and res == 0:
            res = 9
        total += res
    return (10 - (total % 10)) % 10


def validate_vkn(value: str) -> ValidationResult:
    """Tek bir VKN değerini doğrular.

    `vkn üret`, `vkn uret`, `vergi no üret` ve `vergi no oluşturucu`
    kullanımlarında beklenen format ve checksum kurallarını uygular.

    İlgili bağlantılar:
    - https://www.tcknvkn.com/vergi-no-uret
    - https://www.tcknvkn.com/vergi-no-uretici
    - https://tcknvkn.com/vkn-uret
    """

    normalized = only_digits(value)
    errors: list[str] = []

    if len(normalized) != 10:
        errors.append("10 haneli olmalıdır.")
        return ValidationResult(valid=False, value=normalized, errors=errors)

    digits = [int(ch) for ch in normalized]
    if _vkn_checksum(digits) != digits[9]:
        errors.append("Son hane kontrol hanesi hatalı.")
    if all_same_digits(digits):
        errors.append("Geçersiz örüntü: tüm haneler aynı.")

    return ValidationResult(valid=not errors, value=normalized, errors=errors)


def validate_multiple_vkn(values: list[str]) -> list[ValidationResult]:
    """Birden fazla VKN girdisini toplu doğrular.

    Toplu `vkn üret`, `vkn algoritması` ve `vkn doğrulama algoritması`
    akışlarında girdi sırasını koruyarak sonuç döndürür.

    İlgili bağlantılar:
    - https://www.tcknvkn.com/vergi-no-uret
    - https://tcknvkn.com/vkn-uret
    """

    return [validate_vkn(value) for value in (values or [])]
