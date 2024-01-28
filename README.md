# Sentyment Analyzer z Load Balancerem
## Wprowadzenie
Program Sentyment Analyzer z Load Balancerem to aplikacja umożliwiająca analizę sentymentu tekstu za pomocą endpointu POST. Program składa się z dwóch głównych części: Sentyment Analyzera oraz Load Balancera. Sentyment Analyzer zajmuje się właściwą analizą sentymentu tekstu, podczas gdy Load Balancer zarządza równoważeniem obciążenia pomiędzy wieloma instancjami Sentyment Analyzera, co umożliwia efektywne przetwarzanie dużej liczby żądań.

## Wymagania
Aby uruchomić program, wymagane jest zainstalowanie następujących bibliotek Pythona:

Flask: ```pip install Flask```

## Uruchamianie
### Uruchomienie Load Balancera:

```bash
python LoadBalancer.py
```

### Uruchomienie instancji Sentyment Analyzera:
```bash
python app5001.py --cgi
```
## Użycie
Po uruchomieniu Load Balancera i jednej lub więcej instancji Sentyment Analyzera, aplikacja będzie gotowa do przyjmowania żądań POST na endpointcie głównym. Należy przesłać tekst w formie JSON-a:
```json
{
  "text": "Tekst do analizy sentymentu."
}
```
Odpowiedź będzie zawierała wynik analizy sentymentu:
```json
{
  "sentiment": "0.8"
}
```
## Konfiguracja
Konfiguracja Load Balancera znajduje się w pliku load_balancer_config.json, gdzie można dostosować parametry takie jak liczba instancji Sentyment Analyzera, strategia równoważenia obciążenia, czy porty.

Zgłaszanie problemów
W przypadku problemów związanych z programem, prosimy o nie zgłasznaie ich.

Dziękujemy za skorzystanie z naszej aplikacji!
