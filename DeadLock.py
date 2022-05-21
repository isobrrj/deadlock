import threading

impressora = threading.Lock()
camera = threading.Lock()

def gesonel():
    impressora.acquire()
    print("Gesonel está usando a impressora")

    print("Gesonel solicita a câmera")
    camera.acquire()

    print("Gesonel termina de usar os recursos")

    camera.release()
    impressora.release()

def julieta():
    camera.acquire()
    print("Julieta está usando a câmera")

    print("Julieta está solicitando a impressora")
    impressora.acquire()

    print("Julieta termina de usar os recursos")

    impressora.release()
    camera.release()

def main():
    t_A = threading.Thread(target=gesonel, args=[])
    t_B = threading.Thread(target=julieta, args=[])
    
    t_A.start()
    t_B.start()

    t_A.join()
    t_B.join()

main()

