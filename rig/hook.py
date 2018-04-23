import maya.cmds as mc


def do_hook(*objs):

    if not objs:
        objs = mc.ls(sl=True, tr=True, fl=True)
        if not objs:
            mc.warning('Select at least one object')
            return
    hooks = []
    for obj in objs:
        hook = mc.group(em=True, n='{}_hook'.format(obj))
        mmx = mc.createNode('multMatrix', n='mmx_{}'.format(obj))
        dmx = mc.createNode('decomposeMatrix', n='dmx_{}'.format(obj))
        mc.connectAttr('{}.worldMatrix[0]'.format(obj), '{}.matrixIn[1]'.format(mmx), f=True)
        mc.connectAttr('{}.parentInverseMatrix[0]'.format(hook), '{}.matrixIn[2]'.format(mmx), f=True)
        mc.connectAttr('{}.matrixSum'.format(mmx), '{}.inputMatrix'.format(dmx), f=True)
        mc.connectAttr('{}.outputShear'.format(dmx), '{}.shear'.format(hook), f=True)
        mc.connectAttr('{}.outputTranslate'.format(dmx), '{}.translate'.format(hook), f=True)
        mc.connectAttr('{}.outputScale'.format(dmx), '{}.scale'.format(hook), f=True)
        mc.connectAttr('{}.outputRotate'.format(dmx), '{}.rotate'.format(hook), f=True)
        hooks.append(hook)
    return hooks
