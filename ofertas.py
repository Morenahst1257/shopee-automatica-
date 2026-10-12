
# Robo gratuito de ofertas Shopee
# Prepara textos para Pinterest e Facebook

ofertas = [
    {
        "produto": "Produto de exemplo",
        "preco": "R$ 29,90",
        "link": "COLE_AQUI_SEU_LINK_DE_AFILIADA"
    }
]

def preparar_publicacoes():
    for oferta in ofertas:
        texto = (
            f"✨ Confira: {oferta['produto']}\n"
            f"💰 Preço: {oferta['preco']}\n"
            f"🛍️ Veja aqui: {oferta['link']}\n"
            "#Shopee #Achadinhos #Ofertas"
        )

        print("\n--- PUBLICAÇÃO PARA PINTEREST E FACEBOOK ---")
        print(texto)

if __name__ == "__main__":
    preparar_publicacoes()
