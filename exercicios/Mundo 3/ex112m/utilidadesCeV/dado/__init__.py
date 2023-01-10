def leiaDinheiro(perg):
    while True:
        resp = input(perg)
        if ',' in resp:
            resp = resp.replace(',', '.')
        try:
            float(resp)
            return float(resp)
        except ValueError:
            print(f'\033[1;31mERRO! "{resp}" é um preço inválido.\033[m')