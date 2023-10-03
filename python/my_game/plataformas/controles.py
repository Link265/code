#controles


def controles_fun(entity,key):

    print(entity,key)

    keys = {
    "1073741903":entity.right,
    "1073741904":entity.left,
    "1073741905":entity.down,
    "1073741906":entity.up
    }
    keys[str(key)]()
