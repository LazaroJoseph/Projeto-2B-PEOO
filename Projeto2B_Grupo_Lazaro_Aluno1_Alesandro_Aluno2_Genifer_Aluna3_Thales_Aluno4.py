class Animal:
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y):
        self.nome = nome
        self.cor = cor
        self.sexo = sexo
        self.velocidade = velocidade
        self.peso = peso
        self.estamina = estamina
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y

    def imprimir_caracteristicas(self):
        print("Nome:", self.nome)
        print("Cor:", self.cor)
        print("Sexo:", self.sexo)
        print("Velocidade:", self.velocidade)
        print("Peso:", self.peso)
        print("Estamina:", self.estamina)
        print("Posição X:", self.posicao_x)
        print("Posição Y:", self.posicao_y)

    def get_nome(self):
        return self.nome

    def get_cor(self):
        return self.cor

    def get_sexo(self):
        return self.sexo

    def get_velocidade(self):
        return self.velocidade

    def get_peso(self):
        return self.peso

    def get_estamina(self):
        return self.estamina

    def get_posicao_x(self):
        return self.posicao_x

    def get_posicao_y(self):
        return self.posicao_y

    def set_nome(self, nome):
        self.nome = nome

    def set_cor(self, cor):
        self.cor = cor

    def set_sexo(self, sexo):
        self.sexo = sexo

    def set_velocidade(self, velocidade):
        self.velocidade = velocidade

    def set_peso(self, peso):
        self.peso = peso

    def set_estamina(self, estamina):
        self.estamina = estamina

    def set_posicao_x(self, posicao_x):
        self.posicao_x = posicao_x

    def set_posicao_y(self, posicao_y):
        self.posicao_y = posicao_y


class Leao(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y, idade):
        super().__init__(nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y)
        self.idade = idade

    def rugir(self):
        print(f"O {self.nome} está rugindo!")

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade = idade


class Cachorro(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y, raca, idade):
        super().__init__(nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y)
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"O {self.nome} está latindo!")

    def get_raca(self):
        return self.raca

    def get_idade(self):
        return self.idade

    def set_raca(self, raca):
        self.raca = raca

    def set_idade(self, idade):
        self.idade = idade


class Gato(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y, raca):
        super().__init__(nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y)
        self.raca = raca

    def miar(self):
        print(f"O {self.nome} está miando!")


    def get_raca(self):
        return self.raca


    def set_raca(self, raca):
        self.raca = raca


class Vaca(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, posx, posy, raca):
        super().__init__(nome, cor, sexo, velocidade, peso, estamina, posx, posy)
        self.raca = raca

    def emitir_som(self):
        print(f"o {self.nome} está mugindo")

    def getRaca(self):
        return self.raca

    def setRaca(self, raca):
        self.raca = raca


class Camaleao(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, posx, posy):
        super().__init__(nome, cor, sexo, velocidade, peso, estamina, posx, posy)


class Rato(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, posx, posy, tipo):
        super().__init__(nome, cor, sexo, velocidade, peso, estamina, posx, posy)
        self.tipo = tipo

    def emitir_som(self):
        print(f"o {self.nome} está guinchando")
    
    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

def andar(self, distancia):
    self.estamina -= distancia
    if self.estamina < 0:
            self.estamina = 0
    else:
        self.posicao_x += distancia