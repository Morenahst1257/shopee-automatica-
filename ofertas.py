
# Robô de ofertas para afiliados Shopee

def criar_oferta(nome, preco, link_afiliado):
    oferta = f"""
🔥 ACHADINHO SHOPEE 🔥

🛍️ Produto: {nome}
💰 Preço: R$ {preco}

🛒 Confira aqui:
{link_afiliado}

#Shopee #Achadinhos #Ofertas
"""
    return oferta.strip()


if __name__ == "__main__":
    print("Robô de ofertas iniciado!")
    print("Configure os produtos e links para gerar suas ofertas.")
