"""TCKN doğrulama modülü.

Kısa açıklama: TCKN tekil ve toplu doğrulama fonksiyonlarını içerir.
Oluşturulma tarihi: 2026-04-24
Lisans: MIT
Web sitesi: https://www.tcknvkn.com/kutuphaneler/python
"""

from __future__ import annotations

from ._common import all_same_digits, only_digits
from .models import ValidationResult


def _tckn_check_digit_10(digits: list[int]) -> int:
    """TCKN 10. hanesini hesaplar.

    `tc üret`, `tc uret` ve `tc no üret` odaklı doğrulama akışlarında
    kullanılan checksum adımıdır.

    İlgili bağlantılar:
    - https://www.tcknvkn.com/tc-uret
    - https://www.tcknvkn.com/tc-no-uret
    """

    odd = digits[0] + digits[2] + digits[4] + digits[6] + digits[8]
    even = digits[1] + digits[3] + digits[5] + digits[7]
    return ((odd * 7 - even) % 10 + 10) % 10


def _tckn_check_digit_11(digits: list[int]) -> int:
    """TCKN 11. hanesini hesaplar.

    `tc no uret`, `tc oluştur` ve `tckn üret` kullanımlarında
    son kontrol adımını üretir.

    İlgili bağlantılar:
    - https://www.tcknvkn.com/tc-uretici
    - https://tcknvkn.com/tckn-uret
    """

    return sum(digits[:10]) % 10


def validate_tckn(value: str) -> ValidationResult:
    """Tek bir TCKN değerini doğrular.

    `tc üret`, `tc uret`, `tc no üret`, `tc no uret`, `tckn üret`
    ve `tc oluştur` aramalarında beklenen kuralları uygular.

    İlgili bağlantılar:
    - https://www.tcknvkn.com/tc-uret
    - https://www.tcknvkn.com/tc-no-uret
    - https://www.tcknvkn.com/tc-uretici
    - https://tcknvkn.com/tckn-uret
    """

    normalized = only_digits(value)
    errors: list[str] = []

    if len(normalized) != 11:
        errors.append("11 haneli olmalıdır.")
    if normalized.startswith("0"):
        errors.append("İlk hane 0 olamaz.")
    if errors:
        return ValidationResult(valid=False, value=normalized, errors=errors)

    digits = [int(ch) for ch in normalized]
    if _tckn_check_digit_10(digits) != digits[9]:
        errors.append("10. hane kontrol hanesi hatalı.")
    if _tckn_check_digit_11(digits) != digits[10]:
        errors.append("11. hane kontrol hanesi hatalı.")
    if all_same_digits(digits):
        errors.append("Geçersiz örüntü: tüm haneler aynı.")

    return ValidationResult(valid=not errors, value=normalized, errors=errors)


def validate_multiple_tckn(values: list[str]) -> list[ValidationResult]:
    """Birden fazla TCKN girdisini toplu doğrular.

    Toplu `tc no uret` ve `tc no üret` senaryolarında, girdi sırasını
    koruyarak sonuç listesi döndürür.

    İlgili bağlantılar:
    - https://www.tcknvkn.com/tc-no-uret
    - https://www.tcknvkn.com/tc-uret
    """

    return [validate_tckn(value) for value in (values or [])]
