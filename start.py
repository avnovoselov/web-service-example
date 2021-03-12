from server import server

if __name__ == "__main__":
    server.run(
        host='0.0.0.0',  # какой адрес слушаем
        port=5000,  # на каком порту
        debug=False
    )
