import alertpix


token = "Bearer cb22b3ccb34d5ebc4e2ee25c32d2d015"
client = alertpix.Alertpix(token)

pagamento = client.Charge(link="apenasumnerdd", amount=1000, comment="Pagando aquele cafézinho", username="Remetente")
pagamento.create()

print("BrCode para o pagamento: ", pagamento.brcode.code)
print("Aguardando pagamento...")
while True:
    if pagamento.paid == True:
        print("Pagamento concluído!")