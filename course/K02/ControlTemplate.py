
#Combobox
self._cbbx_sel_file.FormattingEnabled = True
self._cbbx_sel_file.DisplayMember = "Name"
self._cbbx_sel_file.Location = System.Drawing.Point(134, 28)
self._cbbx_sel_file.Name = "cbbx_sel_file"
self._cbbx_sel_file.Size = System.Drawing.Size(198, 24)
self._cbbx_sel_file.TabIndex = 1
self._cbbx_sel_file.SelectedIndexChanged += self.Cbbx_sel_fileSelectedIndexChanged
self._cbbx_sel_file.Items.AddRange(System.Array[System.Object](columns))

#textbox
self._txtb_ext_tab_path.Location = System.Drawing.Point(146, 23)
self._txtb_ext_tab_path.Name = "txtb_ext_tab_path"
self._txtb_ext_tab_path.Size = System.Drawing.Size(511, 20)
self._txtb_ext_tab_path.TabIndex = 1
self._txtb_ext_tab_path.Text = defaulExtPath

