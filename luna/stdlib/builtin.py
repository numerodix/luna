from luna import objects as obj


def lua_print(luavalue):
    pyvalue = 'nil'

    if type(luavalue) == obj.LString:
        pyvalue = luavalue.value

    elif type(luavalue) == obj.LNumber:
        pyvalue = luavalue.value
        if int(pyvalue) == pyvalue:
            pyvalue = int(pyvalue)

    print(pyvalue)
