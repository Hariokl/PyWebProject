import time


def base_style(t=None):
    hours = time.localtime()[3] if t is None else t % 24
    if 0 <= hours <= 12:
        br1, bg1, bb1 = 10 + hours * 8, 10 + hours * 10, 50 + hours * 17
        br2, bg2, bb2 = 250, 10 + hours * 10, 58 - hours * 4
        tr, tg, tb = 120 + hours * 11, 250, 250
    else:
        br1, bg1, bb1 = 106 - (hours - 12) * 8, 130 - (hours - 12) * 10, 254 - (hours - 12) * 17
        br2, bg2, bb2 = 250, 130 - (hours - 12) * 10, 10 + (hours - 12) * 4
        tr, tg, tb = 252 - (hours - 12) * 8, 250, 250
    deg = hours * 15
    # base = "body { background-color:" + f"rgb({r1}, {g1}, {b1})" + "; color:" + f"rgb({r2}, {g2}, {b2})" + "; }"
    base = "body { background: linear-gradient(" + f"{deg}deg, rgb({br2}, {bg2}, {bb2}), "
    base += f"rgb({br1}, {bg1}, {bb1})); color: " + f"rgb({tr}, {tg}, {tb})" + "; height: 100vh;}"
    return base, [(br1, bg1, bb1), (br2, bg2, bb2), (tr, tg, tb), deg]


def login_style(t=None):
    hours = time.localtime()[3] if t is None else t % 24
    if 0 <= hours <= 12:
        sr1, sg1, sb1 = 50 + hours * 8, 50 + hours * 11, 100 + hours * 12
        sr2, sg2, sb2 = hours * 4, hours * 8, 20 + hours * 15
    else:
        sr1, sg1, sb1 = 146 - (hours - 12) * 8, 182 - (hours - 12) * 11, 244 - (hours - 12) * 12
        sr2, sg2, sb2 = 48 - (hours - 12) * 4, 96 - (hours - 12) * 8, 180 - (hours - 12) * 15
    rgb = ", ".join(map(str, base_style(t)[1][2]))
    log = base_style(t)[0] + "section{background: linear-gradient(180deg, "
    log += f"rgb({sr1}, {sg1}, {sb1}), rgb({sr2}, {sg2}, {sb2}))" + "; }"
    log += '.but .registration{color: ' + f'rgb({rgb});' + '}'
    return log
