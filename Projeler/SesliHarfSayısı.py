def sesli_harf_sayisi(metin):
    sesliler = "aeioöuüAEIOÖUÜ"
    sayac = 0
    for harf in metin:
        if harf in sesliler:
            sayac += 1
    return sayac
print(sesli_harf_sayisi("Python"))