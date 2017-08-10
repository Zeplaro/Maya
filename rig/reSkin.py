import maya.cmds as mc
from tbx import get_skinCluster

# todo : fix try except when bpm already connected

def do_reSkin(*objs):

    if not objs:
        objs = mc.ls(sl=True, fl=True)
    if not objs:
        mc.warning('Select at least one object')
        return
    for obj in objs:
        skn = get_skinCluster(obj)
        infs = mc.skinCluster(skn, q=True, inf=True)
        for inf in infs:
            conns = mc.listConnections(inf+'.worldMatrix', type='skinCluster', p=True)
            for conn in conns:
                bpm = conn.replace('matrix', 'bindPreMatrix')
                wim = mc.getAttr(inf+'.worldInverseMatrix')
                try:
                    mc.setAttr(bpm, *wim, type='matrix')
                except:
                    pass
        mc.skinCluster(skn, e=True, rbm=True)
    return objs
