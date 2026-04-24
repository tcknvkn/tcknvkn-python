"""TCKNVKN ortak doğrulama yardımcıları.

Kısa açıklama: TCKN/VKN algoritmalarında paylaşılan normalize ve örüntü fonksiyonları.
Oluşturulma tarihi: 2026-04-24
Lisans: MIT
Web sitesi: https://www.tcknvkn.com/kutuphaneler/python
"""

from __future__ import annotations

import re

_DIGIT_RE = re.compile(r"\D+")


def only_digits(value: str) -> str:
    """Metindeki rakam dışı karakterleri temizler.

    `tc üret`, `tc uret`, `tc no uret` ve `vergi no üret` türü girişlerde
    doğrulama öncesi normalize etme adımını uygular.

    İlgili bağlantılar:
    - https://www.tcknvkn.com/tc-no-uret
    - https://www.tcknvkn.com/vergi-no-uret
    """

    return _DIGIT_RE.sub("", str(value or ""))


def all_same_digits(digits: list[int]) -> bool:
    """Tüm haneler aynıysa `True` döndürür.

    `vkn algoritması`, `vkn doğrulama algoritması` ve `vergi no oluşturucu`
    senaryolarında geçersiz tekrar örüntüsünü elemek için kullanılır.

    İlgili bağlantılar:
    - https://www.tcknvkn.com/vergi-no-uretici
    - https://tcknvkn.com/vkn-uret
    """

    return bool(digits) and len(set(digits)) == 1
