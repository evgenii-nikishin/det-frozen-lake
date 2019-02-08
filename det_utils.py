def to_coord(num, grid_size=8):
    return (num // grid_size, num % grid_size)
    
def to_num(coord, grid_size=8):
    return coord[0]*grid_size + coord[1]

def crop_coord(coord, grid_size=8):
    return min(max(coord[0], 0), grid_size-1), min(max(coord[1], 0), grid_size-1)

def coord_ac(a):
    d = {0: (0,-1), 1: (1,0), 2: (0,1), 3:(-1,0)}
    return d[a]

def next_s(s, a, grid_size=8):
    s_c = to_coord(s, grid_size=grid_size)
    a_c = coord_ac(a)
    return to_num(crop_coord((s_c[0]+a_c[0], s_c[1]+a_c[1]), grid_size=grid_size), 
                  grid_size=grid_size)

def make_det(env):
    assert env.env.ncol == env.env.nrow
    for s in range(env.env.nS):
        for a in range(env.env.nA):
            if len(env.env.P[s][a]) > 1:
                s_new = next_s(s, a, grid_size=env.env.ncol)
                tmp = list(filter(lambda x: x[1] == s_new, env.env.P[s][a]))
                # assert len(tmp)>0, '{} {}'.format(s, a)
                corrected_P = tmp[0]
                env.env.P[s][a] = [(1.0,) + corrected_P[1:]]
    return env
