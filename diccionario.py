auto = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 2022,
    "placa": "LQN287",
    "kilometraje": 20000,
    "ciudad_de_compra": "Cali"
}
print(auto["modelo"])

#MODIFICAR ELEMENTOS
auto["año"] = 2023

#AÑADIR ELEMENTOS
auto["color"] = "Rojo"

print(auto)

#ELIMINAR ELEMENTOS
del auto["modelo"]
auto.pop("marca")
print(auto)