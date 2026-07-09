from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass(slots=True)
class DomainCheckResult:
    """
    Ortak checker sonucu.

    Bütün checker'lar (WHOIS, RDAP, DNS, vb.) bu modeli döndürmelidir.
    """

    # Kontrol edilen domain
    domain: str

    # Boş mu?
    available: bool

    # Sonucu üreten checker
    checker: str

    # HTTP / WHOIS dönüş süresi
    response_time: float = 0.0

    # Hata oluştuysa
    error: Optional[str] = None

    # İsteğe bağlı HTTP kodu
    status_code: Optional[int] = None

    # Ham cevap (debug amaçlı)
    raw_response: Any = None

    # Ek bilgiler
    metadata: Dict[str, Any] = field(default_factory=dict)

    @property
    def success(self) -> bool:
        """
        Kontrol başarıyla tamamlandı mı?
        """
        return self.error is None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "domain": self.domain,
            "available": self.available,
            "checker": self.checker,
            "response_time": self.response_time,
            "error": self.error,
            "status_code": self.status_code,
            "metadata": self.metadata,
        }