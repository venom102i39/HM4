class MovaProgramuvannya:
    def __init__(self, name):
        self.name = name
    def vyvesty_pryvytannya(self):
        print(f"Вітаю! Я — мова програмування {self.name}.")
class Python(MovaProgramuvannya):
    def vyvesty_pryvytannya(self):
        print("Привіт! Я Python — проста та потужна мова програмування.")
class Java(MovaProgramuvannya):
    def vyvesty_pryvytannya(self):
        print("Привіт! Я Java — надійна мова для великих проєктів.")
class JavaScript(MovaProgramuvannya):
    def vyvesty_pryvytannya(self):
        print("Привіт! Я JavaScript — мова вебу та інтерактивності.")
py = Python("Python")
java = Java("Java")
js = JavaScript("JavaScript")
py.vyvesty_pryvytannya()
java.vyvesty_pryvytannya()
js.vyvesty_pryvytannya()
