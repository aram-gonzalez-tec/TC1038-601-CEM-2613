response = {
    "status": 200,
    "message": "Solicitud válida.",
    "content": {
        "img": "msdlmsdolmskmdsobs"
    }
}
response = {
    "status": 500,
    "error": "Error interno del servidor."
}
match response:
    case {"status": status, "content": {"img": img}} if status == 200:
        print(f"IMG: {img}")
    case {"status": 500, "error": error}:
        print(f"Error interno: {error}")
    case _:
        print("Formato no válido de la respuesta.")