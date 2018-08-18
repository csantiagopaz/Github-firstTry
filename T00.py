from collections import namedtuple
from collections import deque
Email = namedtuple('Email', ['User', 'Senha'])
usuarios_uc = []
usuario_puc_ing= []
class DCcoreos:
	def __init__(self, user, password):
        self.user = user
		self.password = password
    # esa funcion creat es solo para garantizar se cumpre con las cosas pedidas por la U
    #
    def creat(self):
        pre_user=input("Usuario :")
        direção_de_serviço = input("Para utilizar a direção de serviço @uc.cl digite 1, /"
                                   "para utilizar a direção de serviço @ing.puc.cl digite 2")

        problemas_senha = []
        problemas = []

        for letter in pre_user:
            if letter in dinied_charct:
                problemas.append("Seu usuario possui caracteres não permitidos")
        if int(direção_de_serviço) == 1:
            if pre_user in usuarios_uc:
                problemas.append("Ja existe um usuario com esse nome em @uc.cl")
        elif int(direção_de_serviço) == 2:
            if pre_user in usuario_puc_ing:
                problemas.append("Ja existe um usuario com esse nome em @ing.puc.cl")
        elif len(pre_user)<6:
            problemas.append("Seu Usuario possui menos de 6 caracteres")
        else:
            if int (direção_de_serviço) == 1:

                user = str(pre_user) + "@uc.cl"
                usuarios_uc.append(user)
            elif int( direção_de_serviço) == 2:
                user = str(pre_user) + "@ing.puc.cl"
            pre_password = input("Escolha uma senha:")
            elif pre_user in pre_password:
                problemas_senha.append("A sua senha não pode conter o nome de usuario")
            elif len(pre_password)<6:
                problemas_senha.append("A sua senha deve conter 6 ou mais caracteres")
            elif "," in pre_password or ";" in pre_password:
                problemas_senha.append("a sua senha não pode conter , ou ;")
            else:
                password_confirma = input("Confirme sua senha :")
                if password_confirma == pre_password:
                    password = pre_password
                else:
                    print("As senhas não são iguais")
        elif len(problemas_senha) and len(problemas) == 0:

# ¿ estas bueno ese return ? ó tengo que hacer self.user = Email(etc)?
# deberia ser cada usuario con su user y su password , el dic seria el mejor banco de datos
# para eso?
            return email = Email(self.user,self.password)


    #def login(self):
       # loginn=input()
        #if loginn not in usuarios_uc and not in usuario_puc_ing
           # print("Usuario no encontrado")
       # elif loginn in todos_usuarios:
           # senha=input()
           # if loginn.password==senha:
            #    login_state = True
           # else:
              #  print("senha incorreta")

denied_charct = {"☺☻♥♦♣♠•◘○*+-*\/)([]{}}áâàéêèúûùóôòíîì|°,;:><&%$#!¡¿?"}
login_state = False