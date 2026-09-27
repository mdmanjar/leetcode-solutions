class Solution:
    def bestTower(self, towers: list[list[int]], center: list[int], radius: int) -> list[int]:
        rx = -1
        ry = -1
        rq = -1
        cx = center[0]
        cy = center[1]
        for t in towers:
            tx = t[0]
            ty = t[1]
            tq = t[2]
            d = abs(tx - cx) + abs(ty - cy)
            if d > radius: continue
            if rq > tq: continue
            if rq < tq or (tx < rx or (tx == rx and ty < ry)):
                rx = tx
                ry = ty
                rq = tq
        return [rx, ry]