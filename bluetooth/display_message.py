import nxt
from nxt.locator import find_one_brick

# Conecte-se à Brick NXT
brick = find_one_brick()

# Escreva uma mensagem na tela
try:
    brick.lcd.display_text("Olá, NXT!")
except Exception as e:
    print("Erro ao exibir a mensagem:", e)
finally:
    # Desconecte do NXT após o uso
    brick.sock.close()
