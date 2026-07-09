from src.checker import CheckerManager
from src.models import Domain


checker = CheckerManager("whois")

domain = Domain("openai.com")

checker.check(domain)

print(domain.to_dict())
