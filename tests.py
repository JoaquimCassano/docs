import alertpix

pagamento = alertpix.Charge(link="apenasumnerdd", amount=1000, comment="Pagando aquele cafézinho", username="Remetente")
pagamento.create()

print("BrCode para o pagamento: ", pagamento.brcode.code)
print("Aguardando pagamento...")
while True:
    if pagamento.check() == True:
        print("Pagamento concluído!")
        break