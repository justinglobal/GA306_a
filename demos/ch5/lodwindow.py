import pymel.core as pm

class LODWindow(object):
    """A pymel class for an level-of-detail editing window"""
    ## unique handle for the window
    WINDOW_NAME = 'LOD Window'
    def tag_nodes(self, node_list, res='Low'):
        """tag the supplied nodes with the supplied resolution"""
        for node in node_list:
            # add gameRes attribute if needed
            if not node.hasAttr('gameRes'):
                node.addAttr('gameRes', dataType='string')
            node.gameRes.set(res, type='string')
    def create(self):
        # destroy the window if it already exists
        try:
            pm.deleteUI(self.WINDOW_NAME, window=True)
        except: pass
        # draw the window
        with pm.window(self.WINDOW_NAME) as res_window:
            with pm.columnLayout(adjustableColumn=True):
                with pm.horizontalLayout():
                    pm.text(label='Resolution')
                    with pm.optionMenu() as self.res_menu:
                        pm.menuItem(l='Low')
                        pm.menuItem(l='Med')
                        pm.menuItem(l='Hi')
                    set_res_btn = pm.button(
                        label='Set LOD',
                        command=pm.Callback(self.on_set_res_btn)
                    )
                pm.separator(style='in', height=4)
                with pm.horizontalLayout() as h1:
                    pm.text(label='Low')
                    select_low_btn = pm.button(
                        label='Select All',
                        command=pm.Callback(
                            self.on_select_btn,
                            'Low'
                        )
                    )
                    toggle_low_btn = pm.button(
                        label='Toggle Visibility',
                        command=pm.Callback(
                            self.on_vis_btn,
                            'Low'
                        )
                    )
                with pm.horizontalLayout() as h1:
                    pm.text(label='Medium')
                    select_med_btn = pm.button(
                        label='Select All',
                        command=pm.Callback(
                            self.on_select_btn,
                            'Med'
                        )
                    )
                    toggle_med_btn = pm.button(
                        label='Toggle Visibility',
                        command=pm.Callback(
                            self.on_vis_btn,
                            'Med'
                        )
                    )
                with pm.horizontalLayout() as h1:
                    pm.text(label='High')
                    select_hi_btn = pm.button(
                        label='Select All',
                        command=pm.Callback(
                            self.on_select_btn,
                            'Hi'
                        )
                    )
                    toggle_hi_btn = pm.button(
                        label='Toggle Visibility',
                        command=pm.Callback(
                            self.on_vis_btn,
                            'Hi'
                        )
                    )
                self.status_line = pm.textField(editable=False)
            res_window.setWidthHeight((350,140))
    def on_set_res_btn(self, *args):
        """action to execute when Set LOD button is pressed"""
        # filter selection to only include meshes
        selected = [
            i for i in pm.ls(sl=True) if (
                type(i.getShape())==pm.nt.Mesh)
        ]
        res = self.res_menu.getValue()
        if selected:
            self.tag_nodes(selected, res)
            self.status_line.setText(
                'Set selection to resolution %s'%res
            )
        else:
            self.status_line.setText('No selection processed.')
    def on_select_btn(self, *args):
        """action to execute when Select All button is pressed"""
        # get all the meshes in the scene
        poly_meshes = [
            i for i in pm.ls(
                type=pm.nt.Transform
            ) if type(i.getShape())==pm.nt.Mesh
        ]
        if poly_meshes:
            # select anything with the gameRes attribute and the appropriate value
            pm.select(
                [i for i in poly_meshes if (
                    i.hasAttr('gameRes') and
                    i.gameRes.get()==args[0])
                ]
            )
            self.status_line.setText(
                'Selected %s resolution meshes'%args[0]
            )
        else:
            self.status('Nothing else selected')
    def on_vis_btn(self, *args):
        """action to execute when the Toggle Visiblity button is pressed"""
        # filter list to only include meshes
        poly_meshes = [
            i for i in pm.ls(type=pm.nt.Transform) if (
                type(i.getShape())==pm.nt.Mesh)
        ]
        if poly_meshes:
            # get everything with the current resolution
            res = [i for i in poly_meshes if (
                i.hasAttr('gameRes') and i.gameRes.get()==args[0])
            ]
            if res:
                for j in res:
                    # flip visibility
                    j.visibility.set(1-int(j.visibility.get()))