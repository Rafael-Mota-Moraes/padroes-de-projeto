from abc import ABC, abstractmethod


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self):
        print('Carro de luxo ZN está buscando o cliente...')


class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self):
        print('Carro popular ZN está buscando o cliente...')


class MotoZN(VeiculoPopular):
    def buscar_cliente(self):
        print('Moto está ZN buscando o cliente...')


class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self):
        print('Carro de luxo ZS está buscando o cliente...')


class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self):
        print('Carro popular ZS está buscando o cliente...')


class MotoZS(VeiculoPopular):
    def buscar_cliente(self):
        print('Moto está ZS buscando o cliente...')


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo:
        pass

    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular:
        pass

    @staticmethod
    @abstractmethod
    def get_moto() -> VeiculoPopular:
        pass


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZN()

    @staticmethod
    def get_moto() -> VeiculoPopular:
        return MotoZN()


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZS()

    @staticmethod
    def get_moto() -> VeiculoPopular:
        return MotoZS()


class Cliente:
    def busca_clientes(self):
        for factory in [ZonaSulVeiculoFactory(), ZonaNorteVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto = factory.get_moto()
            moto.buscar_cliente()

            print()
            print()


if __name__ == "__main__":
    c = Cliente()
    c.busca_clientes()
