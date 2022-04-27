import time


def colors(t=None):
    hours = time.localtime()[3] if t is None else t % 24
    if 0 <= hours <= 12:
        br1, bg1, bb1 = 10 + hours * 8, 10 + hours * 10, 50 + hours * 17
        br2, bg2, bb2 = 250, 10 + hours * 10, 58 - hours * 4
        tr, tg, tb = 120 + hours * 11, 250, 250
        btnr, btng, btnb = 120 - hours * 6, 120 - hours * 6, 120 - hours * 6
    else:
        br1, bg1, bb1 = 106 - (hours - 12) * 8, 130 - (hours - 12) * 10, 254 - (hours - 12) * 17
        br2, bg2, bb2 = 250, 130 - (hours - 12) * 10, 10 + (hours - 12) * 4
        tr, tg, tb = 252 - (hours - 12) * 8, 250, 250
        btnr, btng, btnb = 48 + (hours - 12) * 6, 48 + (hours - 12) * 6, 48 + (hours - 12) * 6
    deg = hours * 15
    return [(br1, bg1, bb1), (br2, bg2, bb2), (tr, tg, tb), deg, (btnr, btng, btnb)]


def base_style(t=None):
    color = colors(t)
    # base = "body { background-color:" + f"rgb({r1}, {g1}, {b1})" + "; color:" + f"rgb({r2}, {g2}, {b2})" + "; }"
    base = "body { background: linear-gradient(" + f"{color[3]}deg, rgb({color[1][0]}, {color[1][1]}, {color[1][2]}), "
    base += f"rgb({color[0][0]}, {color[0][1]}, {color[0][2]})); color: " + f"rgb({color[2][0]}, {color[2][1]}, {color[2][2]})" + ";}"
    return base


def login_style(t=None):
    hours = time.localtime()[3] if t is None else t % 24
    if 0 <= hours <= 12:
        sr1, sg1, sb1 = 50 + hours * 8, 50 + hours * 11, 100 + hours * 12
        sr2, sg2, sb2 = hours * 4, hours * 8, 20 + hours * 15
    else:
        sr1, sg1, sb1 = 146 - (hours - 12) * 8, 182 - (hours - 12) * 11, 244 - (hours - 12) * 12
        sr2, sg2, sb2 = 48 - (hours - 12) * 4, 96 - (hours - 12) * 8, 180 - (hours - 12) * 15
    rgb = ", ".join(map(str, colors(t)[2]))
    log = base_style(t) + "section{background: linear-gradient(180deg, "
    log += f"rgba({sr1}, {sg1}, {sb1}, 0.4), rgba({sr2}, {sg2}, {sb2}, 0.4))" + "; }"
    log += '.registration{color: ' + f'rgba({rgb});' + '}'
    return log


def register_style(t=None):
    hours = time.localtime()[3] if t is None else t % 24
    if 0 <= hours <= 12:
        sr1, sg1, sb1 = 50 + hours * 8, 50 + hours * 11, 100 + hours * 12
        sr2, sg2, sb2 = hours * 4, hours * 8, 20 + hours * 15
    else:
        sr1, sg1, sb1 = 146 - (hours - 12) * 8, 182 - (hours - 12) * 11, 244 - (hours - 12) * 12
        sr2, sg2, sb2 = 48 - (hours - 12) * 4, 96 - (hours - 12) * 8, 180 - (hours - 12) * 15
    reg = base_style(t) + "section{background: linear-gradient(180deg, "
    reg += f"rgba({sr1}, {sg1}, {sb1}, 0.4), rgba({sr2}, {sg2}, {sb2}, 0.4))" + "; }"
    return reg


def home_style(t=None):
    color = colors(t)
    btn_t_rgb = color[2]
    btn_b_rgb = color[4]
    back_hover_rgb = btn_b_rgb[0] - 30, btn_b_rgb[0] - 30, btn_b_rgb[0] - 30
    dow = base_style(t)
    dow += ".confirm{" + f"color: rgb{btn_t_rgb};" + f"background: rgb{btn_b_rgb};" + '}'
    dow += ".confirm:hover{" + f"background: rgb{back_hover_rgb}" + "}"
    return dow


def download_style():
    color = colors()
    btn_t_rgb = color[2]
    btn_b_rgb = color[4]
    back_hover_rgb = btn_b_rgb[0] - 30, btn_b_rgb[0] - 30, btn_b_rgb[0] - 30
    dow = base_style()
    return dow
