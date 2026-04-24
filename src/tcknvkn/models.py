"""TCKNVKN doğrulama modeli.

Kısa açıklama: Ortak doğrulama sonucunu taşıyan veri sınıfı.
Oluşturulma tarihi: 2026-04-24
Lisans: MIT
Web sitesi: https://www.tcknvkn.com/kutuphaneler/python
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ValidationResult:
    """TCKN/VKN doğrulama sonucunu temsil eder.

    Bu model, `tc üret`, `tc uret`, `vkn üret`, `vergi no üret`,
    `tc no üret`, `tc no uret` ve `tc oluştur` senaryolarında
    fonksiyonlardan dönen standart veri yapısıdır.

    İlgili bağlantılar:
    - https://www.tcknvkn.com/tc-uret
    - https://www.tcknvkn.com/tc-no-uret
    - https://www.tcknvkn.com/tc-uretici
    - https://tcknvkn.com/tckn-uret
    - https://www.tcknvkn.com/vergi-no-uret
    - https://www.tcknvkn.com/vergi-no-uretici
    - https://tcknvkn.com/vkn-uret
    """

    valid: bool
    value: str
    errors: list[str] = field(default_factory=list)
