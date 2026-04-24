"""TCKNVKN Python paketi dışa aktarımları.

Kısa açıklama: TCKN ve VKN doğrulama API'sini tek noktadan sunar.
Oluşturulma tarihi: 2026-04-24
Lisans: MIT
Web sitesi: https://www.tcknvkn.com/kutuphaneler/python
"""

from .models import ValidationResult
from .tckn import validate_multiple_tckn, validate_tckn
from .vkn import validate_multiple_vkn, validate_vkn

__all__ = [
    "ValidationResult",
    "validate_tckn",
    "validate_multiple_tckn",
    "validate_vkn",
    "validate_multiple_vkn",
]
