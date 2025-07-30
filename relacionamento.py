class Pessoa:
    def _init_(self, nome): #INIT: INICIALIZAR OBJETO
        self.nome = nome
        self.parceiro = []

    def adicionar_parceiro(self, relacionamento):
        self.parceiro.append(relacionamento)

    def mostrar_parceiro(self):
        if not self.parceiro:
            print(f"{self.nome} não possui parceiros registrados.")

        else:
            print(f"parceiros amorosos de {self.nome}:")
            for rel in self.parceiro:
                if rel.pessoa1 == self:
                    parceiro = rel.pessoa2
                else:
                    parceiro = rel.pessoal2
                print(f" - {parceiro.nome}, desde {rel.ano_inicio}")
            
            

class Relacionamento:
    def _init_(self, pessoa1, pessoa2, ano_inicio): #self: relacionamento ao objetoque esta sendo criado/manipulado
        self.pessoa1 = pessoa1
        self.pessoa2 = pessoa2
        self.ano_inicio = ano_inicio
        
    def mostrar_informaçao(self):
        print(f"{self.pessoa1.nome} e {self.pessoa2.nome} estão juntos desde {self.ano_inicio}")



#criando pessoas

ana = Pessoa("Ana")
brino = Pessoa ("brino")
felca = Pessoa("Felca")
menina_veneno = Pessoa("menina veneno")
chico_moedas = Pessoa("chico moedas")
luisa = Pessoa("luisa")
igona = Pessoa("igona")
davi_brito = Pessoa("davi brito")

#criando relacionamentos
 
relacionamento1 = Relacionamento(ana,davi_brito , 2015)
relacionamento2 = Relacionamento(igona,chico_moedas , 2024)
relacionamento3 = Relacionamento(brino, felca , 2021)
relacionamento4 = Relacionamento(menina_veneno,luisa, 2023)
relacionamento5 = Relacionamento(chico_moedas,davi_brito, 2022)

ana.adicionar_parceiro(relacionamento1)
davi_brito.adicionar_parceiro(relacionamento1)


igona.adicionar_parceiro(relacionamento2)
chico_moedas.adicionar_parceiro(relacionamento2)

brino.adicionar_parceiro(relacionamento3)
felca.adicionar_parceiro(relacionamento3) 

menina_veneno.adicionar_parceiro(relacionamento4)
luisa.adicionar_parceiro(relacionamento4) 

chico_moedas.adicionar_parceiro(relacionamento5)
davi_brito.adicionar_parceiro(relacionamento5) 
 
 #exibir 
ana.mostrar_parceiro()