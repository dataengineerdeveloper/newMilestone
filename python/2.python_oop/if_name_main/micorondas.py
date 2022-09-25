from camera import tirar_foto

#uma vez que foi importante um modulo a propriedade de main vai passar a chamar-se de camera

def fazer_pipoca():
    print('fazer pipocas...')
    print(__name__)
    
if __name__ == "__main__":
    #fazer_pipoca()
    tirar_foto()#correndo desta forma o output vai ser tirar foto /camera
    