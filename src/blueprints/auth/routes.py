# pylint: disable=unused-argument, no-member, arguments-differ, no-value-for-parameter

""" Autenticação de usuario """

from flask import Blueprint, request, session, render_template, g, redirect, url_for
from .user import User
from src.database.querys import EquipamentosQuerys, ClientesQuerys, OperacoesQuerys

auth_app = Blueprint(
    "auth_app",
    __name__,
)

users = []
users.append(User(id=1, username="Vitor", password="123"))
users.append(User(id=2, username="vitor", password="123"))
users.append(User(id=3, username="Mariano", password="1515"))
users.append(User(id=4, username="mariano", password="1515"))


@auth_app.route("/", methods=["GET", "POST"])
def index():
    equipamentos = EquipamentosQuerys().mostrar()
    total = len(equipamentos)
    clientes = ClientesQuerys.mostrar()
    total_clientes = len(clientes)
    operacoes = OperacoesQuerys.mostrar().all()[::-1]
    total_operacoes = len(operacoes)
    return render_template("/pages/equipamento/index.html",total=total,total_clientes=total_clientes,total_operacoes=total_operacoes)
