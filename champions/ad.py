champions = [
"https://opgg-static.akamaized.net/meta/images/lol/spell/GarenE.png?image=q_auto,f_png,w_64&v=1670226786967",
        "https://opgg-static.akamaized.net/meta/images/lol/spell/GarenQ.png?image=q_auto,f_png,w_64&v=1670226786967",
        "https://opgg-static.akamaized.net/meta/images/lol/spell/GarenW.png?image=q_auto,f_png,w_64&v=1670226786967"
    ]
lit = []
for champion in champions:
    lit.append(champion.split('""'))
    print(lit)
