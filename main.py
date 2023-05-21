S = """
klasa: Betoniarka

- maks pojemność : stała dla betoniarki, definiowana przy jej tworzeniu
- liczba kg piachu
- liczba kg cementu
- liczba l wody

- podlaczenie do pradu
- wlaczenie silnika

- moze produkowac beton o zdefiniwoanej jakosci

Funkcjonalność:
- przy wykonywaniu betonu betoniark informuje o jakosci wykonywanego betonu (idealnie powinno być 4:2:1 piach:woda:cement)

"""


class Betoniarka:
    def __init__(self, maks_pojemnosc):
        self.maks_pojemnosc = maks_pojemnosc
        self.ilosc_wody = 0
        self.ilosc_piachu = 0
        self.ilosc_cementu = 0
        self.ilosc_cementu = 0
        self.ilosc_betonu = 0
        self.silnik_wlaczony = False

    def zmien_stan_wlaczenia(self):
        self.silnik_wlaczony = not self.silnik_wlaczony

    def wrzuc_materialy(self, woda=0, piach=0, cement=0):
        """Dodać materiały do mieszalnika"""
        objetosc_wrzucanych_materialow = woda + piach + cement
        if self.maks_pojemnosc < self.ilosc_betonu + self.ilosc_cementu + self.ilosc_piachu + self.ilosc_cementu + objetosc_wrzucanych_materialow:
            print("Przeladowanie mieszalnika")
        else:
            self.ilosc_wody += woda
            self.ilosc_piachu += piach
            self.ilosc_cementu += cement




    def wyprodukuj_beton(self):
        # sprawdz przewidywana jakosc
        # zapytaj czy beton powinien zostac wykonany
        print("Czy beton powinien zostać wykonany?")
        do_concrete = input("Tak/Nie: ")
        if do_concrete == "Tak":
            self.wyprodukuj_beton()
            self.ilosc_betonu = self.ilosc_cementu + self.ilosc_piachu + self.ilosc_wody
            self.ilosc_wody = 0
            self.ilosc_piachu = 0
            self.ilosc_cementu = 0
        else:
            pass


    # def wlacz_silnik(self):
    #     self.silnik_wlaczony=True

    def wypisz_stan(self):
        print(f"Betoniarka ma {self.maks_pojemnosc}l pojemności\n"
              f"Betoniarka jest wlaczona: {self.silnik_wlaczony}\n"
              f"Aktualnie w betoniarce jest: \n"
              f" betonu: {self.ilosc_betonu}\n"
              f" piachu: {self.ilosc_piachu}\n"
              f" cementu: {self.ilosc_cementu}\n"
              f" wody: {self.ilosc_wody}\n")
              # f" jakość "

bet = Betoniarka(120)

bet.wypisz_stan()
bet.wrzuc_materialy(woda=10, piach=5, cement=2)
bet.wyprodukuj_beton()
bet.zmien_stan_wlaczenia()
bet.wypisz_stan()

# for jakosc in

"""
Klasa: Betoniarka

- maks pojemnosc : stała dla betoniarki, definiowana przy jej tworzeniu
- liczba kg piachu
- liczba kg cementu
- liczba l wody

- wlaczenie silnika

- moze produkowac beton o zdefiniowanej jakosci

Funkcjonalnosc:
- przy wykonywaniu betonu betoniark informuje o jakosci wykonywanego betonu (idealnie powinno być 4:2:1 piach:woda:cement)
"""

