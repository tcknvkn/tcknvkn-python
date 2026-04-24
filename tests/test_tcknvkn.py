"""TCKNVKN Python birim testleri.

Kısa açıklama: TCKN ve VKN doğrulama fonksiyonlarının varyasyon testleri.
Oluşturulma tarihi: 2026-04-24
Lisans: MIT
Web sitesi: https://www.tcknvkn.com/kutuphaneler/python
"""

from __future__ import annotations

import unittest

from tcknvkn import (
    validate_multiple_tckn,
    validate_multiple_vkn,
    validate_tckn,
    validate_vkn,
)


class ValidationTest(unittest.TestCase):
    """TCKN ve VKN doğrulama davranışlarını test eder."""

    def test_validate_tckn_valid(self) -> None:
        """Geçerli TCKN değerinde `valid=True` beklenir."""
        result = validate_tckn("10000000146")
        self.assertTrue(result.valid)
        self.assertEqual(result.errors, [])

    def test_validate_tckn_normalizes(self) -> None:
        """Formatlı TCKN girdisinin normalize edildiğini doğrular."""
        result = validate_tckn("100-000 00146")
        self.assertTrue(result.valid)
        self.assertEqual(result.value, "10000000146")

    def test_validate_tckn_length_error(self) -> None:
        """11 hane kuralı ihlalinde hata döndüğünü doğrular."""
        result = validate_tckn("12345")
        self.assertFalse(result.valid)
        self.assertIn("11 haneli olmalıdır.", result.errors)

    def test_validate_tckn_leading_zero_error(self) -> None:
        """İlk hane 0 olduğunda hata döndüğünü doğrular."""
        result = validate_tckn("01234567890")
        self.assertFalse(result.valid)
        self.assertIn("İlk hane 0 olamaz.", result.errors)

    def test_validate_tckn_checksum_errors(self) -> None:
        """10. ve 11. hane checksum hatalarının yakalandığını doğrular."""
        result_10 = validate_tckn("10000000156")
        result_11 = validate_tckn("10000000145")
        self.assertFalse(result_10.valid)
        self.assertFalse(result_11.valid)
        self.assertIn("10. hane kontrol hanesi hatalı.", result_10.errors)
        self.assertIn("11. hane kontrol hanesi hatalı.", result_11.errors)

    def test_validate_tckn_same_pattern_error(self) -> None:
        """Tüm haneler aynı olduğunda örüntü hatası döndüğünü doğrular."""
        result = validate_tckn("11111111111")
        self.assertFalse(result.valid)
        self.assertIn("Geçersiz örüntü: tüm haneler aynı.", result.errors)

    def test_validate_multiple_tckn_order(self) -> None:
        """Toplu TCKN doğrulamada sonuç sırasının korunduğunu doğrular."""
        results = validate_multiple_tckn(["10000000146", "10000000145", "11111111111"])
        self.assertEqual(len(results), 3)
        self.assertTrue(results[0].valid)
        self.assertFalse(results[1].valid)
        self.assertFalse(results[2].valid)

    def test_validate_multiple_tckn_empty(self) -> None:
        """Toplu TCKN doğrulamada boş liste desteğini doğrular."""
        self.assertEqual(validate_multiple_tckn([]), [])

    def test_validate_vkn_valid(self) -> None:
        """Geçerli VKN değerinde `valid=True` beklenir."""
        result = validate_vkn("1000036109")
        self.assertTrue(result.valid)
        self.assertEqual(result.errors, [])

    def test_validate_vkn_normalizes(self) -> None:
        """Formatlı VKN girdisinin normalize edildiğini doğrular."""
        result = validate_vkn("100-003-6109")
        self.assertTrue(result.valid)
        self.assertEqual(result.value, "1000036109")

    def test_validate_vkn_length_error(self) -> None:
        """10 hane kuralı ihlalinde hata döndüğünü doğrular."""
        result = validate_vkn("1234")
        self.assertFalse(result.valid)
        self.assertIn("10 haneli olmalıdır.", result.errors)

    def test_validate_vkn_checksum_error(self) -> None:
        """VKN checksum hatasının yakalandığını doğrular."""
        result = validate_vkn("1000036108")
        self.assertFalse(result.valid)
        self.assertIn("Son hane kontrol hanesi hatalı.", result.errors)

    def test_validate_vkn_same_pattern_error(self) -> None:
        """Tüm haneler aynı olduğunda VKN örüntü hatasını doğrular."""
        result = validate_vkn("1111111111")
        self.assertFalse(result.valid)
        self.assertIn("Geçersiz örüntü: tüm haneler aynı.", result.errors)

    def test_validate_multiple_vkn_order(self) -> None:
        """Toplu VKN doğrulamada sonuç sırasının korunduğunu doğrular."""
        results = validate_multiple_vkn(["1000036109", "1000036108", "1111111111"])
        self.assertEqual(len(results), 3)
        self.assertTrue(results[0].valid)
        self.assertFalse(results[1].valid)
        self.assertFalse(results[2].valid)

    def test_validate_multiple_vkn_empty(self) -> None:
        """Toplu VKN doğrulamada boş liste desteğini doğrular."""
        self.assertEqual(validate_multiple_vkn([]), [])

    def test_validate_multiple_lists_with_formatted_values(self) -> None:
        """Formatlı TCKN/VKN listelerinde normalize ve sıra korumasını doğrular."""
        tckn_results = validate_multiple_tckn(["100-000 00146", "123"])
        vkn_results = validate_multiple_vkn(["100-003-6109", "123"])
        self.assertTrue(tckn_results[0].valid)
        self.assertFalse(tckn_results[1].valid)
        self.assertTrue(vkn_results[0].valid)
        self.assertFalse(vkn_results[1].valid)


if __name__ == "__main__":
    unittest.main()
