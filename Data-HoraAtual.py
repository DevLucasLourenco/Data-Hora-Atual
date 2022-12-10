import time as t


data_atual = t.localtime()
ano, mes, dia, hora, minuto, seg, dia_semana, dia_ano, isdst = data_atual



def adaptar_item(item):
    if item < 10:
        
        return '0' + str(item)
    else:
        return item  


def hora_setup():
    return f'{adaptar_item(dia)}/{adaptar_item(mes)}/{ano} - {adaptar_item(hora)}:{adaptar_item(minuto)}'

if __name__ =="__main__":
    print(hora_setup())
    