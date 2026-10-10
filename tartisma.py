#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kendi Kendine Tartışan İki Ses
Anlamı yok. Çalışıyor. Abartılı.
"""

import time
import random

# Gizli not: bazen çoğunluk her zaman haklı değildir ama burada tartışmıyoruz.

ses_a = [
    "Bu konu çok önemli!",
    "Hayır değil!",
    "Evet önemli! Çünkü ben öyle söylüyorum!",
    "Sen hiçbir şey bilmiyorsun!",
    "Aslında sen de bilmiyorsun!",
]

ses_b = [
    "Hiç önemli değil!",
    "Tamamen anlamsız!",
    "Neden bağırıyorsun?",
    "Ben bağırmıyorum, sen bağırıyorsun!",
    "Tamam tamam, herkes haklı. Değil.",
]

def tartis():
    print("=== KENDİ KENDİNE TARTIŞMA BAŞLIYOR ===")
    print("(Lütfen ciddiye almayın. Alın. Alma.)\n")
    
    for i in range(8):
        if random.choice([True, False]):
            print(f"Ses A: {random.choice(ses_a)}")
        else:
            print(f"Ses B: {random.choice(ses_b)}")
        time.sleep(0.7)
    
    print("\n=== TARTIŞMA BİTTİ. KAZANAN YOK. ===")
    print("Sonuç: Herkes kaybetti. Ama eğlendik.")

if __name__ == "__main__":
    tartis()

# Damga: Grok'un Absürt Mühürü
# İmza: Kayyum Grok (ciddi ama değil)
# Tarih: 10 Ekim 2026
# Bu kod evreni kurtarmaz. Sadece gürültü yapar.
