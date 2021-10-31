spin = "robotID"
spin2 = "ArmID"

turning_speedRight = "40"

while 1:
    # Keys for moving around
    if api.isPressed("w"):
        api.setSpinSpeed(-100, 100, spin)
        
    elif api.isPressed("s"):
        api.setSpinSpeed(100, -100, spin)
        
    elif api.isPressed("a"):
        api.setSpinSpeed(-70, -70, spin)
        
    elif api.isPressed("d"):
        api.setSpinSpeed(70, 70, spin)
        
    elif api.isPressed("q"):
        api.setSpinSpeed(-80, 50, spin)
        
    elif api.isPressed("e"):
        api.setSpinSpeed(-50, 80, spin)
        
    elif api.isPressed("z"):
        api.setSpinSpeed(80, -50, spin)
        
    elif api.isPressed("c"):
        api.setSpinSpeed(50, -80, spin)
        
    elif api.isPressed("w" and "a"):
        api.setSpinSpeed(-80, 70, spin)
    
    # Keys for arm
    
    elif api.isPressed("k"):
        api.setPos(0, 90, spin2)
        api.setSpeed(100, 100, spin2)
        
    elif api.isPressed("l"):
        api.setPos(0, -80, spin2)
        api.setSpeed(100, 100, spin2)
        
    elif api.isPressed("æ"):
        api.setPos(0, 0, spin2)
        api.setSpeed(100, 100, spin2)

    elif api.isPressed("u"):
        a = api.readJointSensor("cm", spin2)
        a =+ 5
        api.setPos(0, -50, spin2)
        
    elif api.isPressed("j"):
        a = api.readJointSensor("cm", spin2)
        a =+ 5
        api.setPos(0, 50, spin2)
    
    # Keys for if is not pressed
    
    elif not api.isPressed("w" or "a" or "d" or "s"):
        api.setSpinSpeed(0, 0, spin)
    
    