Welcome to the blender-ndp wiki!
Blender's standart primitives have a flaw: after you've created them, you're stuck with them as is.
You can't just edit properties to change the sphere's resolution; you can't change amount of sides on the cylinder; etc.

NDPs to the rescue!
'NDP' stands for 'Non-Destructive Primitive', which is what this plugin is supposed to do: add primitives, which's properties you can edit at any time.

But with great power comes great... um... limitations.
The only way you can edit the geometry of NDPs are
- Primitive params(size, divisions, etc)
- Non-applied modifier stack

If you want to do anything else with them(move vertices by hand, add uvs, etc), you have to convert them to regular meshes. And you can't revert them back to NDP-s(this is done intenionally so you won't lose you progress after primitive's mesh re-generation).

I tried my best to make this addition to blender as intuitive as possible, so I hope you'll find it useful.

After installing the plugin, the following things should change:
1) Shift+A (Add) menu now has an extra submenu at the top called 'Non-Destructive' with all the supported NDP types.
2) Alt+C with a selected NDP brings up a dialog for converting into a mesh;
3) Alt+C with a selected non-NDP object opens up the default convert menu(as it did in blender 2.79b);
4) Ctrl+W toggles wireframe state. I thought such a hotkey would be helpful, considering editing NDP always turns on its wireframe to better see divisions.
5) Entering 'Edit Mode' with a selected NDP will open up the 'Edit NDP' popup. This is done intentionally so you won't lose progress after putting time into tweaking geometry.

Some things to be ware of:
- NDP data is attached to mesh data, so in case of several NDPs sharing a mesh(instances), converting one will convert them all. If that's not what you want, first make a mesh unique and only then convert.
- Edit mode is not the only way of destructively changing geometry. And, unfortunately, I can't restrict every way of altering the NDP's geometry without converting it first: you can apply modifiers, merge meshes, etc. Doing so might screw you up, so be ware.
- Considering that there's already WonderMesh(which is free on github, is supported and has more shapes), me continuing the project is unlikely, so take this project as is. In my opinion, it's more intuitive and handy, but that's about it.

P.S.
While doing the project, I found out I had no need for NDPs.
Standart primitives are good enough for most cases and the restrictions that NDPs bring are too high.
I need non-destructive workflow in cases where I know exactly what might change and how I'd change it. Where the parameters of iterations are transparent.
And primitives do not cover those parameters at all.
The best usages I can find are: sometimes I need my screws to have some additional sides and now I can have an easily editable grid with wireframe modifier.

This is the main reason why I'm leaving the project as is (perhaps with the exception of fixing some bugs here and there) and moving on to greater things.

But that's me. Maybe you're different. Maybe you need this. Maybe there are a lot of you, who do need this and find this to be promising.
In such a case, I might change my mind and continue on.
This is a finished product that you can work with. I gave you everything to decide, whether it's worth it or not.
