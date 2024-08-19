# 
# check list box
# 
self._clbTest.FormattingEnabled = True
self._clbTest.Location = System.Drawing.Point(136, 278)
self._clbTest.Name = "clbTest"
self._clbTest.Size = System.Drawing.Size(172, 94)
self._clbTest.TabIndex = 17
for lv in levels:
    self._clbTest.Items.Add(lv)
# 
# cbbSourceFile
# 
self._cbbSourceFile.FormattingEnabled = True
self._cbbSourceFile.Location = System.Drawing.Point(125, 19)
self._cbbSourceFile.Name = "cbbSourceFile"
self._cbbSourceFile.Size = System.Drawing.Size(183, 21)
self._cbbSourceFile.TabIndex = 5
self._cbbSourceFile.Items.AddRange(System.Array[System.Object](typeSource))
self._cbbSourceFile.SelectedIndex = 0