from flask import Flask, jsonify
import nxt
import nxt.locator 
import nxt.brick
import time

app = Flask(__name__)

@app.route('/dados')
def get_dados():
    try:
        bob = nxt.locator.find(host="00:16:53:09:72:DE")
        bob.start_program("Bob6.rxe")
        r = 2.75
        L = 17
        OmegaL = 0
        OmegaR = 0 
        Vxg = 0
        TETAg = 0
        
        MotorLeft = bob.get_motor(nxt.motor.Port.B)
        Iposition_left = MotorLeft.get_tacho()
        MotorRight = bob.get_motor(nxt.motor.Port.C)
        IPosition_right = MotorRight.get_tacho()
        to = time.time_ns()
        
        time.sleep(0.1)  # 100 ms de pausa para cálculo
        
        Fposition_left = MotorLeft.get_tacho()
        Fposition_right = MotorRight.get_tacho()
        tf = time.time_ns()
        
        OmegaL = (Fposition_left - Iposition_left) / (tf - to)
        OmegaR = (Fposition_right - IPosition_right) / (tf - to)
        
        Vxg = (r * OmegaR / 2) + (r * OmegaL / 2)
        TETAg = ((r * OmegaR / 2 * L) - (r * OmegaL / 2 * L))
        
        return jsonify({'Vxg': Vxg, 'TETAg': TETAg})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
