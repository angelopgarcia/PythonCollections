class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)


conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)
print(conta_do_gui)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
print(conta_da_dani)

contas = [conta_do_gui, conta_da_dani]
for conta in contas:
    print(conta)

contas = [conta_do_gui, conta_da_dani, conta_do_gui]
print(contas[0])

conta_do_gui.deposita(100)
print(contas[0])

print(contas[2])

contas[2].deposita(300)
print(conta_do_gui)

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

contas = [conta_do_gui, conta_da_dani]
print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])

contas.insert(0, 76)
print(contas[0], contas[1], contas[2])

('Guilherme', 37, 1981) # tupla
('Daniela', 31, 1987)
#paulo = (39, 'Paulo, 1979) # ruim

conta_do_gui = (15, 1000)
# conta_do_gui.deposita() # variação OO
conta_do_gui[1]

def deposita(conta): # variação funcional
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)

usuarios = [guilherme, daniela]
usuarios

usuarios.append(('Paulo', 39, 1979))
usuarios