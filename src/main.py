from grid_class import GridGraphics
import grid_settings as st


g = GridGraphics(20, 20)

cnt = 0
while True:
    if cnt % 400 == 0 and cnt > 0:
        g.clear_all()
    g.color_square(cnt % 20, (cnt // 20)%20, st.GREEN if cnt % 3 ==0 else st.BLUE)
    g.hold(0)
    g.update()
    cnt += 1
