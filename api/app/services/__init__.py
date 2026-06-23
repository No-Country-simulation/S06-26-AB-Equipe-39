"""Camada de serviços — a lógica de negócio da API.

Os routers (HTTP) chamam estes serviços. Manter a lógica aqui facilita testar e,
mais tarde, trocar os mocks por banco/agente sem mexer na camada HTTP.
"""
